import math

print("Number of students vs possible seating arrangements:\n")

students = 20

for n in range(1, students):
    arrangements = math.factorial(n)
    print(f"{n} students → {arrangements} possible arrangements")
