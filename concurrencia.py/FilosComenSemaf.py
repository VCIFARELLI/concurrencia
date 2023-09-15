import threading
import time
import random

NUM_FILOSOFOS = 5

filosofo_semaforos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]
tenedores_semaforos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

def filosofo(filosofo_id):
    while True:
        print(f"Filósofo {filosofo_id} está pensando.")
        time.sleep(random.uniform(1, 5))  # Simula el tiempo de pensamiento
        
        print(f"Filósofo {filosofo_id} quiere comer.")
        tomar_tenedores(filosofo_id)
        
        print(f"Filósofo {filosofo_id} está comiendo.")
        time.sleep(random.uniform(1, 5))  # Simula el tiempo de comer
        
        dejar_tenedores(filosofo_id)

def tomar_tenedores(filosofo_id):
    tenedor_izq = filosofo_id
    tenedor_der = (filosofo_id + 1) % NUM_FILOSOFOS
    
    filosofo_semaforos[filosofo_id].acquire()
    tenedores_semaforos[tenedor_izq].acquire()
    tenedores_semaforos[tenedor_der].acquire()
    filosofo_semaforos[filosofo_id].release()

def dejar_tenedores(filosofo_id):
    tenedor_izq = filosofo_id
    tenedor_der = (filosofo_id + 1) % NUM_FILOSOFOS
    
    tenedores_semaforos[tenedor_izq].release()
    tenedores_semaforos[tenedor_der].release()

filosofos = [threading.Thread(target=filosofo, args=(i,)) for i in range(NUM_FILOSOFOS)]

for f in filosofos:
    f.start()

for f in filosofos:
    f.join()

