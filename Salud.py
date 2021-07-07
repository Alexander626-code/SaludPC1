# este programa chequea el estado de salud de tu computadora.
import shutil
import psutil
def verif_disk_usado(disk):
    du = shutil.disk_usage(disk)
    libre = du.free / du.total * 100
    return libre > 20
def wverif_cpu_usada():
    usado = psutil.cpu_percent(1)
    return usado < 75
if not verif_disk_usado("/") or not wverif_cpu_usada():
    print("ERROR: ")
else:
    print("Tu equipo parece estar en buenas condiciones.")
