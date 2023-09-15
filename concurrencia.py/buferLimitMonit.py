import threading
import time

# Tamaño máximo del buffer
BUFFER_SIZE = 5

class BoundedBuffer:
    def __init__(self):
        self.buffer = []
        self.lock = threading.Condition()  # Creamos un monitor con un condicional

    def produce(self, item):
        with self.lock:
            while len(self.buffer) >= BUFFER_SIZE:
                print("Buffer lleno. Esperando para producir...")
                self.lock.wait()
            self.buffer.append(item)
            print(f"Producido: {item}")
            self.lock.notifyAll()

    def consume(self):
        with self.lock:
            while len(self.buffer) == 0:
                print("Buffer vacío. Esperando para consumir...")
                self.lock.wait()
            item = self.buffer.pop(0)
            print(f"Consumido: {item}")
            self.lock.notifyAll()

# Función del productor
def producer(buffer):
    for i in range(1, 11):
        item = f"item {i}"
        buffer.produce(item)
        time.sleep(1)  # Simula la producción de un elemento

# Función del consumidor
def consumer(buffer):
    for _ in range(1, 11):
        buffer.consume()
        time.sleep(2)  # Simula el consumo de un elemento

# Crear el buffer compartido
buffer = BoundedBuffer()

# Crear las threads del productor y el consumidor
producer_thread = threading.Thread(target=producer, args=(buffer,))
consumer_thread = threading.Thread(target=consumer, args=(buffer,))

# Iniciar las threads
producer_thread.start()
consumer_thread.start()

# Esperar a que ambas threads terminen
producer_thread.join()
consumer_thread.join()

print("Programa terminado")
