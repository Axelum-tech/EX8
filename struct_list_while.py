temps = [10.0, 9.0, 8.0, 0.0, -5.0,-10.0, 0.0]
days  = ["MO", "TU", "WD", "TH", "FR", "SA", "SU"]
i=0


while i<len(temps):
    if temps[i]<=0:
        sign="*"
    else:
        sign=" "
    print(sign, days[i], temps[i])
    i+=1
   