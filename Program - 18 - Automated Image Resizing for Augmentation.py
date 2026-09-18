#Program - 18 - Automated Image Resizing for Augmentation
import os
from PIL import Image
from torchvision import transforms

input_folder = 'images' 
output_folder = 'resized_images'
os.makedirs(output_folder, exist_ok=True)

resize_transform = transforms.Resize((250, 250))

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert('RGB')
        resized_img = resize_transform(img)

        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)
    print(f"Resized and saved: {output_folder}")
