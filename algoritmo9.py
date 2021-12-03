from datetime import date, timedelta
primera_fecha=date(2021,12,2)
segunda_fecha=date(2021,12,22)
cont=0
f = primera_fecha

while f < segunda_fecha:
   if f.weekday()==6:
            cont+=1
   f = f + timedelta(days=1)
print("La diferencia es de",cont, "domingos")











#import datetime 
#def formato(primera_fecha, segunda_fecha, formato, contador, timedelta):
   # while True:
        #primera_fecha= datetime.strptime(primera_fecha)
        #segunda_fecha = datetime.strptime(segunda_fecha)

        #if primera_fecha > segunda_fecha:
           #print('La primera fecha debe ser menor o igual que la segunda') 
    
        #while primera_fecha <= segunda_fecha:
            #if datetime.weekday(primera_fecha) == 6:
               #contador +=1
               #suma_domingos = primera_fecha.strftime(formato)
               #print(contador, suma_domingos, 'dia domingo')
            #primera_fecha = primera_fecha + timedelta(days = 1)
