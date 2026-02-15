# Task 1: Encoding and Encryption

This task covers various encoding techniques and demonstrates why **encoding is NOT security**.

## Overview

Task 1 explores different types of encoding used in computer systems and highlights the critical difference between encoding and encryption. Through practical simulations, this task covers why Base64, URL encoding, and similar techniques should never be used as security mechanisms.

## Subtopics

### 1. Base64 Encoding
- **Location**: `For Base64/`
- **File**: `base64.py`
- **Description**: 
    - Interactive Tkinter application for real-time Base64 encode and decode
    - Demonstrates how Base64 is used to convert binary data into text-safe format
    - Real-world use: Email attachments (SMTP), Basic Authentication headers, JWT tokens

### 2. URL Encoding
- **Location**: `For URL/`
- **File**: `url_encoding_simulation.html`
- **Description**: 
    -HTML/JavaScript simulation showing proper vs improper URL encoding
    - Demonstrates how missing encoding leads to injection attacks (e.g., reflected XSS)
    - Real-world use: Query parameters in REST APIs and OAuth redirect URIs

### 3. OAuth/JWT Authentication
- **Location**: `for Oauth/`
- **Files**: `login.html`, `shop.html`, `attacker.html`
- **Description**: 
    -Multi-page simulation (login → shop → attacker)
    - Shows how URL encoding and Base64 are used in OAuth flows
    - Highlights risks when encoding + validation are not handled correctly 

### 4. HTTP vs HTTPS
- **Location**: `HTTP vs HTTPS simulation/`
- **Files**: `index.html`, `server.py`
- **Description**: 
    - Flask web application that compares data transmission over HTTP vs HTTPS
    - Includes insecure file upload and interception of encoded payloads (Base64, URL-encoded data)
    - Demonstrates why encoding alone is not enough — TLS/HTTPS is required for confidentiality

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Encoding** | Converting data from one format to another (e.g., Base64) - reversible, no security |
| **Encryption** | Converting data using a secret key - requires key to decrypt |
| **Hashing** | One-way function producing fixed-size output - cannot be reversed |

## Learnig outcomes

1. **Base64 is NOT security**: Encoding (Base64, URL) makes data **transmittable**, but does **not** make it **secure**
2. **Always validate and encode user input**: Prevents XSS and injection attacks
3. **Use HTTPS in production**: LS/HTTPS is the actual security layer that works together with encoding
4. **JWT should use proper encryption**: In production, use proper encryption or signed tokens

---

## Navigation

- [Main README](../README.md)
- [Task 2: Brute Force vs Heuristic](../Task%202/README.md)
- [Task 3: Database](../Task%203/README.md)
