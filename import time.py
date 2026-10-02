import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=int(time.strftime('%M'))  
print(timestamp)    
timestamp=int(time.strftime('%S'))
print(timestamp)
import time
current_hour=int(time.strftime('%H'))
print("Abhi ka time (Hour) hai:",current_hour)
if current_hour<12:
    print("Good Morning sir!")
elif current_hour>17:
    print("Good Evening!")
else:
    print("Good After Noon Sir!")



       
    
