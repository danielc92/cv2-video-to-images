# Extract images from video
Pulling data from video files (images).

# Before you get started
- Basic Python (3.6.5)

# Setup
**How to obtain this repository:**
```sh
git clone 
```

**Environment**
- Python 3.6.5
- MacOS

**Modules/dependencies:**
- `cv2`

Install the following dependences:
```sh
pip install cv2
```

# Running
First get the frames per second of the video file.
```sh
python3 get-fps.py
```
Next, change settings in `get-images.py` with the frames value (int) gathered from `get-fps.py` and seconds interval and run.
```sh
python3 get-images.py
```
After this step, your images should be saved in image folder.

# Tests
- Calculating frame per second from video file
- Exporting image from `sample.mp4` every 2 seconds, using frames per second as an input

# Contributors
- Daniel Corcoran

# Sources
- [Capturing frames per second using cv2](https://www.learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/)
