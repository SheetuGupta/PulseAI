# e:/videoAI/form_analysis/pipeline/video_processor.py
import ffmpeg
import tempfile
import os
from PIL import Image
from config.settings import MAX_VIDEO_SECONDS

def validate_video(video_bytes: bytes) -> dict:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(video_bytes)
        temp_path = temp_file.name

    try:
        probe = ffmpeg.probe(temp_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        
        if not video_stream:
            return {"valid": False, "error": "No video stream found."}
            
        duration = float(probe['format'].get('duration', 0))
        if duration > MAX_VIDEO_SECONDS:
            return {"valid": False, "error": f"Video too long. Maximum is {MAX_VIDEO_SECONDS} seconds."}
            
        width = int(video_stream.get('width', 0))
        height = int(video_stream.get('height', 0))
        fps_str = video_stream.get('r_frame_rate', '0/1')
        num, den = map(int, fps_str.split('/'))
        fps = num / den if den != 0 else 0
        
        return {
            "valid": True, 
            "duration": duration, 
            "width": width, 
            "height": height, 
            "fps": fps
        }
    except ffmpeg.Error as e:
        return {"valid": False, "error": f"FFmpeg error: {e.stderr.decode('utf8', errors='ignore') if e.stderr else str(e)}"}
    except Exception as e:
        return {"valid": False, "error": f"Validation error: {str(e)}"}
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

def extract_frames(video_bytes: bytes, fps: int = 1) -> list[dict]:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(video_bytes)
        temp_video_path = temp_file.name

    output_dir = tempfile.mkdtemp()
    extracted_frames = []

    try:
        (
            ffmpeg
            .input(temp_video_path)
            .filter("fps", fps=fps)
            .output(f"{output_dir}/frame_%03d.jpg", format="image2", vcodec="mjpeg")
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        
        files = sorted([f for f in os.listdir(output_dir) if f.endswith(".jpg")])
        for i, file_name in enumerate(files):
            file_path = os.path.join(output_dir, file_name)
            image = Image.open(file_path).copy()
            timestamp = i / float(fps)
            extracted_frames.append({"timestamp": timestamp, "image": image})
            
    except Exception as e:
        print(f"Error extracting frames: {str(e)}")
    finally:
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
        for root, dirs, files in os.walk(output_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        if os.path.exists(output_dir):
            os.rmdir(output_dir)
            
    return extracted_frames
