import multiprocessing
import time

# 1
def wait():
    time.sleep(0.5)
    print("Done waiting")

process = multiprocessing.Process(target=wait)

# Add code below
process.start()
process.join()
print("Finished")

# 2 - dos process a la vez
# Add code below
start = time.time()

p1 = multiprocessing.Process(target=wait)
p2 = multiprocessing.Process(target=wait)

p1.start()
p2.start()

p1.join()
p2.join()

end = time.time()

elapsed = end - start


# 3 - Multiples procesos abiertos a la vez (forma mas eficiente)
# Add code below
start = time.time()

processes = [multiprocessing.Process(target=wait) for _ in range(6)]

for process in processes:
    process.start()

for process in processes:
    process.join()

end = time.time()

elapsed = end - start

# 4 - 
def sum3(x, y, z):
    print(x + y + z)

def list_average(values):
    print(sum(values) / len(values))

# Add code below
sum3_process = multiprocessing.Process(target=sum3, args=[3, 2, 5])
list_average_process = multiprocessing.Process(target=list_average, args=[[1, 2, 3, 4, 5]])

sum3_process.start()
list_average_process.start()

sum3_process.join()
list_average_process.join()


# 5 - shared value: es como un global para los procesos
def sum3(x, y, z):
    print(x + y + z)
def sum3(x, y, z, shared_value):
    shared_value.value = x + y + z

float_value = multiprocessing.Value("f")
process = multiprocessing.Process(target=sum3, args=[5, 7, 4, float_value])
process.start()
process.join()

print(float_value.value)

# 6 - lock en shared value: para no ir sobreescribiendolo en paralelo entre muchos procesos: Se lockea en la funcion que debe escribirlo (entre lectura y escritura)
def sum_values(first, last, shared_value):
    for i in range(first, last):
        with shared_value.get_lock():
            shared_value.value += i

def measure_runtime(function_to_measure):
    N = 10000
    shared_value = multiprocessing.Value("i")
    process1 = multiprocessing.Process(target=function_to_measure, args=(1, N // 2, shared_value))
    process2 = multiprocessing.Process(target=function_to_measure, args=(N // 2, N, shared_value))
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    return end - start
    
# Add code below
def sum_values_improved(first, last, shared_value):
    value_sum = 0
    for i in range(first, last):
        value_sum += i
    with shared_value.get_lock():
        shared_value.value += value_sum

time_sum_values = measure_runtime(sum_values)
time_sum_values_improved = measure_runtime(sum_values_improved)

print(time_sum_values)
print(time_sum_values_improved)