# URL Encoding Simulation

## Overview

This is a web-based simulation demonstrating URL encoding and its importance in web security. It shows the difference between **unsafe** (vulnerable to XSS) and **safe** (properly encoded) output.

## What is URL Encoding?

URL encoding (also called percent-encoding) converts characters into a format that can be transmitted over the Internet. Special characters are replaced with a `%` followed by two hexadecimal digits.

For example:
- Space → `%20`
- `<` → `%3C`
- `>` → `%3E`
- `"` → `%22`

## Why is URL Encoding Important?

URL encoding is essential for:
1. **Security**: Prevents XSS (Cross-Site Scripting) attacks
2. **Data Integrity**: Ensures special characters don't break URLs
3. **Standards Compliance**: Follows RFC 3986 for URL formatting

## The Simulation

This demonstration shows two scenarios:

### 1. Unsafe Output (Vulnerable)
The input is directly inserted into HTML without any encoding. This allows attackers to inject malicious scripts.

Example attack input:
```
html
<img scr=x onerror=alert('XSS')>
```

### 2. Safe Output (Protected)
The input is properly encoded using `encodeURIComponent()` before display. This converts special characters to their safe HTML entities.

## Running the Simulation

Simply open the HTML file in a web browser:

```
bash
# Open in browser
Task 1/For URL/url_encoding_simulation.html
```
## What the Program Looks Like

![URL GUI Main Interface](/Task%201/Screenshots/urlefront.png)

---

## Demonstration

1. Enter any text in the input field
2. Click "Submit (Unsafe)" - see how HTML/script tags execute
3. Click "Submit (Safe)" - see how the same content is safely displayed
4. Try entering: <img scr=x onerror=alert('XSS')>

![URL GUI Main Interface](/Task%201/Screenshots/url%20result.png)

--- 
## Key Functions

### Unsafe (Vulnerable)
```
javascript
function submitUnsafe() {
    const input = document.getElementById("userInput").value;
    document.getElementById("unsafeResult").innerHTML = input;
}
```

### Safe (Protected)
```
javascript
function submitSafe() {
    const input = document.getElementById("userInput").value;
    const encoded = encodeURIComponent(input);
    const decoded = decodeURIComponent(encoded);
    document.getElementById("safeResult").innerText = decoded;
}
```

## Key Learnings

1. **Always encode user input**: Never directly insert user data into HTML
2. **Use encodeURIComponent()**: For encoding URL parameters
3. **Use innerText instead of innerHTML**: Prevents XSS when displaying user content
4. **Validate and sanitize input**: Additional layer of protection

---

## Navigation

- [Task 1 README](../README.md)
- [Base64 Encoding](../For%20Base64/README.md)
- [OAuth Simulation](../for%20Oauth/README.md)
- [HTTP vs HTTPS](../HTTP%20vs%20HTTPS%20simulation/README.md)
