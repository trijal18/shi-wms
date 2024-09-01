import cv2
import os

def create_video(image_folder, output_video,duration, fps=1):
    number_of_frames=len(image_folder)
    fps=number_of_frames//duration
    # Get a list of images in the directory
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()  # Ensure images are sorted in the correct order

    if not images:
        print("No images found in the specified folder.")
        return

    # Determine the width and height from the first image
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID', 'MJPG', etc. for different formats
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        
        if frame is None:
            print(f"Failed to load {image_path}. Skipping.")
            continue
        
        video.write(frame)

    # Release the video writer object
    video.release()
    print(f"Video saved as {output_video}")

if __name__== "__main__":
    # Example usage:
    image_folder = r"D:\projects\sih_wms\not fake\cd"  # Folder containing images
    output_video = image_folder+r"\not_wow.mp4" # Output video file name
    duration = 4 

    create_video(image_folder, output_video, fps)
