from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_videos', methods=['POST'])
def search_videos():
    text = request.form['text']
    video_directory = r"D:\FPT_aptech\video_player\static\videos"  # Thay thế bằng đường dẫn tới thư mục chứa video của bạn.
    video_list = get_video_list(video_directory)
    found_videos = find_videos(text, video_list)
    return jsonify(found_videos)

def get_video_list(directory):
    """Hàm lấy danh sách các video từ thư mục."""
    return [f for f in os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mkv'))]

def find_videos(text, video_list):
    """Hàm tìm kiếm video theo từ khóa."""
    words = text.split()
    found_videos = []
    for word in words:
        for video in video_list:
            if word.lower() in video.lower():
                found_videos.append(video)
                break
    return found_videos

if __name__ == '__main__':
    app.run(debug=True)
