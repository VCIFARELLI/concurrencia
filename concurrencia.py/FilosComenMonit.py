import threading
import time
import random

NUM_FILOSOFOS = 5

class MonitorFilosofos:
    def __init__(self):
        self.mutex = threading.Condition()
        self.estado = ["PENSANDO"] * NUM_FILOSOFOS

    def tomar_tenedores(self, filosofo):
        with self.mutex:
            self.estado[filosofo] = "HAMBRIENTO"
            self.probar_comer(filosofo)
            while self.estado[filosofo] == "HAMBRIENTO":
                self.mutex.wait()

    def dejar_tenedores(self, filosofo):
        with self.mutex:
            self.estado[filosofo] = "PENSANDO"
            self.probar_comer((filosofo + 1) % NUM_FILOSOFOS)
            self.probar_comer((filosofo - 1) % NUM_FILOSOFOS)
            self.mutex.notify_all()

    def probar_comer(self, filosofo):
        if (
            self.estado[filosofo] == "HAMBRIENTO" and
            self.estado[(filosofo + 1) % NUM_FILOSOFOS] != "COMIENDO" and
            self.estado[(filosofo - 1) % NUM_FILOSOFOS] != "COMIENDO"
        ):
            self.estado[filosofo] = "COMIENDO"
            self.mutex.notify()

def filosofo(filosofo_id, monitor):
    for _ in range(5):  # Los filósofos comerán 5 veces
        print(f"Filósofo {filosofo_id} está pensando.")
        time.sleep(random.uniform(1, 5))  # Simula el tiempo de pensamiento
        
        print(f"Filósofo {filosofo_id} quiere comer.")
        monitor.tomar_tenedores(filosofo_id)
        
        print(f"Filósofo {filosofo_id} está comiendo.")
        time.sleep(random.uniform(1, 5))  # Simula el tiempo de comer
        
        print(f"Filósofo {filosofo_id} ha terminado de comer.")
        monitor.dejar_tenedores(filosofo_id)

monitor = MonitorFilosofos()
filosofos = [threading.Thread(target=filosofo, args=(i, monitor)) for i in range(NUM_FILOSOFOS)]

for f in filosofos:
    f.start()

for f in filosofos:
    f.join()

print("Programa terminado")
