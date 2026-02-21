# Brute Force Approach

## Overview

This directory contains examples demonstrating the brute force approach to problem-solving. Brute force is a straightforward method that tries all possible solutions to find the optimal one.

## Brute Force

Brute force is an algorithm design pattern that:
- Tries all possible solutions systematically
- Checks each solution to find the best one
- Guarantees finding the optimal solution (if one exists)
- May be very slow for large problems

## Time Complexity

Brute force algorithms often have exponential time complexity:
- **O(n!)** - Factorial (e.g., seating arrangements)
- **O(2^n)** - Exponential (e.g., subset sum)
- **O(n^k)** - Polynomial (e.g., sorting)

## Files Included

### 1. Brute FOrce.py
A simple linear search example that searches for a name in a list. 

**Example:**
```
python
Name = ["Ram", "Shyam", "Hari", "Sita", "Gita", "Laxman", "Rawan", "Nobita", "Sunio", "Gian", "Sizuka", 
        "degisugi", "Doreamon", "Doreme", "Sourav", "Puyush", "Sahil", "Avantiva"]

Name_to_search = "Doreamon"
```
TO run this 

``` 
bash 
cd "Task 2/Brute force aproach"
python "Brute FOrce.py"
```

### 2. bruteforce_in_findingword.py
Another example of brute force word searching. This program loops until the word is found.

To run this 
```
bash
cd "Task 2/Brute force aproach"
python "bruteforce_in_findingword.py"
```

### 3. factorial growth.py
Demonstrates how factorial growth works with seating arrangements.

To run 
```
bash
cd "Task 2/Brute force aproach"
python "factorial growth.py"
```

**Output:**
```
Number of students vs possible seating arrangements:

1 students → 1 possible arrangements
2 students → 2 possible arrangements
3 students → 6 possible arrangements
4 students → 24 possible arrangements
...
19 students → 121645100408832000 possible arrangements
```

### 4. time complexity.py
Shows estimated time to check all arrangements at 1 microsecond per arrangement.

**Output:**
```
Estimated time to check all arrangements:

5 students → 120.00 seconds
10 students → 3628800.00 seconds (≈ 42 days)
15 students → 1307674368000.00 seconds (≈ 41 years)
```
To Run this program 
```
bash
cd "Task 2/Brute force aproach"
python "time complexity.py"
```

## When to Use Brute Force

Brute force is appropriate when:
- Problem size is small
- Simplicity is more important than efficiency
- You need the optimal solution
- No better algorithm is available

## When NOT to Use Brute Force

Brute force should be avoided when:
- Problem size is large
- Time constraints are tight
- Heuristic solutions are acceptable
- Problem is known to be NP-hard

## Advantages

 Guaranteed to find optimal solution
 Simple to implement and understand
 Works for any problem

## Disadvantages

 Can be extremely slow
 May be impractical for large problems
 Memory intensive for some problems

---

## Navigation

- [Task 2 README](../README.md)
- [Heuristic Approach](../heuristic%20aproach/README.md)
