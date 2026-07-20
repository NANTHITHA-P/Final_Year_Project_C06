from ultralytics import YOLO

model = YOLO(r"E:\Final_Year_Project_C06\runs\detect\outputs\helmet_final(last)\weights\best.pt")

model.predict(
    source="videos",
    save=True,
    conf=0.4,
    show=True
)