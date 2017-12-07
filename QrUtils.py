import qrcode
import qrcode.image.svg
from PIL import Image,ImageDraw, ImageFont

def Create(Text):
		
	qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_H,
		box_size = 15,
		border = 5,
	)
	
	qr.add_data(Text)
	qr.make(fit=True)
	img = qr.make_image().convert('RGBA')
	txt = Image.new('RGBA', img.size, (0,0,0,1))
	fnt = ImageFont.truetype('Font/Arial.ttf',32)
	d = ImageDraw.Draw(txt)
	d.text((10,10),Text,font=fnt,fill=(0,0,0,255))
	return Image.alpha_composite( img,txt)
	