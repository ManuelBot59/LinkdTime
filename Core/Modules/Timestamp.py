from datetime import datetime, timedelta
from Core.Utils import Format
from tzlocal import get_localzone
import pytz

class GET:
    @staticmethod
    def Date(timestamp, timezone):
        timestamp = float(timestamp)
        date_format = Format.GET.Date_format()
        hours_format = Format.GET.Hour_format()
        orig_format = "%Y-%m-%d %H:%M:%S"
        timestamp = timestamp / 1000
        dt_utc = datetime.utcfromtimestamp(timestamp)

        if timezone.lower() == "auto" or timezone.strip() == "":
            local_tz = get_localzone()
            dt_local = dt_utc.replace(tzinfo=pytz.utc).astimezone(local_tz)
            offset_seconds = dt_local.utcoffset().total_seconds()
            offset_hours = int(offset_seconds // 3600)
            offset_minutes = int((offset_seconds % 3600) // 60)
            sign = "+" if offset_hours >= 0 else "-"
            tz_offset = f"UTC{sign}{abs(offset_hours):02d}:{abs(offset_minutes):02d}"
            tz_name = f"{local_tz} ({tz_offset})"
        else:
            try:
                offset_sign = 1 if "+" in timezone else -1
                hours, minutes = map(int, timezone.replace("GMT", "").replace("+", "").replace("-", "").split(":"))
                delta = timedelta(hours=hours * offset_sign, minutes=minutes * offset_sign)
                dt_local = dt_utc + delta
                tz_name = timezone
            except:
                dt_local = dt_utc
                tz_name = "UTC"

        formatted = dt_local.strftime(date_format)
        or_formatted = dt_local.strftime(orig_format)

        if hours_format == 0:
            hour = dt_local.strftime("%I")
            am_pm = dt_local.strftime("%p")
            formatted = formatted[:11] + hour + formatted[13:] + f" {am_pm}"

        return formatted, or_formatted, tz_name