hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
#Sample input:12 17 59
totalmins = mins+dura
addhour = totalmins//60
if totalmins>=60:
    totalmins %= 60
#Expected output: 13:16
print(str(hour+addhour)+":"+str(totalmins))
