import os

# Specify the folder containing the images
folder_path = "F:\Semester 7\Data Mining and Machine Learning Lab\Research\Processed Images Folder\Augmented Images\Healthy Leaf"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Sort the files to ensure consistent renaming order
image_files.sort()

# First, rename all files to a temporary name to avoid conflicts
for index, filename in enumerate(image_files, start=1):
    # Define the temporary filename
    temp_filename = f"temp_{index}.jpg"
    
    # Create the full path for old and temporary file names
    old_file = os.path.join(folder_path, filename)
    temp_file = os.path.join(folder_path, temp_filename)
    
    # Rename the file to the temporary name
    os.rename(old_file, temp_file)

# Now, rename the temporary files to the final desired format
for index, temp_filename in enumerate(sorted(os.listdir(folder_path)), start=1):
    if temp_filename.startswith("temp_"):
        # Define the final filename
        final_filename = f"Healthy Leaf Image {index}.jpg"
        
        # Create the full path for temporary and final file names
        temp_file = os.path.join(folder_path, temp_filename)
        final_file = os.path.join(folder_path, final_filename)
        
        # Rename the file to the final name
        os.rename(temp_file, final_file)
        print(f"Renamed '{temp_filename}' to '{final_filename}'")

print("All files have been renamed.")
