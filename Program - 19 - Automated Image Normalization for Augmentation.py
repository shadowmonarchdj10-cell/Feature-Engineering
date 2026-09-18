#Program - 19 - Automated Image Normalization for Augmentation
import os
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from PIL import Image

INPUT_DIR = "C:/Users/MACFAST/AppData/Local/Programs/Python/Python313/Lib/site-packages/torchvision/datasets/images"
OUTPUT_DIR = "augmented_images"   
BATCH_SIZE = 16                   
IMAGE_SIZE = (224, 224) 

os.makedirs(OUTPUT_DIR, exist_ok=True)

transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
dataset = datasets.ImageFolder(root=INPUT_DIR, transform=transform)

loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

print(f"Saving augmented images to {OUTPUT_DIR}...")

for batch_idx, (images, labels) in enumerate(loader):
    save_path = os.path.join(OUTPUT_DIR, f"batch_{batch_idx}.png")
    save_image(images, save_path, normalize=True)
    print(f"Saved: {save_path}")
    if batch_idx == 2:
        break
print("✅ Augmentation complete.")
