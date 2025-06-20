
# Archivo: Start.py modificado
# Este script maneja la detección de zona horaria local y ajusta la hora a UTC-5

import pytz
from datetime import datetime
import tzlocal

def get_local_time():
    local_timezone = tzlocal.get_localzone()
    now = datetime.now(local_timezone)
    return now.strftime('%Y-%m-%d %H:%M:%S'), str(local_timezone)

def convert_to_utc_offset(tz_name):
    tz = pytz.timezone(tz_name)
    now = datetime.now(tz)
    offset = now.utcoffset().total_seconds() / 3600
    return f"UTC{offset:+.0f}"

if __name__ == '__main__':
    local_time, tz_name = get_local_time()
    offset = convert_to_utc_offset(tz_name)
    print(f"Hora local: {local_time} ({tz_name} - {offset})")
