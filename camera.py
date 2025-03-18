import time
import os
import cv2

# Module: Image Capture
class ImageCapture:
    def __init__(self, save_path="captured_images"):
        self.save_path = save_path
        os.makedirs(self.save_path, exist_ok=True)

    def save_image(self, frame, label):
        timestamp = int(time.time())
        filename = f"{self.save_path}/{label}_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        return filename
