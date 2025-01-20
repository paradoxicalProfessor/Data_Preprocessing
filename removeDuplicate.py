import os
import imagehash
from PIL import Image
from collections import defaultdict

def find_and_remove_duplicates(folder_path):
    # Dictionary to store image hashes
    image_hashes = defaultdict(list)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        try:
            # Open image and calculate its hash
            with Image.open(file_path) as img:
                img_hash = imagehash.average_hash(img)
            
            # Store the file path in the dictionary with the hash as key
            image_hashes[img_hash].append(file_path)
        
        except Exception as e:
            print(f"Could not process {file_path}: {e}")
    
    # Find and delete duplicates
    duplicates = 0
    for hash_value, file_paths in image_hashes.items():
        if len(file_paths) > 1:
            # Keep the first file and delete the rest
            for duplicate_path in file_paths[1:]:
                os.remove(duplicate_path)
                duplicates += 1
                print(f"Removed duplicate: {duplicate_path}")
    
    print(f"Total duplicates removed: {duplicates}")

# Specify the folder path
folder_path = "F:\\Semester 7\\Data Mining and Machine Learning Lab\\Research\\Classification\\Processed Images Updated\\Leaf Spot Disease"  # Change this to your folder path
find_and_remove_duplicates(folder_path)
