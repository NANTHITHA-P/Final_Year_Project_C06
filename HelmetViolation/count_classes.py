import os

labels_dir = "FinalDataset/train/labels"

count = {0: 0, 1: 0}

for file in os.listdir(labels_dir):
    if not file.endswith(".txt"):
        continue

    with open(os.path.join(labels_dir, file), "r") as f:
        for line in f:
            line = line.strip()
            if line:
                cls = int(line.split()[0])
                count[cls] += 1

print("\nTraining Dataset Class Distribution")
print("----------------------------------")
print("With Helmet    :", count[0])
print("Without Helmet :", count[1])
print("Total Objects  :", count[0] + count[1])