from flask import Flask, render_template, request, send_file
import io
import string
import random
from PIL import Image, ImageDraw, ImageFont

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def id_generator(size=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def serve_pil_image(txt='Hello'):
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    fnt = ImageFont.truetype('./fonts/verdanab.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((10,10), txt, font=fnt, fill=(255, 255, 0))
    img.save('static/image/out.jpeg', 'JPEG', quality=70)

@app.route('/', methods=['GET'])
def getCapatcha():
    txt = id_generator()
    serve_pil_image(txt)
    return render_template(
    "index.html",
    capatcha=txt
    )

@app.route('/', methods=['POST'])
def postCapatcha():
    txt = id_generator()
    serve_pil_image(txt)
    info = request.form
    provided = info.get('provided', '')
    guess = info.get('guess', '')
    print("guess: {0}, provided: {1}".format(guess, provided))
    return render_template(
    "index.html",
    msg='Match is {0}'.format(provided == guess),
    capatcha=txt
    )

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
