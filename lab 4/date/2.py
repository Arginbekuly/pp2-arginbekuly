from datetime import datetime , timedelta
today=datetime.now()
yesteday=datetime.now()-timedelta(days=1)
tomorraw=datetime.now()+timedelta(days=1)
print("today:",today,"\nyesteday:",yesteday,"\ntomorraw:",tomorraw,sep=" ")