
# Archivo: Timestamp.py modificado
# Conversión de timestamp ajustado a zona horaria local

from datetime import datetime
import pytz
import tzlocal

def convert_timestamp(ts):
    local_timezone = tzlocal.get_localzone()
    dt = datetime.fromtimestamp(ts, pytz.utc)
    local_dt = dt.astimezone(local_timezone)
    return local_dt.strftime('%Y-%m-%d %H:%M:%S'), str(local_timezone)

if __name__ == '__main__':
    ts = 1718803200  # Ejemplo: 20 junio 2024 00:00:00 UTC
    local_time, tz_name = convert_timestamp(ts)
    print(f"Hora local convertida: {local_time} ({tz_name})")
