import qrcode

# Take input from user and ask to submit a link
# Then remove whitespace from string data
data = input("Enter text or URL: ").strip()
# Asks user for what they want to name the file
filename = input("Enter the filename: ").strip()

# Create QR Code using data
img = qrcode.make(data)

# Save file as filename entered
img.save(f"{filename}.png")