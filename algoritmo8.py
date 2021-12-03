from datetime import date

hoy = date(2021, 11, 22)
otra_fecha = date(2021, 12, 22)

delta= otra_fecha - hoy


print(delta)
print(delta.days)