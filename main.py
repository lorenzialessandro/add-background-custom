import os
from PIL import Image
from rembg import remove
import io

def process():
    
    # Change the following variables to match your requirements
    
    folder_path = 'src/input/'  # Folder path containing images to process
    background_image_path = 'src/background/sponsor.png' # Custom background image to overlay the processed images (ex. sponsor board)
    output_folder = 'src/output/' # # Output folder for processed images - will be created if it doesn't exist

    # End of variables to change
    
    print(
        f"Processing image images in {folder_path} with background image {background_image_path}...")

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        print(f"Creating output folder: {output_folder}")
        os.makedirs(output_folder)

    # Open the background image
    background = Image.open(background_image_path)

    # Loop through all image files in the folder
    for filename in os.listdir(folder_path):
        print(f"Processing {filename}...")
        if filename.endswith(".png") or filename.endswith(".jpg"): 
            # Open the image
            image_path = os.path.join(folder_path, filename)
            with open(image_path, 'rb') as f:
                # Remove the background using rembg
                removed_bg_data = remove(f.read())

            # Load the image data as a Pillow image
            image = Image.open(io.BytesIO(removed_bg_data)).convert("RGBA")

            # Resize the image to match the background size (optional, depending on requirement)
            bg_width, bg_height = background.size
            image_width, image_height = image.size

            # Calculate the scale factor to fit the image within the background
            scale = min(bg_width / image_width, bg_height / image_height)
            new_width = int(image_width * scale)
            new_height = int(image_height * scale)

            # Resize the image with the calculated dimensions
            image_resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Create a copy of the background to overlay the image
            composite = background.copy()

            # Paste the image onto the background 
            x = (bg_width - new_width) // 2
            y = (bg_height - new_height) // 2
            composite.paste(image_resized, (x, y), image_resized)

            # Save the new image
            output_path = os.path.join(output_folder, filename)
            composite.save(output_path)

            print(f"Saved {filename} to {output_folder}")
            
def main():
    print("Starting image processing...")
    process()

if __name__ == "__main__":
    main()