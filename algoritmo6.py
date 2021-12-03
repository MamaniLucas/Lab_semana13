import datetime
def mostrarFecha():
    fecha = datetime.datetime.now()
    print(fecha.strftime("%H:%M:%S"))
    print(fecha.strftime("%Y:%m:%D"))
mostrarFecha()






