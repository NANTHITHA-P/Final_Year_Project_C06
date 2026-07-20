import os

labels_dir = "FinalDataset/train/labels"

valid = 0
invalid = 0
empty = 0

for file in os.listdir(labels_dir):
    if not file.endswith(".txt"):
        continue

    path = os.path.join(labels_dir, file)

    with open(path) as f:
        lines = f.readlines()

    if len(lines) == 0:
        empty += 1
        continue

    ok = True

    for line in lines:
        parts = line.strip().split()

        if len(parts) != 5:
            ok = False
            break

        try:
            cls = int(parts[0])
            coords = list(map(float, parts[1:]))
        except:
            ok = False
            break

    if ok:
        valid += 1
    else:
        invalid += 1

print("Valid labels :", valid)
print("Invalid labels :", invalid)
print("Empty labels :", empty)