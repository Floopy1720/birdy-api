from flask import Flask, render_template, request
from PIL import Image, ImageFont, ImageDraw
app = Flask(__name__)

stonk_img = Image.open('static/stonk orginal.png')
draw_stonk = ImageDraw.Draw(stonk_img)
font = ImageFont.truetype('Roboto-Medium.ttf', 150)

@app.route('/')
def hello_world():
	return '<h1> Hello </h1>'
	pass
@app.route('/stonk')
def stonk():
	text = request.args.get('text')
	draw_stonk.text((1250,900), text, font = font, fill='white')
	stonk_img.save('static/stonk.png')
	return render_template('index.html')
	pass

@app.route('/stonk_test')
def stonk_test():
	test_text = request.args.get('text')
	return test_text
	pass