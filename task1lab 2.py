import ffmpeg
import json

def get_video_metadata(video_path):
        # Probe the video to get metadata
    probe = ffmpeg.probe(video_path, v='error', select_streams='v:0', show_entries='stream=width,height,r_frame_rate')
    video_stream = probe['streams'][0]
    
    # Extract width, height, and frame rate
    width = video_stream['width']
    height = video_stream['height']
    frame_rate_str = video_stream['r_frame_rate']
    resolution = f"{width}x{height}"
    
    # Convert frame rate string to a float value
    frame_rate_numerator, frame_rate_denominator = map(int, frame_rate_str.split('/'))
    fps = frame_rate_numerator / frame_rate_denominator
    
    metadata = {
        'width': width,
        'height': height,
        'resolution': resolution,
        'frame_rate': frame_rate_str,
        'fps': fps
    }
    
    return metadata

# Path to your video file (update this with your actual video path)
video_path = 'videosa.mp4'

# Get video metadata
video_metadata = get_video_metadata(video_path)
print(json.dumps(video_metadata, indent=4))
