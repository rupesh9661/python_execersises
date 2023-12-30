import datetime

current_date=datetime.datetime.now()
current_time=current_date.strftime("%H:%M")

if(current_time>="6:00" and current_time<"12:00"):
    print("Good Morning Rupesh")
elif(current_time>="12:00" and current_time<"18:00"):
    print("Good Afternoon Rupesh")
else:
    print("Good Evening Rupesh ")    
