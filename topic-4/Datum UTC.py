from datetime import datetime  
import pytz  
utc = datetime.now(pytz.utc)  
print(utc)

berlin = pytz.timezone('Europe/Berlin')
berlintime = berlin.localize(datetime.now())
print(berlintime)