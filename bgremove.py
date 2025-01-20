from rembg import remove
from PIL import Image, ImageOps
import os
import io

input_folder = "F:\\Semester 7\\Data Mining and Machine Learning Lab\\Research\\White Mold"
output_folder = "F:\\Semester 7\\Data Mining and Machine Learning Lab\\Research\\White Mold"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image and try to remove EXIF data
        try:
            with Image.open(input_path) as img:
                # Attempt to correct orientation if EXIF data is present
                try:
                    img = ImageOps.exif_transpose(img)
                except Exception as exif_error:
                    print(f"Skipping EXIF processing for {filename}: {exif_error}")
                
                # Re-save the image without EXIF data in case of issues
                buffered = io.BytesIO()
                img.convert("RGB").save(buffered, format="PNG")
                image_data = buffered.getvalue()
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

        # Remove the background
        output_data = remove(image_data)

        # Open the result image directly from output_data
        result_image = Image.open(io.BytesIO(output_data))  # Use BytesIO to read image data

        # Create a white background image
        white_bg = Image.new("RGBA", result_image.size, (255, 255, 255, 255))  # RGBA for transparency handling

        # Paste the result image on the white background (with transparency handling)
        if result_image.mode in ('RGBA', 'LA') or (result_image.mode == 'P' and 'transparency' in result_image.info):
            white_bg.paste(result_image, mask=result_image.split()[3])  # Use the alpha channel as a mask
        else:
            white_bg.paste(result_image)

        # Save the image with the white background
        white_bg.convert("RGB").save(output_path, format="JPEG")  # Convert to RGB for JPEG

        print(f"Processed {filename}")
