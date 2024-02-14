from datetime import datetime

today_with_sec = datetime.now()
y=today_with_sec.replace(microsecond=0)
print(y)
