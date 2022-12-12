import cv2
import numpy as np

name = "FinalSalad18"

cap = cv2.VideoCapture(name + ".mp4")

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

GTstates = []
frame_no = 0
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        frame = cv2.resize(frame, (960, 540))
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

        frame_no = frame_no + 1
        if frame_no % 50 == 0:
            cv2.destroyAllWindows()
            print("What was this guy handling?\n1 - nothing\n2 - banana\n3 - apple\n4 - orange\n5 - brocoli\n6 - carrot\n7 - knife")
            GTstate = input("Your answer: ")
            GTstates.append(int(GTstate))
            print(GTstates)

    # Break the loop
    else:
        break

np.array(GTstates)
numpy_name = name + "_GTstates.npy"
np.save(numpy_name, GTstates)

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()