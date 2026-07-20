from ultralytics import YOLO

def main():
    model = YOLO("yolo11s.pt")

    model.train(
        data="FinalDataset/data.yaml",
        epochs=20,
        imgsz=640,
        batch=2,
        workers=0,
        device=0,
        amp=False,
        cache=False,
        project="outputs",
        name="helmet_final(last)",
        patience=20,
        save=True
    )

if __name__ == "__main__":
    main()