# Sample Camera Controller using OpenCV for USB camera
import cv2
import time

class CameraController:
    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)
        time.sleep(2)  # Allow the camera to initialize

    def capture_image(self):
        ret, frame = self.camera.read()
        return frame

    def release_camera(self):
        self.camera.release()

# Example usage
if __name__ == "__main__":
    camera = CameraController()

    while True:
        image = camera.capture_image()
        # Perform actions with the captured image
        cv2.imshow("Captured Image", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release_camera()
    cv2.destroyAllWindows()
