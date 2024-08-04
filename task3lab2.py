import subprocess
import os
from PIL import Image
import matplotlib.pyplot as plt

def run_ffmpeg_command(command):
    
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        raise

def extract_frames(input_video):
    # Define the output directories
    i_frames_dir = "extracted_frames/I_frames"
    p_frames_dir = "extracted_frames/P_frames"
    b_frames_dir = "extracted_frames/B_frames"

    # Create the output directories if they do not exist
    os.makedirs(i_frames_dir, exist_ok=True)
    os.makedirs(p_frames_dir, exist_ok=True)
    os.makedirs(b_frames_dir, exist_ok=True)

    # FFmpeg commands to extract frames
    i_frame_command = f"ffmpeg -i \"{input_video}\" -vf \"select='eq(pict_type,I)'\" -vsync vfr \"{i_frames_dir}/I_frame_%04d.png\""
    p_frame_command = f"ffmpeg -i \"{input_video}\" -vf \"select='eq(pict_type,P)'\" -vsync vfr \"{p_frames_dir}/P_frame_%04d.png\""
    b_frame_command = f"ffmpeg -i \"{input_video}\" -vf \"select='eq(pict_type,B)'\" -vsync vfr \"{b_frames_dir}/B_frame_%04d.png\""

    # Run FFmpeg commands
    print("Extracting I-frames...")
    run_ffmpeg_command(i_frame_command)

    print("Extracting P-frames...")
    run_ffmpeg_command(p_frame_command)

    print("Extracting B-frames...")
    run_ffmpeg_command(b_frame_command)

    print("Frames extraction completed.")

def display_frames(frame_dir, num_frames=2):
    """Display only the first `num_frames` frames from a given directory using Pillow."""
    frame_files = [f for f in sorted(os.listdir(frame_dir)) if f.endswith('.png')]
    for file_name in frame_files[:num_frames]:
        img_path = os.path.join(frame_dir, file_name)
        with Image.open(img_path) as img:
            plt.imshow(img)
            plt.title(f"Frame: {file_name}")
            plt.axis('off')
            plt.show()

# Define the input video file
input_video = "videosa.mp4"

# Extract the frames
extract_frames(input_video)

# Display the first two frames of each type
print("Displaying I-frames...")
display_frames("extracted_frames/I_frames", num_frames=2)

print("Displaying P-frames...")
display_frames("extracted_frames/P_frames", num_frames=2)

print("Displaying B-frames...")
display_frames("extracted_frames/B_frames", num_frames=2)
