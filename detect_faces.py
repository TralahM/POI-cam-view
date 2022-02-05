#!/usr/bin/env python
"""Detect Faces using Computer Vision."""
import cv2
import argparse


def detect_faces(frame, file_decorator="admin.png"):
    """Detect faces."""
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    targ_img = cv2.imread(file_decorator, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    for (x, y, w, h) in faces:
        x_offset = x
        y_offset = y
        new_targ = cv2.resize(targ_img, (int(w * 1.1), int(h * 1.1)))
        for c in range(0, 3):
            frame[
                y_offset: y_offset + new_targ.shape[0],
                x_offset: x_offset + new_targ.shape[1],
                c,
            ] = (
                new_targ[:, :, c] * (new_targ[:, :, 3] / 255.0)
                + frame[
                    y_offset: y_offset + new_targ.shape[0],
                    x_offset: x_offset + new_targ.shape[1],
                    c,
                ]
                * (1.0 - new_targ[:, :, 3] / 255.0)
            )

    cv2.imshow("Video", frame)


def main():
    """Run main program."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w --webcam",
        action="store_true",
        dest="webcam",
        help="Use the Webcam instead.",
        default=False,
    )
    parser.add_argument(
        "-f --filename",
        action="store",
        dest="filename",
        help="The Image to detect the faces.",
        default=None,
    )
    args = parser.parse_args()
    if args.webcam:
        print("webcam")
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            detect_faces(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print(f"image: {args.filename}")
        frame = cv2.imread(args.filename, -1)
        while True:
            detect_faces(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
