import datetime as dt

def ms(t):
  if isinstance(t, dt.timedelta):
    return t.total_seconds() * 1000
  elif isinstance(t, dt.datetime):
    return (t - dt.datetime(1970,1,1)).total_seconds() * 1000

def midnight(date:dt.date):
  return dt.datetime.combine(date, dt.datetime.min.time()) 