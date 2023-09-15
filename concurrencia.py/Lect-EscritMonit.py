import threading
import time

class LectorEscritorMonitor:
    def __init__(self):
        self.mutex = threading.Condition()
        self.lectores = 0
        self.escritores = 0
        self.escritura_en_progreso = False

    def leer(self, lector_id):
        with self.mutex:
            while self.escritores > 0 or self.escritura_en_progreso:
                self.mutex.wait()
            self.lectores += 1

        print(f"Lector {lector_id} está leyendo.")
        time.sleep(1)  # Simula la lectura
        print(f"Lector {lector_id} ha terminado de leer.")

        with self.mutex:
            self.lectores -= 1
            if self.lectores == 0:
                self.mutex.notify()

    def escribir(self, escritor_id):
        with self.mutex:
            while self.lectores > 0 or self.escritura_en_progreso:
                self.mutex.wait()
            self.escritura_en_progreso = True

        print(f"Escritor {escritor_id} está escribiendo.")
        time.sleep(2)  # Simula la escritura
        print(f"Escritor {escritor_id} ha terminado de escribir.")

        with self.mutex:
            self.escritura_en_progreso = False
            self.mutex.notify_all()

def lector(lector_id, monitor):
    for _ in range(3):
        monitor.leer(lector_id)
        time.sleep(1)

def escritor(escritor_id, monitor):
    for _ in range(3):
        monitor.escribir(escritor_id)
        time.sleep(2)

lector_escritor_monitor = LectorEscritorMonitor()

lectores = [threading.Thread(target=lector, args=(i, lector_escritor_monitor)) for i in range(3)]
escritores = [threading.Thread(target=escritor, args=(i, lector_escritor_monitor)) for i in range(2)]

for thread in lectores:
    thread.start()

for thread in escritores:
    thread.start()

for thread in lectores:
    thread.join()

for thread in escritores:
    thread.join()

print("Programa terminado")
