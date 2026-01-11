# 🔳 QR Code Generator with Auto-Logo

A Python automation script that generates high-quality QR codes and automatically embeds platform-specific logos (GitHub or YouTube) based on the input URL.

## ✨ Features
* **Auto-Detection:** Automatically detects `github.com` or `youtube.com` links to apply the correct logo.
* **Smart Branding:** Places the logo in the center of the QR code without compromising scannability.
* **High Reliability:** Uses `ERROR_CORRECT_H` (High Error Correction) to ensure the QR code works even with the image overlay.
* **Fallback:** Generates a standard clean QR code for non-specific links.

## 🛠️ Prerequisites

Before running the script, make sure you have **Python 3.x** installed.

You will need to install the following dependencies:

```bash
pip install qrcode[pil] pillow
```

## How to Use
Run the script:

```Bash
python main.py
```
Enter your link when prompted: Plaintext
LINK TO GEN QR: [https://github.com/your-username](https://github.com/your-username)

Owner Tayakorn000
