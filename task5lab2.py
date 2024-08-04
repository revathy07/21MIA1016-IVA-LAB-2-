import ffmpeg
import os

# Function to reconstruct video from I-frames
def reconstruct_video_from_i_frames(input_dir, output_video, frame_rate):
    # Create a video from images
    ffmpeg.input(os.path.join(input_dir, 'I_frame_%04d.png'), framerate=frame_rate).output(
        output_video, 
        vcodec='libx264', 
        crf=23,  # Constant Rate Factor, adjust for quality
        pix_fmt='yuv420p'
    ).run()
    
    print(f"Video reconstructed and saved as {output_video}")

# Paths
input_dir = 'extracted_frames/I_frames'
output_video = 'reconstructed_video.mp4'
frame_rate = 5  # Reduced frame rate for the reconstructed video

# Reconstruct video
reconstruct_video_from_i_frames(input_dir, output_video, frame_rate)
