from flask import Flask, request, Response, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'frame' not in request.files:
        return "No file part", 400
    file = request.files['frame']
    if file.filename == '':
        return "No selected file", 400
    file.save(os.path.join(UPLOAD_FOLDER, 'frame.jpg'))
    return "File uploaded successfully", 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/stream')
def stream_image():
    def generate():
        try:
            while True:
                with open(os.path.join(UPLOAD_FOLDER, 'frame.jpg'), 'rb') as f:
                    frame = f.read()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print(f"Error: {e}")
            yield (b'--frame\r\n'
                   b'Content-Type: text/plain\r\n\r\n' + b'Failed to load image' + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
