# OAuth/JWT Authentication Simulation

## Overview

This is a web-based simulation demonstrating OAuth 2.0 and JWT (JSON Web Token) authentication. It shows how authentication works in modern web applications and highlights the critical difference between **encoding** and **encryption**.

## What is OAuth?

OAuth 2.0 is an authorization framework that enables applications to obtain limited access to user accounts on HTTP services. It delegates user authentication to the service hosting the user account.

## What is JWT?

JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties. A JWT consists of three parts:
1. **Header** - Specifies the token type and signing algorithm
2. **Payload** - Contains the claims (user data)
3. **Signature** - Verifies the token wasn't tampered with

## Security Warning

This simulation demonstrates a common security misconception: **JWT tokens are Base64 encoded, NOT encrypted!**

In this simulation:
- The payload is simply Base64 encoded (anyone can decode it)
- The "signature" is just a placeholder
- This is NOT secure for production use

In production, JWT should be:
- Properly signed using secure algorithms (HS256, RS256)
- Or encrypted using JWE (JSON Web Encryption)
- Transmitted over HTTPS only

## Files

| File | Description |
|------|-------------|
| `login.html` | Login page that creates a fake JWT token |
| `shop.html` | Protected page that displays user info from JWT |
| `attacker.html` | Demonstrates how an attacker can read the token |

## How It Works

1. User enters email and password
2. System creates a JWT with:
   - Header: `{"alg": "HS256", "typ": "JWT"}`
   - Payload: `{"email": "user@email.com", "role": "customer"}`
   - Signature: Fake signature
3. Token is Base64 encoded and stored in localStorage
4. The token is sent with each request to authenticate the user

## Running the Simulation

Simply open the HTML files in a web browser. For best results, serve them from a local web server:

```
bash
# Using Python's built-in server
cd "Task 1/for Oauth"
python -m http.server 8000
# Then open http://localhost:8000/login.html
```

## Demonstration Steps

1. Open `login.html` in a browser
2. Enter any email and password
3. Click Login - observe the JWT created in localStorage
4. You'll be redirected to `shop.html` showing user info
5. Open browser DevTools (F12) to see the token in localStorage
6. Copy the payload portion and decode it in Base64 decoder
7. Notice how easy it is to read the "secret" data!

## Key Learnings

1. **Encoding ≠ Encryption**: Base64 encoding is not security
2. **JWT is not secure by default**: Always use HTTPS and proper signing
3. **Never store sensitive data in JWT payload**: It's just encoded, not encrypted
4. **Use proper auth flows**: OAuth 2.0 with proper implementation

---

## What the Program Looks Like

![Oauth GUI Main Interface](/Task%201/Screenshots/Oauthfirst.png)

![Oauth GUI Second Interface](/Task%201/Screenshots/oauthsecond.png)



## Navigation

- [Task 1 README](../README.md)
- [Base64 Encoding](../For%20Base64/README.md)
- [URL Encoding](../For%20URL/README.md)
- [HTTP vs HTTPS](../HTTP%20vs%20HTTPS%20simulation/README.md)
