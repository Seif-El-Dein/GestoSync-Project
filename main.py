import sys
import cv2
import datetime
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import QTimer, QSize
from google_drive_uploader import GoogleDriveUploader
from camera import ImageCapture
from gesture_detector import HandGestureDetector
from GestoSync_UI import UI_GestoSync

# Main Application
class GestoSync_App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UI_GestoSync()
        self.ui.setupUi(self)
        window = self.frameGeometry()
        window.moveCenter(self.screen().availableGeometry().center())


        # Handle unexpected errors
        sys.excepthook = lambda excType, excValue, _ : QMessageBox.critical(self, "Error", f"An unexpected error occurred:\n{excType.__name__}: {excValue}")


        self.detector = HandGestureDetector()
        self.capture = ImageCapture()
        self.uploader = GoogleDriveUploader()
        self.handle_buttons()

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def handle_buttons(self):
        # self.ui.firstRotateRightButton.clicked.connect(lambda: self.Handle_Rotate(Camera.FirstCamera, Camera.RotateRight))   # Rotate Right Button
        # self.ui.secondRotateRightButton.clicked.connect(lambda: self.Handle_Rotate(Camera.SecondCamera, Camera.RotateRight)) # Rotate Right Button
        # self.ui.firstRotateLeftButton.clicked.connect(lambda: self.Handle_Rotate(Camera.FirstCamera, Camera.RotateLeft))     # Rotate Left Button
        # self.ui.secondRotateLeftButton.clicked.connect(lambda: self.Handle_Rotate(Camera.SecondCamera, Camera.RotateLeft))   # Rotate Left Button
        # self.ui.firstMirrorButton.clicked.connect(lambda: self.Handle_Rotate(Camera.FirstCamera, Camera.Mirror))             # Mirror Button
        # self.ui.secondMirrorButton.clicked.connect(lambda: self.Handle_Rotate(Camera.SecondCamera, Camera.Mirror))           # Mirror Button
        # self.ui.firstToggleButton.clicked.connect(lambda: self.Handle_Toggle(Camera.FirstCamera))                            # Toggle Camera
        # self.ui.secondToggleButton.clicked.connect(lambda: self.Handle_Toggle(Camera.SecondCamera))                          # Toggle Camera
        # self.ui.file_name_edit.textChanged.connect(self.Handle_Text)                                                       # Text Edit Change
        self.ui.capture_button.clicked.connect(self.capture_and_upload)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            gesture = self.detector.detect_gesture(frame)
            if gesture:
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            qimg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
            self.ui.firstCameraLabel.setPixmap(QPixmap.fromImage(qimg))

    def capture_and_upload(self):
        ret, frame = self.cap.read()
        if ret:
            gesture = self.detector.detect_gesture(frame)
            if gesture:
                file_path = self.capture.save_image(frame, gesture)
                self.uploader.upload_file(file_path, folder_id="1DGtEIkPdXw5sBnGW79uZGMVHoJ8EzIti")
                print(f"Uploaded {file_path} to Google Drive.")
                msg_box = QMessageBox()
                icon = QIcon()
                icon.addFile(u":/Labels/GestoSync.ico", QSize(), QIcon.Normal, QIcon.Off)
                msg_box.setWindowIcon(icon)
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Upload Successful")
                msg_box.setText(f"File '{file_path}' has been uploaded to google drive at {datetime.datetime.now()}!")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GestoSync_App().show()
    app.exec()
