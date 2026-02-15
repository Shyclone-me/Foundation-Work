from flask import Flask, request, send_file
import base64

server = input("""
               Select server:
               [1] HTTP
               [2] HTTTPS 
               Enter choice:                 
               """)
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


if server == '1':
    app.run(host='127.0.0.1', port=5000)
elif server == '2':
    app.run(
    host='127.0.0.1',
    port=5000,
    ssl_context="adhoc"
) 
else:
    print("Rerun the server with appropriate choice")
