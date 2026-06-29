from flask import Flask, render_template
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def generate_qr():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
    qr = qrcode.make(url)
    qr.save("static/qr.png")
    print("✅ QR-код создан!")

if __name__ == '__main__':
    if not os.path.exists("static/qr.png"):
        generate_qr()
    app.run(debug=True, host='0.0.0.0', port=5000)