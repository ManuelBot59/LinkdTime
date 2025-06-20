import datetime
import pytz
from Core.Utils import Colors, Convert
from Core.Utils import Timestamp

def Scan(link, printable, users, conversion, types, timezone, orig_conversion):
    timestamp = Timestamp.GET.Timestamp(link)
    if timestamp == "None":
        print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "Timestamp Not Found")
        conversion.append("Unknown")
        orig_conversion.append("Unknown")
    else:
        local_datetime = Convert.To_Local_Zone(timestamp)
        timezone_str = local_datetime.strftime('%Z')
        offset_str = Convert.Get_UTC_Offset(local_datetime)
        tz_display = f"{local_datetime.tzinfo} ({offset_str})"

        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + f"Timestamp Found: {timestamp}")
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + f"Converted Time: {local_datetime} {tz_display}")

        conversion.append(str(local_datetime))
        orig_conversion.append(timestamp)

    types.append("Post")
    users.append("Unknown")
