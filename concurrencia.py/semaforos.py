import threading
import time

# Definir un semáforo con un contador inicial
semaphore = threading.Semaphore(2)  # Permitir hasta 2 hilos a la vez

def tarea(nombre):
 print(f"{nombre} esperando para entrar al área crítica")
 semaphore.acquire()
 print(f"{nombre} entró al área crítica")
 time.sleep(2)  # Simular una operación crítica
 print(f"{nombre} salió del área crítica")
semaphore.release()


# Crear varios hilos que intentan acceder al área crítica
thread1 = threading.Thread(target=tarea, args=("Hilo 1",))
thread2 = threading.Thread(target=tarea, args=("Hilo 2",))
thread3 = threading.Thread(target=tarea, args=("Hilo 3",))

# Iniciar los hilos
thread1.start()
thread2.start()
thread3.start()

# Esperar a que todos los hilos terminen
thread1.join()
thread2.join()
thread3.join()

print("Todos los hilos han terminado.")
