import qrcode

# Take input from user and ask to submit a link
# Then remove whitespace from string data
data = str.strip(input("Enter text or URL: "))
filename = input("Enter the filename: ")



# Create QR Code using data
img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
# Save file as filename entered
img.save(f"{filename}.png")