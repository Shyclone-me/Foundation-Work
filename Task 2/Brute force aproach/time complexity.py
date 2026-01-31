import math

check_time = 0.000001  # assuming 1 microsecond per arrangement

print("Estimated time to check all arrangements:\n")

last_student = 20
for n in range(5, last_student):
    total_time = math.factorial(n) * check_time
    print(f"{n} students → {total_time:.2f} seconds")
