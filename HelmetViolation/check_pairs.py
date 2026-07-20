import os

image_dir = "FinalDataset/train/images"
label_dir = "FinalDataset/train/labels"

images = {
    os.path.splitext(f)[0]
    for f in os.listdir(image_dir)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
}

labels = {
    os.path.splitext(f)[0]
    for f in os.listdir(label_dir)
    if f.endswith(".txt")
}

print("Images :", len(images))
print("Labels :", len(labels))
print("Missing labels :", len(images - labels))
print("Extra labels :", len(labels - images))