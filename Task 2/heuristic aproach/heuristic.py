import random
from collections import defaultdict

random.seed(42)

students = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

# Friendship
friends = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G"],
    "E": ["B", "H", "I"],
    "F": ["C", "J"],
    "G": ["D", "K"],
    "H": ["E"],
    "I": ["E", "L"],
    "J": ["F", "M"],
    "K": ["G", "N"],
    "L": ["I"],
    "M": ["J"],
    "N": ["K"],
    "O": ["P"],
    "P": ["O"]
}


city = {
    "A": "Kathmandu", "B": "Pokhara",   "C": "Kathmandu", "D": "Kathmandu",
    "E": "Pokhara",   "F": "Biratnagar", "G": "Lalitpur",  "H": "Pokhara",
    "I": "Chitwan",   "J": "Biratnagar", "K": "Lalitpur",  "L": "Chitwan",
    "M": "Biratnagar","N": "Butwal",     "O": "Dhangadhi","P": "Dhangadhi"
}

def is_valid(seating):
    for i in range(len(seating) - 1):
        s1, s2 = seating[i], seating[i + 1]
        # Check friendship (symmetric)
        if s2 in friends.get(s1, []) or s1 in friends.get(s2, []):
            return False
        # Check city
        if city[s1] == city[s2]:
            return False
    return True

# Heuristic: sort by number of friends (degree)
def constraint_count(student):
    return len(friends.get(student, []))

# Sort students by constraint descending
students_sorted = sorted(students, key=constraint_count, reverse=True)

# Group by constraint level and shuffle within groups for variety
groups = defaultdict(list)
for s in students_sorted:
    groups[constraint_count(s)].append(s)

students_sorted = []
for deg in sorted(groups, reverse=True):
    random.shuffle(groups[deg])
    students_sorted.extend(groups[deg])

print("Order of placement (most constrained first):")
print(" →", " ".join(students_sorted))
print()

# Greedy placement: try positions preferring center insertions first
seating = []
for student in students_sorted:
    placed = False
    positions = list(range(len(seating) + 1))
    if seating:
        # Sort to prefer positions farther from ends (center first)
        positions.sort(key=lambda i: min(i, len(seating) - i), reverse=True)
    for i in positions:
        temp = seating[:i] + [student] + seating[i:]
        if is_valid(temp):
            seating = temp
            placed = True
            print(f"✓ Placed {student:>2}  →  {' → '.join(seating)}")
            break
    if not placed:
        print(f"✗ Could not place {student}")
        print("Current partial arrangement:", " → ".join(seating))
        break

print("\n" + "═"*65)
if len(seating) == len(students):
    print("SUCCESS! Final valid seating arrangement found:")
    print(" → " + " → ".join(seating))
else:
    print("Heuristic failed to find a complete valid arrangement.")
    print("Partial result:", " → ".join(seating))