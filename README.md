# Image background removal and custom replacement

## Overview

This simple script automates the process of **removing the background from images and replacing it with a custom background**. 

The primary use case is to substitute the background with a specified image, such as a sponsor board or any other desired design. It is particularly useful for batch processing images within a directory.

## Example

<table style="border-collapse: collapse; text-align: center;">
  <thead>
    <tr>
      <th>1. Input Image</th>
      <th>2. Background Removed</th>
      <th>3. Final Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <img src="img/input.png" alt="Input Image" style="height: 300px; object-fit: cover;">
      </td>
      <td>
        <img src="img/bg_image.png" alt="Background Removed" style="height: 300px; object-fit: cover;">
      </td>
      <td>
        <img src="img/output.png" alt="Final Output" style="height: 300px; object-fit: cover;">
      </td>
    </tr>
  </tbody>
</table>



## Features
- Removes backgrounds from images using the `rembg` library.
- Replaces the removed background with a custom image.
- Resizes the input image to fit proportionally within the specified background image.
- Supports batch processing for multiple images in a folder.

## Prerequisites

- Python 3.6 or higher.
- Required Python libraries:
  - `rembg`
  - `Pillow`

Install the necessary libraries by running:
```bash
pip install rembg pillow
```

## Usage

1. Clone this repository or download the script.
2. Place the images to be processed in the folder specified by the `folder_path` variable (default: `src/input/`).
3. Provide a background image in the location specified by the `background_image_path` variable (default: `src/sponsor/sponsor.png`).
4. Specify the output folder for the processed images in the `output_folder` variable (default: `src/output/`).

### How to Run the Script

Run the script using:
```bash
python main.py
```

### Customization

Modify the following variables in the `process()` function to suit your needs:
- `folder_path`: The directory containing the images you want to process.
- `background_image_path`: The path to the background image.
- `output_folder`: The directory where processed images will be saved.

## Workflow

### Input
Place the original images in the specified input folder (`src/input/` by default).

### Processing Steps
1. The script removes the background of each image using `rembg`.
2. It overlays the resized image onto the custom background image.
3. The composite image is saved to the output folder (`src/output/` by default).

### Outputs
The processed images will be saved in the output directory, maintaining their original filenames.


## Notes
- Supported image formats are `.png` and `.jpg`.
- Ensure the background image is large enough to accommodate the input images.

## License
This project is licensed under the MIT License.

## Contributions
Contributions and improvements are welcome! Please submit a pull request or raise an issue if you encounter any problems.

