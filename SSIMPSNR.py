import subprocess
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

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

    # Create the output directories if they do not exist
    os.makedirs(i_frames_dir, exist_ok=True)
    os.makedirs(p_frames_dir, exist_ok=True)

    # FFmpeg commands to extract frames
    i_frame_command = f"ffmpeg -i \"{input_video}\" -vf \"select='eq(pict_type,I)'\" -vsync vfr \"{i_frames_dir}/I_frame_%04d.png\" -frames:v 1"
    p_frame_command = f"ffmpeg -i \"{input_video}\" -vf \"select='eq(pict_type,P)'\" -vsync vfr \"{p_frames_dir}/P_frame_%04d.png\" -frames:v 1"

    # Run FFmpeg commands
    print("Extracting first I-frame...")
    run_ffmpeg_command(i_frame_command)

    print("Extracting first P-frame...")
    run_ffmpeg_command(p_frame_command)

    print("Frames extraction completed.")

def load_frame(frame_dir, frame_type):
    frame_file = sorted(os.listdir(frame_dir))[0]
    frame_path = os.path.join(frame_dir, frame_file)
    frame = cv2.imread(frame_path)
    return frame

def calculate_ssim_psnr(img1, img2):
    """Calculate SSIM and PSNR between two images."""
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    ssim_value = ssim(gray_img1, gray_img2, data_range=gray_img2.max() - gray_img2.min())
    psnr_value = psnr(img1, img2)
    
    return ssim_value, psnr_value

# Define the input video file
input_video = "videosa.mp4"

# Extract the frames
extract_frames(input_video)

# Directory where extracted frames are saved
i_frame_dir = 'extracted_frames/I_frames'
p_frame_dir = 'extracted_frames/P_frames'

# Load the first frames
i_frame = load_frame(i_frame_dir, 'I')
p_frame = load_frame(p_frame_dir, 'P')

# Calculate SSIM and PSNR between the first I-frame and first P-frame
ssim_value, psnr_value = calculate_ssim_psnr(i_frame, p_frame)

# Print SSIM and PSNR values
print(f'SSIM between first I-frame and P-frame: {ssim_value:.4f}')
print(f'PSNR between first I-frame and P-frame: {psnr_value:.4f}')
