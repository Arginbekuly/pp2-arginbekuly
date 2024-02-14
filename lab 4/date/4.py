from datetime import datetime

def diff():
    x=datetime.datetime.now()
    y=datetime.datetime.now()-datetime.timedelta(days=7)
    delta=x-y
    return delta.total_seconds()
print(diff())
