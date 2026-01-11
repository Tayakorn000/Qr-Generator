import qrcode
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H

# Link Input
link = input("LINK TO GEN QR:  ").strip()

# Determine Logo Based on Link
if "github.com" in link:
    logo_path = "github.png"
elif "youtube.com" in link or "youtu.be" in link:
    logo_path = "youtube.png"
else:
    logo_path = None  # ลิงก์อื่นไม่ใส่โลโก้

# QR Code Configuration
qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,  # ทนสุด
    box_size=20,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Logo Integration
if logo_path:
    logo = Image.open(logo_path).convert("RGBA")

    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 5 
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    pos = (
        (qr_width - logo_size) // 2,
        (qr_height - logo_size) // 2
    )

    qr_img.paste(logo, pos, logo)

# Save QR Code
qr_img.save("qr_with_logo.png")
print("สร้าง QR พร้อมโลโก้สำเร็จ")
