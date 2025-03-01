import os
import glob 
import cv2
import tqdm 

from pathlib import Path
from deepface import DeepFace
from draw import highlight_face

os.environ["DEEPFACE_HOME"] = "./models"
skip_frame = int(os.environ.get("DEEPFACE_SKIP_FRAME", "10"))
detector = int(os.environ.get("DEEPFACE_DETECTOR", "opencv"))

files = glob.glob("./volume/input/*.mp4")

for file in os.scandir("./volume/output/"):
    if not file.name.endswith(".gitkeep"):
        os.unlink(file.path)

for file in files:
    print(f"Processing {file}...")

    video_capture = cv2.VideoCapture(file)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    video_writer = cv2.VideoWriter(
        f"./volume/output/{Path(file).stem}.mp4", 
        cv2.VideoWriter_fourcc(*"mp4v"), 
        fps, 
        (width, height)
    )
    \
    cache_result = []
    for i in tqdm.tqdm(range(int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)))):
        has_frame, img = video_capture.read()

        if not has_frame:
            break

        img_raw = img.copy()
        img_bgr = cv2.cvtColor(img_raw, cv2.COLOR_RGB2BGR)
        
        result = DeepFace.analyze(
            img_path = img_bgr, 
            actions = ['age', 'gender', 'emotion'],
            enforce_detection=False,
            detector_backend=detector
            silent=True
        ) if (i % skip_frame == 0) else cache_result
        cache_result = result

        for option in result:
            age = option["age"]
            gender = option["dominant_gender"]
            emotion = option["dominant_emotion"]
            
            text = f"{age}\n{gender}\n{emotion}"

            img_raw = highlight_face(
                img_raw, 
                option["region"],
                text
            )
        
        video_writer.write(img_raw)
        with open(f"./volume/output/{Path(file).stem}.txt", "a") as f:
            f.write(f"{age} {gender} {emotion}\n")

    video_capture.release()
    video_writer.release()