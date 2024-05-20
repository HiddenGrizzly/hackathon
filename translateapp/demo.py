# demo.py

import os
import subprocess

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

def play_videos(directory, video_list):
    """Hàm phát video."""
    for video in video_list:
        video_path = os.path.join(directory, video)
        print(f"Đang phát video: {video}")
        subprocess.run(["start", video_path])  # Trên MacOS, sử dụng "open". Trên Windows sử dụng "start", trên Linux sử dụng "xdg-open".

if __name__ == "__main__":
    video_directory = "path/to/your/video/directory"  # Thay thế bằng đường dẫn tới thư mục chứa video của bạn.
    user_input = input("Nhập đoạn văn bản: ")
    
    video_list = get_video_list(video_directory)
    found_videos = find_videos(user_input, video_list)
    
    if found_videos:
        print("Các video tìm thấy:")
        for video in found_videos:
            print(video)
        play_videos(video_directory, found_videos)
    else:
        print("Không tìm thấy video nào phù hợp.")