import cv2 as cv
import time
import os

class ImageCapture():
    def __init__(self):
        # Reading Video from Camera
        self.capture = cv.VideoCapture(0)

        # If camera fails to load
        if not self.capture.isOpened():
            print("Error: Could not open camera.")
            exit()

    def capture_image(self):
        time.sleep(1)

        # Start the time
        start_time = time.time()

        while True:
            # Capture frame-by-frame
            ret, frame = self.capture.read()

            # If failed to capture image
            if not ret:
                print("Error: Could not capture image.")
                exit()

            # Display the resulting frame
            cv.imshow("Camera", frame)

            # After 3 seconds have passed
            if time.time() - start_time >= 3:
                # Resize the image 224x224
                resized_image = cv.resize(frame, (224, 224))

                # Save the image
                cv.imwrite("attendance_image.jpg", resized_image)
                print("Image saved!")

                break

            # Break when pressed 'b'
            if cv.waitKey(1) & 0xFF==ord('b'):
                break

        self.capture.release()
        cv.destroyAllWindows()


# Create class instance
image_capture = ImageCapture()
# Capture the image
image_capture.capture_image()

