import os
import shutil
import random
from pathlib import Path

# Główna konfiguracja
SOURCE_DIR = "Train"
TARGET_DIR = "dataset"
SPLIT_RATIO = 0.8  # 80% train, 20% val

# Klasy (foldery)
CLASSES = [
     "Graffiti","Vandalism"
]

# Tworzenie struktury folderów
for split in ["train", "val"]:
    for class_name in CLASSES:
        (Path(TARGET_DIR) / "images" / split / class_name).mkdir(parents=True, exist_ok=True)
        (Path(TARGET_DIR) / "labels" / split / class_name).mkdir(parents=True, exist_ok=True)

# Dzielenie obrazów i etykiet
for class_name in CLASSES:
    src_class_path = Path(SOURCE_DIR) / class_name
    images = list(src_class_path.glob("*.png"))
    random.shuffle(images)
    split_idx = int(len(images) * SPLIT_RATIO)
    train_imgs = images[:split_idx]
    val_imgs = images[split_idx:]

    for split, split_imgs in zip(["train", "val"], [train_imgs, val_imgs]):
        for img_path in split_imgs:
            # Ścieżka docelowa do obrazu
            dst_img = Path(TARGET_DIR) / "images" / split / class_name / img_path.name
            shutil.copy(img_path, dst_img)

            # Ścieżka do odpowiadającej etykiety
            label_path = img_path.with_suffix(".txt")
            if label_path.exists():
                dst_label = Path(TARGET_DIR) / "labels" / split / class_name / label_path.name
                shutil.copy(label_path, dst_label)

print("✅ Obrazy i etykiety zostały podzielone i skopiowane do YOLOv8.")
