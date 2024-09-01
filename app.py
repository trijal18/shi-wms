from flask import Flask, request, jsonify, render_template, send_file
import os
from modules.generate_video import generate_video

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify(success=False), 400

    # Call the Python function to generate the video
    video_path = generate_video(text)

    if os.path.exists(video_path):
        return jsonify(success=True, videoUrl=f"/download/{video_path}")
    else:
        return jsonify(success=False), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
