from flask import Flask, request, jsonify, render_template, send_file
import os
from modules.generate_video import generate_video
from modules.interpolation.alpha_blending import increase_frame_rate

app = Flask(__name__)

# Ensure the 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

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

    try:
        # Call the Python function to generate the video
        video_path = generate_video(text)

        if os.path.exists(video_path):
            return jsonify(success=True, videoUrl=f"/download/{video_path}")
        else:
            return jsonify(success=False), 500
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route('/interpolate')
def video_processing():
    return render_template('interpolate.html')

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify(success=False, message="No video file uploaded"), 400

    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify(success=False, message="No selected video"), 400

    if video_file:
        # Sanitize filename to prevent security issues
        video_filename = os.path.basename(video_file.filename)
        video_path = os.path.join('uploads', video_filename)
        video_file.save(video_path)
        
        try:
            processed_video_path = increase_frame_rate(video_path, "inti.mp4", 2)

            if os.path.exists(processed_video_path):
                return jsonify(success=True, videoUrl=f"/download/{processed_video_path}")
            else:
                return jsonify(success=False), 500
        except Exception as e:
            return jsonify(success=False, message=str(e)), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Sanitize filename to prevent security issues
    filename = os.path.basename(filename)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
