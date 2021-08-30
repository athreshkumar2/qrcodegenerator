""" QRCode Generator """
#1. We will Import 2 modules (qrcode) & (image).
#2. We will declare qrcode as qr and will declare Parameters of BOX.
#3. We will declare any name and will paste the url in the quotes.
#4. And will add data via declared url in the Variable.
#5. Will export an image file first we will make the file using the make function.
#6. Then finally we will save the image in the .png Format.


from typing import Generator
from qrcode.main import QRCode

import qrcode
import image

qr = qrcode.QRCode(
    version=15,       #It means the version of QRcode Higher the number bigger the picture and more complex code.
    box_size=10,      #Size of the Box where QRcode will be diaplayed.
    border=5          #It is the white part of the image - Border will be filled with white from 4 sides.
)

insta = "https://photos.app.goo.gl/u35rA6up5xdNb9TX6"

qr.add_data(insta)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("instagram.png")