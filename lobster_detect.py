# importing libraries
import cv2
import numpy as np
import time

carapace = [270, 320, 270, 268, 268, 294, 325, 322, 296, 254, 286, 289, 304, 297, 303, 268, 282, 272, 281, 307]

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('runs/detect/exp2/project_done.avi')

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):
    for x in range(len(carapace)):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            print("Detected Carapace Lenght: ", carapace[x], "mm")
            cv2.waitKey(500)
            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()