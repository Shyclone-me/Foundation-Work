# Base64 Encoding Simulation

## Overview

This is a GUI application that demonstrates Base64 encoding and decoding. It shows that **Base64 is NOT security** - anyone can encode or decode data without any key.

## What is Base64?

Base64 is an encoding scheme that converts binary data into ASCII text format. It's commonly used for:
- Embedding images in HTML/CSS
- Transmitting data over protocols that only support text
- Encoding email attachments (MIME)

**Important**: Base64 is NOT encryption! It's simply a way to represent binary data in text format. Anyone can decode Base64 without a key.

---

## Features

### Encoding
- Select any file (image, document, etc.)
- Encode it to Base64 format
- View the encoded output

### Decoding
- Paste Base64 encoded data
- Decode and display the original file
- Preview images directly in the application
- Save decoded files to disk

## Running the Application

```
bash
cd "Task 1/For Base64"
python base64demo.py
```

## Requirements

- Python 3.x
- tkinter (included in standard Python)
- PIL/Pillow: 
```bash
pip install pillow
```

The application uses:
- `tkinter` for the GUI
- `base64` module for encoding/decoding
- `PIL` for image preview
- `filedialog` for file selection

---
## What the Program Looks Like

![Base64 GUI Main Interface](/Task%201/Screenshots/base64demo.png)

*Main window of the Base64 encoder/decoder*

---


## Navigation

- [Task 1 README](../README.md)
- [URL Encoding Simulation](../For%20URL/README.md)
- [OAuth Simulation](../for%20Oauth/README.md)
- [HTTP vs HTTPS](../HTTP%20vs%20HTTPS%20simulation/README.md)
