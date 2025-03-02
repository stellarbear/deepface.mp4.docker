Run the [deepface](https://github.com/serengil/deepface/) in a Docker container against mp4 files.

## TLDR
```
./bin/run.sh
```
or
```
DEEPFACE_SKIP_FRAME=24 docker compose run deepface
```

## Step by step
### 1. Build python & deepface image (single run)
```
docker compose build --progress=plain
```

### 2. Prepare your files
Place all the files in the ```./volume/input/``` directory

### 3. Run the docker compose
```
docker compose run deepface
```
Configure defaults
```
DEEPFACE_DETECTOR=opencv DEEPFACE_SKIP_FRAME=1 docker compose run deepface
DEEPFACE_DETECTOR=retinaface DEEPFACE_SKIP_FRAME=24 docker compose run deepface
DEEPFACE_DETECTOR=mtcnn DEEPFACE_SKIP_FRAME=24 docker compose run deepface
```
| Argument    | Values | Defaults |
| -------- | ------- |------- |
| DEEPFACE_DETECTOR  | opencv, retinaface, mtcnn, ssd, dlib, mediapipe, yolov8, centerface [description](https://github.com/serengil/deepface#:~:text=its%20tutorial.-,Face%20Detection%20and%20Alignment,-%2D%20Demo)   |   opencv
| DEEPFACE_SKIP_FRAME | 1, 5, 24, etc (depends on the model)     |  10

### 4. Result
You can find the result in the ```./volume/output/``` directory

### 5. Local development
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/analyze.py
```