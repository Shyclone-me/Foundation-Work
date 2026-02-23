# Task 3: Database Normalization and SQL Operations

## Overview

This task focuses on **Database Normalization**, a critical concept in relational database design. It demonstrates how to transform unnormalized data into progressively normalized forms (1NF, 2NF, 3NF) to reduce redundancy and improve data integrity.

The task includes:
- Docker setup for MySQL database
- SQL scripts for 1NF, 2NF, and 3NF implementations
- CRUD operations
- JOIN operations
- Database anomalies demonstration

---

## Prerequisites

Before running this task, ensure you have:
- **Docker Desktop** installed and running
- **MySQL Client** or any database GUI tool (MySQL Workbench, DBeaver, etc.)
- Basic understanding of SQL and relational databases

---

## Project Structure

```
Task 3/
├── README.md
├── Docker/
│   └── docker-compose.yml          # MySQL container configuration
└── sql/
    ├── 1nf.sql                     # First Normal Form schema
    ├── 2nf.sql                     # Second Normal Form schema
    ├── 3nf.sql                     # Third Normal Form schema
    ├── sql_operation.sql           # CRUD operations
    ├── joinoperation.sql           # JOIN queries
    └── anomalies_query.sql         # Anomaly demonstrations
```

---

## Getting Started

### Setting up MySQL with Docker

1. Navigate to the Docker directory:
   
```
bash
   cd Task 3/Docker
   
```

2. Start the MySQL container:
   
```
bash
   docker-compose up -d
   
```

3. Verify the container is running:
   
```
bash
   docker ps
   
```

4. Connect to MySQL:
   - **Host:** localhost
   - **Port:** 3301
   - **User:** root
   - **Password:** root
   - **Database:** college_db

### Running SQL Scripts

You can run SQL scripts using:
- **Command Line:**
  
```
bash
  mysql -h localhost -P 3301 -u root -proot college_db < filename.sql
  
```
- **MySQL Workbench:** Connect and execute the scripts
- **Docker exec:**
  
```
bash
  docker exec -it Students_database mysql -u root -proot college_db
  
```

---

## Normalization Forms

### First Normal Form (1NF)

**File:** `sql/1nf.sql`

**Requirements:**
- Each column contains atomic (indivisible) values
- Each column contains values of a single type
- Each row is unique
- Each column has a unique name

**Table Structure:**
```
sql
CREATE TABLE club_members_1nf (
    student_id INT NOT NULL,
    student_name VARCHAR(100),
    email VARCHAR(100),
    club_name VARCHAR(100) NOT NULL,
    club_room VARCHAR(50),
    club_mentor VARCHAR(100),
    join_date DATE,
    PRIMARY KEY (student_id, club_name)
);
```

**Issues with 1NF:**
- Data redundancy (student info repeated for each club membership)
- Update anomalies (changing a student's email requires multiple updates)
- Insertion anomalies (cannot add a new club without a student)
- Deletion anomalies (removing a student may lose club information)

---

### Second Normal Form (2NF)

**File:** `sql/2nf.sql`

**Requirements:**
- Must be in 1NF
- No partial dependencies (non-key attributes must depend on the entire primary key)

**Table Structure:**

1. **Students Table:**
```
sql
CREATE TABLE student_2nf (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100)
);
```

2. **Clubs Table:**
```
sql
CREATE TABLE club_2nf (
    club_name VARCHAR(100) PRIMARY KEY,
    club_room VARCHAR(50),
    club_mentor VARCHAR(100)
);
```

3. **Membership Table (Junction Table):**
```
sql
CREATE TABLE membership_2nf (
    student_id INT,
    club_name VARCHAR(100),
    join_date DATE,
    PRIMARY KEY (student_id, club_name),
    FOREIGN KEY (student_id) REFERENCES student_2nf(student_id),
    FOREIGN KEY (club_name) REFERENCES club_2nf(club_name)
);
```

**Improvements:**
- Eliminated redundant student data
- Eliminated redundant club data
- Each entity is now properly separated

---

### Third Normal Form (3NF)

**File:** `sql/3nf.sql`

**Requirements:**
- Must be in 2NF
- No transitive dependencies (non-key attributes should not depend on other non-key attributes)

**Table Structure:**

1. **Students Table:**
```sql
CREATE TABLE student_3nf (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100)
);
```

2. **Clubs Table (with surrogate key):**
```
sql
CREATE TABLE club_3nf (
    club_id INT AUTO_INCREMENT PRIMARY KEY,
    club_name VARCHAR(100) UNIQUE,
    club_room VARCHAR(50),
    club_mentor VARCHAR(100)
);
```

3. **Membership Table:**
```
sql
CREATE TABLE membership_3nf (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    club_id INT,
    join_date DATE,
    FOREIGN KEY (student_id) REFERENCES student_3nf(student_id),
    FOREIGN KEY (club_id) REFERENCES club_3nf(club_id)
);
```

**Benefits:**
- Complete elimination of data redundancy
- Easier maintenance and updates
- Better data integrity
- Scalable database design

---

## SQL Operations

**File:** `sql/sql_operation.sql`

This file demonstrates basic CRUD (Create, Read, Update, Delete) operations:

### INSERT Operations
```
sql
-- Insert new students
INSERT INTO student_3nf (student_name, email)
VALUES ('Khushi', 'khushi@email.com'), ('Peina', 'peina@email.com');

-- Insert new club
INSERT INTO club_3nf (club_name, club_room, club_mentor)
VALUES ('Robotics Club', 'Lab 204', 'Mr. Shyam');
```

### SELECT Operations
```
sql
-- Display all students
SELECT * FROM student_3nf;

-- Display all clubs
SELECT * FROM club_3nf;
```

### UPDATE Operations
```
sql
-- Update student's email
UPDATE student_3nf
SET email = 'khushi.updated@email.com'
WHERE student_name = 'Khushi';
```

### DELETE Operations
```
sql
-- Delete a student
DELETE FROM student_3nf
WHERE student_id = 9;
```

---

## JOIN Operations

**File:** `sql/joinoperation.sql`

Demonstrates how to combine data from multiple tables:

```
sql
SELECT 
    s.student_name AS "Student Name",
    c.club_name AS "Club Name",
    m.join_date AS "Join Date"
FROM membership_3nf m
JOIN student_3nf s ON m.student_id = s.student_id
JOIN club_3nf c ON m.club_id = c.club_id;
```

**Expected Output:**
| Student Name | Club Name   | Join Date  |
|--------------|-------------|------------|
| Asha         | Music Club  | 2024-01-10|
| Asha         | Sports Club | 2024-01-15|
| Bikash       | Drama Club  | 2024-01-25|
| ...          | ...         | ...        |

---

## Database Anomalies

**File:** `sql/anomalies_query.sql`

### 1. Insertion Anomaly
**Problem:** Cannot add a new club without assigning at least one student.
```
sql
INSERT INTO club_members_unf
(student_id, student_name, email, club_name, club_mentor, join_date)
VALUES
(NULL, NULL, NULL, 'Robotics Club', 'Mr. Kumar', NULL);
```

### 2. Update Anomaly
**Problem:** Updating a club's mentor requires updating multiple rows.
```
sql
UPDATE club_members
SET club_mentor = 'Mr. Sharma'
WHERE club_name = 'Music Club'
LIMIT 1;
```

### 3. Deletion Anomaly
**Problem:** Deleting a club membership may accidentally delete important data.
```
sql
DELETE FROM club_members
WHERE club_name = 'Sports Club';
```

**Solution:** Normalization eliminates these anomalies by separating concerns and reducing redundancy.

---

## Key Learnings

1. **Data Redundancy:** Normalization reduces duplicate data storage
2. **Data Integrity:** Proper normalization ensures accurate and consistent data
3. **Maintainability:** Normalized databases are easier to maintain and update
4. **Scalability:** Well-normalized databases scale better
5. **Performance:** While normalization reduces redundancy, denormalization may be used for performance optimization in specific scenarios

---

## Additional Notes

- The docker-compose.yml creates a persistent volume (`mysql_data`) to preserve data
- To stop the container: `docker-compose down`
- To remove all data: `docker-compose down -v`

