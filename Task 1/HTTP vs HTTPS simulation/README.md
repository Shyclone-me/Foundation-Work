# HTTP vs HTTPS Simulation

## Overview

This is a simulation demonstrating the difference between HTTP (HyperText Transfer Protocol) and HTTPS (HTTP Secure). It shows how data is transmitted in both protocols and why HTTPS is essential for secure communication.

## What is HTTP?

HTTP (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web. However, it has a critical flaw:

- **Data is sent in plain text**
- Anyone on the network can intercept and read the data
- No encryption or security mechanisms
- Vulnerable to man-in-the-middle attacks

## What is HTTPS?

HTTPS (HTTP Secure) adds a layer of security using:

- **SSL/TLS Encryption**: Data is encrypted before transmission
- **Certificate Authentication**: Verifies the server's identity
- **Data Integrity**: Ensures data isn't tampered with during transmission

## The Simulation

This simulation includes:

1. **index.html**: A web page with an image upload form
2. **server.py**: A Flask server that can run in both HTTP and HTTPS modes

### How It Works

1. User selects an image file
2. Image is converted to Base64
3. Data is sent to the server via POST request
4. Server saves the image

When running over HTTP, the data is visible to anyone intercepting the network traffic. When running over HTTPS, the data is encrypted.

## Running the Simulation

### Start the Server

```
bash
cd "Task 1/HTTP vs HTTPS simulation"
python server.py
```


### Access the Application
Choose the server, then it will start the server.

- **HTTP**: http://127.0.0.1:5000
it looks like 
![HTTP GUI Main Interface](/Task%201/Screenshots/Http.png)

- **HTTPS**: https://127.0.0.1:5000
it looks like 
![URL GUI Main Interface](/Task%201/Screenshots/HTTPS.png)
Note: The server uses an ad-hoc SSL certificate for demonstration. Your browser may show a security warning - this is expected for self-signed certificates.

### Test the Difference

1. Open the page in HTTP mode
2. Upload an image - use a network sniffer to see the plain text data
3. Switch to HTTPS mode
4. Upload an image again - observe that the data is encrypted

### Client (index.html)
- Uses JavaScript FileReader to convert image to Base64
- Sends data as JSON to the server

## Key Differences

| Feature | HTTP | HTTPS |
|---------|------|-------|
| Security | None | SSL/TLS Encryption |
| Port | 80 | 443 |
| Data | Plain text | Encrypted |
| Certificate | Not required | Required |
| Attack Risk | High | Low |

## Key Learnings

1. **Always use HTTPS for sensitive data**: Passwords, credit cards, personal information
2. **Encryption is essential**: Without it, data can be intercepted
3. **Certificates verify identity**: Prevents impersonation attacks
4. **Look for the padlock**: Always check for HTTPS in production websites

---

## Navigation

- [Task 1 README](../README.md)
- [Base64 Encoding](../For%20Base64/README.md)
- [URL Encoding](../For%20URL/README.md)
- [OAuth Simulation](../for%20Oauth/README.md)
