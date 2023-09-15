import threading

# Recurso compartido (en este caso, una variable)
recurso = 0

# Semáforos
mutex = threading.Semaphore(1)  # Mutex para garantizar acceso exclusivo al recurso
lectores = threading.Semaphore(1)  # Semáforo para controlar el número de lectores
escritores = threading.Semaphore(1)  # Semáforo para controlar el número de escritores

# Función de escritura
def escritor():
    global recurso
    escritores.acquire()
    recurso += 1
    print(f"Escritor escribió el valor {recurso}")
    escritores.release()

# Función de lectura
def lector():
    global recurso
    lectores.acquire()
    mutex.acquire()
    lectores.release()
    
    # Lectura del recurso
    print(f"Lector leyó el valor {recurso}")
    
    mutex.release()

# Crear lectores y escritores
for _ in range(5):
    threading.Thread(target=lector).start()
for _ in range(2):
    threading.Thread(target=escritor).start()
