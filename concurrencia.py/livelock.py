import threading

# Dos recursos compartidos
recurso_A = threading.Lock()
recurso_B = threading.Lock()

def hilo_1():
    print("Hilo 1: Intentando adquirir recurso A")
    recurso_A.acquire()
    print("Hilo 1: Adquirió recurso A, intentando adquirir recurso B")
    recurso_B.acquire()
    print("Hilo 1: Adquirió recurso B")

def hilo_2():
    print("Hilo 2: Intentando adquirir recurso B")
    recurso_B.acquire()
    print("Hilo 2: Adquirió recurso B, intentando adquirir recurso A")
    recurso_A.acquire()
    print("Hilo 2: Adquirió recurso A")

# Crear dos hilos
thread1 = threading.Thread(target=hilo_1)
thread2 = threading.Thread(target=hilo_2)

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que ambos hilos terminen
thread1.join()
thread2.join()

print("Ambos hilos han terminado.")
