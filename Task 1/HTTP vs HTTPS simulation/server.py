from flask import Flask, request, send_file
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json['image']
    image_bytes = base64.b64decode(data)

    with open('uploads/saved_image.png', 'wb') as f:
        f.write(image_bytes)

    print("[SERVER] Image saved successfully")
    return 'OK'

# app.run(host='127.0.0.1', port=5000) # for http
app.run(
    host='127.0.0.1',
    port=5000,
    ssl_context="adhoc"
) # for https
