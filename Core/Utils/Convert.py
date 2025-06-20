import datetime
import pytz

def To_Local_Zone(timestamp):
    utc_dt = datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
    local_dt = utc_dt.astimezone()
    return local_dt

def Get_UTC_Offset(local_dt):
    offset = local_dt.utcoffset()
    total_minutes = int(offset.total_seconds() // 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"UTC{hours:+03}:{minutes:02}"
