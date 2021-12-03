import datetime
def mostrarfecha():
    fecha = datetime.datetime.now()
    print("La hora actual es: ")
    print(fecha.strftime("%H: %M: %S"))
    print("La fecha actual es: ")
    print(fecha.strftime("%Y-%m-%d"))

mostrarfecha()