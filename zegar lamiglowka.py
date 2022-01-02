hour=int(input("podaj godzine: "))
minute=int(input("podaj minute: "))
if (hour > 24):
    print("godzina wieksza niz 24!")
elif (hour < 0):
    print("godzina mniejsza niz 0!")
if (minute > 60):
    print("minuta wieksza niz 60!")
elif (minute < 0):
    print("minuta mniejsza niz 0!")
if(hour>12):
    hour=hour-12
minute=minute/5
hour=hour*30
minute=minute*30
print("wskazowka godzinowa tworzy kat ",hour)
print("wskazowka minutowa tworzy kat ",minute)
if(minute>hour):
    odleglosc=minute-hour
elif(hour>minute):
    odleglosc=hour-minute
if(odleglosc>180):
    odleglosc=360-odleglosc
print("odleglosc dwoch wskazowek w stopniach to: ",odleglosc)