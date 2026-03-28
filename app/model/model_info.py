from ultralytics import YOLO

model = YOLO("/Users/namgungmyeongsu/Desktop/프로젝트/sch/25-1/임베디드/embedded_project/app/model/best8.pt")

model.info()
print("Classes:", model.names)