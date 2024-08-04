import os

def list_frame_sizes(frame_dir):
    """List file sizes of frames in the given directory."""
    frame_files = sorted([f for f in os.listdir(frame_dir) if f.endswith('.png')])
    sizes = {}
    
    for file_name in frame_files:
        file_path = os.path.join(frame_dir, file_name)
        size = os.path.getsize(file_path)
        sizes[file_name] = size
    
    return sizes

def calculate_average_size(sizes):
    """Calculate the average size from a dictionary of file sizes."""
    if not sizes:
        return 0
    return sum(sizes.values()) / len(sizes)

def display_and_compare_sizes(directories):
    """Display sizes of each frame and compare average sizes."""
    averages = {}
    
    for frame_type, directory in directories.items():
        sizes = list_frame_sizes(directory)
        if sizes:
            print(f"\n{frame_type} Frames Sizes:")
            for frame, size in sizes.items():
                print(f"{frame}: {size / 1024:.2f} KB")  # Convert bytes to KB
            average_size = calculate_average_size(sizes)
            print(f"Average size of {frame_type} frames: {average_size / 1024:.2f} KB")  # Convert bytes to KB
            averages[frame_type] = average_size / 1024  # Store average size in KB
        else:
            print(f"No {frame_type} frames found in directory.")
            averages[frame_type] = 0

    # Compare average sizes
    print("\nAverage Frame Size Comparison:")
    for frame_type, avg_size in averages.items():
        print(f"Average size of {frame_type} frames: {avg_size:.2f} KB")
    
    # Display the comparison
    print("\nComparison of Average Sizes:")
    sorted_avg_sizes = sorted(averages.items(), key=lambda x: x[1])
    for i in range(len(sorted_avg_sizes)):
        for j in range(i + 1, len(sorted_avg_sizes)):
            frame_type_i, avg_size_i = sorted_avg_sizes[i]
            frame_type_j, avg_size_j = sorted_avg_sizes[j]
            print(f"{frame_type_i} vs {frame_type_j}: {avg_size_i:.2f} KB vs {avg_size_j:.2f} KB")

# Define the directories
directories = {
    "I-Frame": "extracted_frames/I_frames",
    "P-Frame": "extracted_frames/P_frames",
    "B-Frame": "extracted_frames/B_frames"
}

# Display and compare sizes
display_and_compare_sizes(directories)
