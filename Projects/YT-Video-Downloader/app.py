import yt_dlp
import os
import re
from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)

# Ensure the 'downloads' directory exists
downloads_dir = os.path.abspath("downloads")
os.makedirs(downloads_dir, exist_ok=True)

def sanitize_filename(filename):
    # Remove invalid characters for Windows filenames and replace consecutive invalid characters with a single underscore
    sanitized_filename = re.sub(r'[\/:*?"<>|]+', '_', filename)
    return sanitized_filename

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("video_url")
        ydl_opts = {
            'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),  # Set the download location
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', 'video')
                ydl.download([url])
            
            sanitized_video_title = sanitize_filename(video_title)
            video_filename = os.path.join(downloads_dir, f"{sanitized_video_title}.mp4")
            
            print("Video filename:", video_filename)  # Debugging output
            
            if os.path.exists(video_filename):
                return send_file(video_filename, as_attachment=True)
            else:
                return jsonify({"error": "Video file not found."}), 404
        
        except Exception as e:
            return f"An error occurred: {str(e)}"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
