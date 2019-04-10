# Imports
import cv2

capture = cv2.VideoCapture('./sample.mp4')

# Calculate how often to export frame to image
frames_per_second = 30
image_every_n_seconds = 2
multiplier = frames_per_second * image_every_n_seconds

currentFrame = 0

while(True):

    ret, frame = capture.read()

    # If frame doesnt exist break out of while loop
    if frame is None:
        break

    # Export image conditionally
    image_path = './image/frame' + str(currentFrame) + '.jpg'
    if currentFrame % multiplier == 0:
        print ('Exporting image to: ' + image_path)
        cv2.imwrite(image_path, frame)

    currentFrame += 1

capture.release()
cv2.destroyAllWindows()
