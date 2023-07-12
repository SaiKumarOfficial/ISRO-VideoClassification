import cv2
import os
from dotenv import load_dotenv
load_dotenv()
# Directory containing the videos
videos_directory = os.getenv('VIDEO_DIR')

# Output directory to save the frames
output_directory = os.getenv('OUTPUT_IMAGE_DIR')

# Iterate through all video files in the directory
for filename in os.listdir(videos_directory):
    if filename.endswith('.mp4'):
        video_path = os.path.join(videos_directory, filename)

        # Create a new directory to save frames for each video
        video_output_directory = os.path.join(output_directory, filename[:-4])
        os.makedirs(video_output_directory, exist_ok=True)

        # Open the video file
        video = cv2.VideoCapture(video_path)

        frame_count = 0
        save_count = 0

        # Read frames from the video
        while True:
            success, frame = video.read()

            # Check if frame reading was successful
            if not success:
                break

            # Resize the frame
            frame = cv2.resize(frame, (500, 500))

            # Convert the frame to grayscale
            

            frame_count += 1

            # Save every 10th frame
            if frame_count % 10 == 0:
                save_count += 1
                frame_path = os.path.join(video_output_directory, f'frame_{save_count:06d}.jpg')
                cv2.imwrite(frame_path, frame)

        # Release the video capture
        video.release()
