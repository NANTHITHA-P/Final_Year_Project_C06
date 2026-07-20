import os

labels_dir = "FinalDataset/train/labels"

valid_images = 0
background_images = 0
invalid_boxes = 0

for file in os.listdir(labels_dir):
    if not file.endswith(".txt"):
        continue

    path = os.path.join(labels_dir, file)

    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]

    if not lines:
        background_images += 1
        continue

    ok = False

    for line in lines:
        parts = line.split()

        if len(parts) != 5:
            continue

        try:
            cls = int(parts[0])
            x, y, w, h = map(float, parts[1:])

            if cls not in [0, 1]:
                continue

            if not (0 <= x <= 1 and
                    0 <= y <= 1 and
                    0 < w <= 1 and
                    0 < h <= 1):
                continue

            ok = True

        except:
            continue

    if ok:
        valid_images += 1
    else:
        invalid_boxes += 1

print("Images with valid YOLO labels :", valid_images)
print("Background images             :", background_images)
print("Invalid label images          :", invalid_boxes)