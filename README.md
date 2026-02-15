# Foundation Work - Coursework Project

A comprehensive coursework project covering three major topics: **Encoding & Encryption**, **P vs NP Problems (Brute Force vs Heuristic)**, and **Database Design**.

---

## Project Structure

```
Foundation-Work/
├── README.md                    # Main README
├── Task 1/
│   ├── README.md               # Task 1 Overview
│   ├── For Base64/
│   │   ├── base64.py          # Base64 encoding/decoding GUI
│   │   └── README.md
│   ├── For URL/
│   │   ├── url_encoding_simulation.html  # XSS vulnerability demo
│   │   └── README.md
│   ├── for Oauth/
│   │   ├── login.html         
│   │   ├── shop.html          
│   │   ├── attacker.html      
│   │   └── README.md
│   └── HTTP vs HTTPS simulation/
│       ├── index.html
│       ├── server.py           # Flask server
│       ├── uploads/
│       └── README.md
├── Task 2/
│   ├── README.md               # Task 2 Overview
│   ├── Brute force aproach/
│   │   ├── Brute FOrce.py
│   │   ├── bruteforce_in_findingword.py
│   │   ├── factorial growth.py
│   │   ├── time complexity.py
│   │   └── README.md
│   └── heuristic aproach/
│       ├── heuristic.py
│       └── README.md
└── Task 3/
    ├── README.md               # Task 3 Overview
    ├── Docker/
    │   └── docker-compose.yml  # MySQL container
    └── sql/
        ├── 1nf.sql            # First Normal Form
        ├── 2nf.sql            # Second Normal Form
        ├── 3nf.sql            # Third Normal Form
        ├── anomalies_query.sql
        ├── joinoperation.sql
        └── sql_operation.sql
```

---

## Task 1: Encoding and Encryption

### what is Task 1 About "

Task 1 covers various encoding techniques and demonstrates why **encoding is NOT security**. It explores the critical difference between encoding, encryption, and hashing through practical simulations.

### Task includes:

1. **Base64 Encoding** (`Task 1/For Base64/base64.py`)
   - Created a GUI application demonstrating Base64 encoding and decoding
   - Shows that Base64 is NOT encryption - anyone can decode it without a key

2. **URL Encoding** (`Task 1/For URL/url_encoding_simulation.html`)
   - Built a web simulation showing XSS vulnerability
   - Demonstrates how URL encoding prevents injection attacks by encoding special characters

3. **OAuth/JWT Authentication** (`Task 1/for Oauth/`)
   - Created a simple JWT-based authentication simulation (login.html, shop.html, attacker.html)
   - Demonstrates that JWT uses Base64 encoding (NOT encryption) - a common security misconception

4. **HTTP vs HTTPS** (`Task 1/HTTP vs HTTPS simulation/`)
   - Built a Flask server demonstrating secure vs insecure communication
   - Shows that HTTPS encrypts data in transit, while HTTP sends data in plain text

### Key Learnings
- Base64 is NOT encryption - it's designed for data transmission, not protection
- URL Encoding prevents XSS attacks by encoding special characters
- OAuth/JWT uses Base64 encoding (not encryption) for tokens
- HTTPS provides encryption for data in transit

---

## Task 2: P vs NP Problems - Brute Force vs Heuristic

### What is Task 2 About?

Task 2 explores and computational complexity by comparing brute force and heuristic approaches to problem-solving. It demonstrates the difference between P problems (solvable in polynomial time) and NP problems (solutions can be verified in polynomial time but finding them may take exponential time).

### What We Have Done

1. **Brute Force Approach** (`Task 2/Brute force aproach/`)
   - `Brute FOrce.py` - Simple linear search example
   - `bruteforce_in_findingword.py` - Finding a word in a list
   - `factorial growth.py` - Demonstrates factorial time complexity O(n!)
   - `time complexity.py` - Shows estimated time to solve factorial problems

2. **Heuristic Approach** (`Task 2/heuristic aproach/heuristic.py`)
   - Implemented seating arrangement problem using greedy heuristic with backtracking
   - Constraints: Friends cannot sit next to each other, students from same city cannot sit next to each other
   - Uses heuristic: Sort by most constrained first (students with most friends)
   - Demonstrates how heuristics can find good solutions without exploring all possibilities

### Key Concepts
- **P Problems**: Can be solved in polynomial time (e.g., sorting, searching)
- **NP Problems**: Solutions can be verified in polynomial time (e.g., traveling salesman, seating arrangements)
- **Brute Force**: Tries all possibilities - guaranteed to find solution but may take exponentially long
- **Heuristic**: Uses approximation rules to find good solutions quickly - doesn't guarantee optimal solution

---

## Task 3: Database

### What is Task 3 About?
 
   - `3nf.sql` - Third Normal Form (using surrogate keys for proper relationships)

2. **Database Anomalies** (`Task 3/sql/anomalies_query.sql`)
   - Demonstrates Insertion, Update, and Deletion anomalies

3. **SQL Operations** (`Task 3/sql/sql_operation.sql`)
   - CRUD operations: INSERT, SELECT, UPDATE, DELETE

4. **Join Operations** (`Task 3/sql/joinoperation.sql`)
   - Demonstrates JOIN queries across multiple tables

5. **Docker Setup** (`Task 3/Docker/docker-compose.yml`)
   - MySQL 8.0 container with persistent storage

### Database Schema (Student Club Membership System)
- **Students**: student_id, student_name, email
- **Clubs**: club_id, club_name, club_room, club_mentor
- **Membership**: membership_id, student_id, club_id, join_date

### Key Concepts
- **Normalization**: Organizing data to reduce redundancy
- **Primary Key**: Unique identifier for each record
- **Foreign Key**: Reference to another table's primary key
- **Surrogate Key**: Artificial key (e.g., AUTO_INCREMENT)
- **Join**: Combining data from multiple tables
- **CRUD**: Create, Read, Update, Delete operations

---

## 🛠️ Technologies & Tools

- **Languages**: Python 3, HTML, CSS, JavaScript, SQL
- **Frameworks**: Flask (for web simulations)
- **GUI**: Tkinter
- **Database**: MySQL (via Docker)
- **Other**: Docker Compose, Git

---

## 🚀 How to Explore the Repository

1. Clone the repo:  
   ```bash
   git clone https://github.com/Shyclone-me/Foundation-Work.git
   ```
2. Go into any Task folder
3. Read the detailed README.md inside that folder
4. Follow the Setup & Run instructions provided in each task

--- 

## License

This is a coursework project. All rights reserved.

---

## Author
© Pratyush Rajbhandari
250546
