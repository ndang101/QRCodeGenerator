import qrcode

# Take input from user and ask to submit a link
# Then remove whitespace from string data
data = input("Enter text or URL: ").strip()
# Asks user for what they want to name the file
filename = input("Enter the filename: ").strip()

# Create QR Code using data
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
img = qr.make_image(fill_color="black", back_color="white")
qr.make(fit=True)



# Save file as filename entered
img.save(f"{filename}.png")