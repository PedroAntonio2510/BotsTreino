import qrcode 

#Codigo para gerar QrCode

data = "https://github.com/PedroAntonio2510"
qr = qrcode.QRCode(version=1)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")
