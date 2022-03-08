# Python QR Code Generator

import qrcode

property = input("What do you want to embed in your QR code? ") #Ask for the user's input
generated_qr = qrcode.make(property) #Generate the QR Code
generated_qr.save("qr.png") #Save the QR Code
