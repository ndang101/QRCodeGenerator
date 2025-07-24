import qrcode

#take input from user and ask to submit a link

user_input = input("Enter text or link: ")

img = qrcode.make(user_input)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")