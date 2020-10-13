import cv2
import os

input_name = "sample_4.mp4"
resolution = [(320, 240), (480, 352), (640, 480), (960, 720), (1120, 832)]  # width, height

for res in resolution:
    print(res)
    output_name = str(res) + "_" + input_name
    video = cv2.VideoCapture(input_name)
    FPS = int(round(video.get(cv2.CAP_PROP_FPS), 0))
    width = video.get(3)
    height = video.get(4)

    if not video.isOpened():
        print("Could not open")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_name, fourcc, FPS, res)

    while True:
        ret, frame = video.read()
        if ret:
            frame = cv2.resize(frame, res)

            # Display the resulting frame
            out.write(frame)
        else:
            break

    # When everything done, release the capture
    video.release()
    out.release()
cv2.destroyAllWindows()
