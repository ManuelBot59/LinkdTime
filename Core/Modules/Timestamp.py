# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from datetime import datetime,timedelta
from Core.Utils import Format

class GET:
 
    @staticmethod
    def Date(timestamp,timezone):
        timestamp = float(timestamp)
        date_format = Format.GET.Date_format()
        hours_format = Format.GET.Hour_format()
        orig_format = "%Y-%m-%d %H:%M:%S"
        timestamp = timestamp/1000
        intial = datetime.fromtimestamp(timestamp)
        if timezone != "GMT+2:00":
            zone = timezone.split("GMT",1)[1].replace("+","").replace("-","")
            hours_t = zone.split(":",1)[0]
            minute_t = zone.split(":",1)[1]
            hours_t = int(hours_t)
            if "+" in timezone:
                hours_t = hours_t - 2
            elif "-" in timezone:
                hours_t = hours_t + 2
            zone = timedelta(hours=hours_t,minutes=int(minute_t))
            if "+" in timezone:
                intial = intial + zone
            elif "-" in timezone:
                intial = intial - zone
        formatted = intial.strftime(date_format)
        or_formatted = intial.strftime(orig_format)
        if hours_format == 1:
            pass
        else:
            formatted_hour = formatted[11] + formatted[12]
            int_formatted_hour = int(formatted_hour)
            if int_formatted_hour <= 12:
                f_formatted_hour = str(formatted_hour)
            else:
                f_formatted_hour1 = int_formatted_hour-12
                f_formatted_hour_list = str(f_formatted_hour1)
                count = f_formatted_hour_list.count(".")
                f_formatted_hour = f_formatted_hour_list.split(".",count)[0]
            formatted = formatted.replace(formatted_hour,str(f_formatted_hour))
            if int(int_formatted_hour) < 12:
                formatted = formatted + " AM"
            elif int(int_formatted_hour) == 24:
                formatted = formatted + " AM"
            else:
                formatted = formatted + " PM"
        return formatted,or_formatted
