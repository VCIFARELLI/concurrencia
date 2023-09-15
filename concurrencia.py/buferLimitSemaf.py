import threading
import time

# Tamaño máximo del buffer
BUFFER_SIZE = 5

# Buffer compartido
buffer = []
# Semaforo para controlar el acceso al buffer
buffer_semaphore = threading.Semaphore(1)
# Semaforo para controlar el número de elementos en el buffer
items_semaphore = threading.Semaphore(0)

# Función del productor
def producer():
    for i in range(1, 11):
        item = f"item {i}"
        print(f"Produciendo {item}")
        time.sleep(1)  # Simula la producción de un elemento
        buffer_semaphore.acquire()
        if len(buffer) < BUFFER_SIZE:
            buffer.append(item)
            items_semaphore.release()
        else:
            print("Buffer lleno, esperando para poner un elemento")
        buffer_semaphore.release()

# Función del consumidor
def consumer():
    for _ in range(1, 11):
        items_semaphore.acquire()
        buffer_semaphore.acquire()
        item = buffer.pop(0)
        print(f"Consumiendo {item}")
        buffer_semaphore.release()
        time.sleep(2)  # Simula el consumo de un elemento

# Crear las threads del productor y el consumidor
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Iniciar las threads
producer_thread.start()
consumer_thread.start()

# Esperar a que ambas threads terminen
producer_thread.join()
consumer_thread.join()

print("Programa terminado")

#(BufferMonitor) que contiene un buffer,( mutex) para garantizar,
#(insert)para agregar elementos al buffer,(remove) para eliminar elementos