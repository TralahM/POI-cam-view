#!/usr/bin/env python
"""Read Video capture properties."""
import cv2
import argparse


def decode_fourcc(fourcc):
    """Decode fourcc code."""
    fourcc_int = int(fourcc)
    print(f"Int value of fourcc: {fourcc_int}")
    return "".join([chr((fourcc_int >> 8 * i) & 0xFF) for i in range(4)])


def print_props(capture):
    """Print props of video capture."""
    # Get and print these values:
    print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(
        capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print(
        "CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(
            capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )
    print("CAP_PROP_FPS : '{}'".format(capture.get(cv2.CAP_PROP_FPS)))
    print("CAP_PROP_POS_MSEC : '{}'".format(
        capture.get(cv2.CAP_PROP_POS_MSEC)))
    print("CAP_PROP_POS_FRAMES : '{}'".format(
        capture.get(cv2.CAP_PROP_POS_FRAMES)))
    print(
        "CAP_PROP_FOURCC  : '{}'".format(
            decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC))
        )
    )
    print("CAP_PROP_FRAME_COUNT  : '{}'".format(
        capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("CAP_PROP_MODE : '{}'".format(capture.get(cv2.CAP_PROP_MODE)))
    print("CAP_PROP_BRIGHTNESS : '{}'".format(
        capture.get(cv2.CAP_PROP_BRIGHTNESS)))
    print("CAP_PROP_CONTRAST : '{}'".format(
        capture.get(cv2.CAP_PROP_CONTRAST)))
    print("CAP_PROP_SATURATION : '{}'".format(
        capture.get(cv2.CAP_PROP_SATURATION)))
    print("CAP_PROP_HUE : '{}'".format(capture.get(cv2.CAP_PROP_HUE)))
    print("CAP_PROP_GAIN  : '{}'".format(capture.get(cv2.CAP_PROP_GAIN)))
    print("CAP_PROP_EXPOSURE : '{}'".format(
        capture.get(cv2.CAP_PROP_EXPOSURE)))
    print("CAP_PROP_CONVERT_RGB : '{}'".format(
        capture.get(cv2.CAP_PROP_CONVERT_RGB)))
    print(
        "CAP_PROP_RECTIFICATION : '{}'".format(
            capture.get(cv2.CAP_PROP_RECTIFICATION))
    )
    print("CAP_PROP_ISO_SPEED : '{}'".format(
        capture.get(cv2.CAP_PROP_ISO_SPEED)))
    print("CAP_PROP_BUFFERSIZE : '{}'".format(
        capture.get(cv2.CAP_PROP_BUFFERSIZE)))


def main():
    """Run main."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        action="store",
        help="The Image to detect the faces.",
        default=None,
    )
    args = parser.parse_args()
    video_capture = cv2.VideoCapture(args.filename)
    print_props(video_capture)


if __name__ == "__main__":
    main()
