import ffmpeg
import matplotlib.pyplot as plt

def get_frame_info(video_file):
    
    # Use ffmpeg to extract frame information
    probe = ffmpeg.probe(video_file, v='error', select_streams='v:0', show_entries='frame=pict_type', format='json')
    
    # Extract 'frames' list from the JSON structure
    frames = probe['frames']  
    
    return frames

def analyze_frame_distribution(frame_info):
    
    frame_counts = {'I': 0, 'P': 0, 'B': 0}
    
    # Count each type of frame
    for frame in frame_info:
        pict_type = frame.get('pict_type')
        if pict_type in frame_counts:
            frame_counts[pict_type] += 1
    
    # Calculate percentages
    total_frames = sum(frame_counts.values())
    if total_frames > 0:
        percentages = {k: (v / total_frames) * 100 for k, v in frame_counts.items()}
    else:
        percentages = {k: 0 for k in frame_counts}
    
    return frame_counts, percentages

def plot_frame_distribution(frame_counts):
    
    labels = frame_counts.keys()
    sizes = frame_counts.values()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Bar chart
    ax.bar(labels, sizes, color=['red', 'green', 'blue'])
    ax.set_title('Frame Type Distribution (Bar Graph)')
    ax.set_xlabel('Frame Type')
    ax.set_ylabel('Count')
    
    plt.tight_layout()
    plt.show()

def main(video_file):
    
    frame_info = get_frame_info(video_file)
    frame_counts, percentages = analyze_frame_distribution(frame_info)
    
    print("Frame Counts:", frame_counts)
    print("Frame Percentages:", percentages)
    
    plot_frame_distribution(frame_counts)

if __name__ == "__main__":
    video_file = 'videosa.mp4' 
    main(video_file)
