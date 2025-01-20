import cv2
import os

def resize_images(input_folder, output_folder, size=(224, 224)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        
        if img is not None:
            resized_img = cv2.resize(img, size)
            cv2.imwrite(os.path.join(output_folder, filename), resized_img)

# Usage
resize_images('F:\\Semester 7\\Data Mining and Machine Learning Lab\\Research\\Processed Images Folder\\Classified Images\\Wilt Disease', 'F:\\Semester 7\\Data Mining and Machine Learning Lab\\Research\\Processed Images Folder\\Resized\\Wilt Disease')
