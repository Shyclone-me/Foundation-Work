# Heuristic Approach

## Overview

This directory contains an example of the heuristic approach to problem-solving. Heuristics use approximation rules to find good solutions quickly without exploring all possible solutions.

## Heuristic

A heuristic is a technique designed for solving a problem more quickly when classic methods are too slow, or for finding an approximate solution when classic methods fail to find any exact solution.

## Key Characteristics

- **Approximation**: Finds good solutions, not necessarily optimal
- **Speed**: Much faster than brute force for large problems
- **Rules of thumb**: Uses problem-specific knowledge
- **No guarantee**: May not find the best solution

## The Seating Arrangement Problem

This example solves a complex seating arrangement problem with multiple constraints.

### Problem Statement

Arrange 16 students (A-P) in a line such that:
1. **Friends cannot sit next to each other**
2. **Students from the same city cannot sit next to each other**

### Data

#### Students and Their Friends
```
python
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
```

#### Students and Their Cities
```
python
city = {
    "A": "Kathmandu", "B": "Pokhara",   "C": "Kathmandu", "D": "Kathmandu",
    "E": "Pokhara",   "F": "Biratnagar", "G": "Lalitpur",  "H": "Pokhara",
    "I": "Chitwan",   "J": "Biratnagar", "K": "Lalitpur",  "L": "Chitwan",
    "M": "Biratnagar","N": "Butwal",     "O": "Dhangadhi","P": "Dhangadhi"
}
```

## The Heuristic Algorithm

### Step 1: Sort by Constraint (Most Constrained First)
Students with the most friends are placed first because they have the most restrictions.

```
python
def constraint_count(student):
    return len(friends.get(student, []))

students_sorted = sorted(students, key=constraint_count, reverse=True)
```

### Step 2: Greedy Placement with Backtracking
Try to place each student in valid positions. If no position works, backtrack.

```
python
for student in students_sorted:
    for i in range(len(seating) + 1):
        temp = seating[:i] + [student] + seating[i:]
        if is_valid(temp):
            seating = temp
            break
```

### Step 3: Prefer Center Positions
Students placed in the center have more neighbors, so we try center positions first.

```
python
positions.sort(key=lambda i: min(i, len(seating) - i), reverse=True)
```

## Running the Example

```
bash
cd "Task 2/heuristic aproach"
python heuristic.py
```

## Sample Output

```
Order of placement (most constrained first):
→ E → I → B → H → A → C → D → F → G → J → K → N → L → M → O → P

✓ Placed E   →  E
✓ Placed I   →  E → I
✓ Placed B   →  E → I → B
...
✓ Placed P   →  J → C → G → A → I → N → P → H → O → M → L → B → K → D → F → E

═════════════════════════════════════════════════════════
SUCCESS! Final valid seating arrangement found:
 → J → C → G → A → I → N → P → H → O → M → L → B → K → D → F → E
```

## Comparison: Brute Force vs Heuristic

| Aspect | Brute Force | Heuristic |
|--------|-------------|-----------|
| Solution Quality | Optimal | Good (may not be optimal) |
| Time Complexity | O(n!) - factorial | Much faster |
| Memory | High | Lower |
| Guarantee | Yes (optimal) | No |

## When to Use Heuristics

Heuristics are ideal when:
- Problem is NP-hard (like seating arrangements)
- Optimal solution isn't required
- Time constraints exist
- Problem size is large
- Approximate solutions are acceptable

## Common Heuristic Techniques

1. **Greedy**: Make the best local choice at each step
2. **Hill Climbing**: Iteratively improve solution
3. **Genetic Algorithms**: Evolution-based optimization
4. **Simulated Annealing**: Random moves to escape local optima
5. **Tabu Search**: Memory-based search

---

## Navigation

- [Task 2 README](../README.md)
- [Brute Force Approach](../Brute%20force%20aproach/README.md)
