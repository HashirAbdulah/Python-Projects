import qrcode as q
from PIL import Image

qr = q.QRCode(
    version=1,
    error_correction=q.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://www.youtube.com/")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("filenamewithextension.png")