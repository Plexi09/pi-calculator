import threading

sum = 0
estimate = 0
i = 0
epsilon = 0.000000001

def calculate_sum():
    global sum, i
    while True:
        sum += (-1) ** i / (2 * i + 1)
        i += 1

def estimate_pi():
    global sum, estimate
    while True:
        estimate = 4 * sum
        print(f"Aproximation of pi after {i} iterations: {estimate}")

# Create threads
t1 = threading.Thread(target=calculate_sum)
t2 = threading.Thread(target=estimate_pi)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()