import os
import cv2
from facetracker import FaceTracker


facetracker = FaceTracker('scripts/yolov8n-face.pt')

video = cv2.VideoCapture('samples/mantissa.mov')

# video_out = cv2.VideoWriter('samples/mantissa_out.mov', cv2.VideoWriter_fourcc(*'mp4v'), 30, (int(video.get(3)), int(video.get(4))))

while True:
    ret, frame = video.read() 

    if not ret:
        break

    results = facetracker.track(frame, verbose=False)
    im = results[0].plot() 

    # video_out.write(im)

    for result in results:
        print(result.boxes)

# video.release()