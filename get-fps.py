# Code is adapted from https://www.learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/
import cv2

video_path = './sample.mp4'

capture = cv2.VideoCapture(video_path)

(major_ver, minor_ver, subminor_ver) = (cv2.__version__.split('.'))

if int(major_ver) < 3:
    fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else:
    fps = capture.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

capture.release()
