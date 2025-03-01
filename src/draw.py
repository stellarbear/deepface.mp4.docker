import cv2
from typing import List, Tuple, Any, Dict

def highlight_face(
    img: Any,
    face: Dict[str, int],
    text: str,
):
    color = (0, 0, 255)

    cv2.rectangle(
        img=img, 
        pt1=(face["x"], face["y"]), 
        pt2=(face["x"] + face["w"], face["y"] + face["h"]), 
        color=color, 
        thickness=2
    )

    thickness = 1
    font_scale = 1
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    (_, label_height), _ = cv2.getTextSize(text, font_face, font_scale, thickness) 
    for i, line in enumerate(text.split('\n')):
        y = face["y"] + face["h"] + (i + 1)*(label_height + 2)
        cv2.putText(img, line, (face["x"], y), font_face, font_scale, color, thickness)

    return img