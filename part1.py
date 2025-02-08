# pylint: disable=no-member
"""
This script captures video from the default camera and displays it in a window.
It allows the user to save frames by pressing the 's' key and quit the application by pressing the 'q' key.
Usage:
    Run the script and a window will open displaying the video feed from the camera.
    Press 's' to save the current frame as an image file.
    Press 'q' to quit the application.
"""
import cv2

#open the camera
cap = cv2.VideoCapture(0)
COUNTER = 1

while True:
    #capture the video frame by frame
    ret, frame = cap.read()

    if frame is None:
        print("Not available")
        break
    #resize the frame to 640x480
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow('Video', frame)

    #press s to save the frame
    if cv2.waitKey(1) & 0xFF == ord('s'):
        filename = f'image{COUNTER}.jpg'
        cv2.imwrite(filename, frame)
        COUNTER+=1
    #press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the camera and close the window
cap.release()
cv2.destroyAllWindows()
