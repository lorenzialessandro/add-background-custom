import os
from PIL import Image
from rembg import remove
import io

def process():

    # Define the directory with PNG images and the background image path
    folder_path = '' # Path to the folder containing PNG images
    background_image_path = '' # Path to the background image
    output_folder = '' # Output folder to save the processed images

    print(f"Processing PNG images in {folder_path} with background image {background_image_path}...")

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        print(f"Creating output folder: {output_folder}")
        os.makedirs(output_folder)

    # Open the background image
    background = Image.open(background_image_path)

    # Loop through all PNG files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            print(f"Processing {filename}...")
            
            # Open the PNG image
            png_image_path = os.path.join(folder_path, filename)
            with open(png_image_path, 'rb') as f:
                # Remove the background using rembg
                removed_bg_data = remove(f.read())
            
            # Load the image data as a Pillow image
            png_image = Image.open(io.BytesIO(removed_bg_data)).convert("RGBA")
            
            # Resize the PNG to match the background size (optional, depending on requirement)
            png_resized = png_image.resize(background.size, Image.Resampling.LANCZOS)
            
            # Create a copy of the background to overlay the PNG
            composite = background.copy()
            
            # Paste the PNG onto the background (adjust position as needed)
            composite.paste(png_resized, (0, 0), png_resized)  # (0, 0) is top-left
            
            # Save the new image
            output_path = os.path.join(output_folder, filename)
            composite.save(output_path)

            print(f"Saved {filename} to {output_folder}")


def main():
    # print("Starting...")
    process()
    
    
if __name__ == "__main__":
    main()