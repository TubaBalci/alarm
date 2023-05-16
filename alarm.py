import webbrowser
from datetime import datetime

timeStr = input("Alarm saati giriniz eg.: 18.50\n")

time_lst = timeStr.rsplit(".")

t = datetime.now().timetuple()

inputHour = int(time_lst[0])
inputMin = int(time_lst[1])
hour = int(t[3]); min = int(t[4])

if(inputHour > 24  or inputHour < 0  or inputMin > 60  or inputMin < 0):
    print("Geçersiz saat")
elif(inputHour <= hour and inputMin < min ):
    print("Alarm saati geçti")   
else:
    while(not hour==inputHour or not min==inputMin):
        t = datetime.now().timetuple()
        hour = int(t[3]); min = int(t[4])
    webbrowser.open('https://www.youtube.com/watch?v=xXhEz3hqlQE', new=2)