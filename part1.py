import cv2

#open the camera
cap = cv2.VideoCapture(0)
counter = 1

while True:
    #capture the video frame by frame
    ret, frame = cap.read()

    #resize the frame to 640x480
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow('Video', frame)

    #press s to save the frame
    if cv2.waitKey(1) & 0xFF == ord('s'):
        filename = f'image{counter}.jpg'
        cv2.imwrite(filename, frame)
        counter += 1
        
    #press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the camera and close the window
cap.release()
cv2.destroyAllWindows()
