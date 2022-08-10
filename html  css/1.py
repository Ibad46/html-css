from ensurepip import version
from turtle import fillcolor
import qrcode #install qrcode
import image #pip install Image


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
                  box_size=5,
                  border=4)
qr.add_data("https://www.instagram.com/afzaar_fsk") #can pass link 
qr.make(fit=True)

img=qr.make_image(fillcolor="black", back_color="yellow")
img.save("myprofile.png")