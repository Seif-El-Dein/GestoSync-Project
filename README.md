# GestoSync-Project Documentation

## Overview

**GestoSync** is an application designed to detect hand gestures using a webcam, capture images based on these gestures, and upload the captured images to a specified Google Drive folder. The application leverages computer vision and machine learning libraries to interpret hand movements and integrates with Google Drive for cloud storage.

## Features

- **Hand Gesture Detection**: Utilizes MediaPipe to recognize and interpret hand gestures in real-time.
- **Image Capture**: Captures images upon recognizing specific gestures.
- **Google Drive Integration**: Uploads captured images to a designated folder in Google Drive for easy access and sharing.

## Modules

The application is structured into several key modules:

1. **Hand Gesture Detection (`gesture_detector.py`)**:
   - **Purpose**: Detects and interprets hand gestures from the webcam feed.
   - **Key Components**:
     - `HandGestureDetector` class: Initializes MediaPipe's hand detection and provides methods to process frames and count raised fingers.

2. **Image Capture (`camera.py`)**:
   - **Purpose**: Captures and saves images when specific gestures are detected.
   - **Key Components**:
     - `ImageCapture` class: Manages the directory for storing images and handles the saving process with timestamps.

3. **Google Drive Uploader (`google_drive_uploader.py`)**:
   - **Purpose**: Manages authentication and uploads images to Google Drive.
   - **Key Components**:
     - `GoogleDriveUploader` class: Handles OAuth2 authentication and provides methods to upload files to a specified Google Drive folder.

4. **User Interface (`GestoSync_UI.py`)**:
   - **Purpose**: Provides a graphical user interface for user interaction.
   - **Key Components**:
     - `GestureSnapDrive` class: Extends `QMainWindow` to create the main application window, display the webcam feed, and handle user inputs.

5. **Main Application (`main.py`)**:
   - **Purpose**: Integrates all modules and runs the application.
   - **Key Components**:
     - Initializes the main window and starts the application loop.

## Setup and Installation

To set up the GestoSync application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Seif-El-Dein/GestoSync-Project.git
   cd GestoSync-Project
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Google Drive API**:
   - Obtain `client_secrets.json` from the Google Developer Console.
   - Place the `client_secrets.json` file in the project directory.

5. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

- **Launching the Application**: Run `main.py` to start the application. The main window will display the webcam feed.
- **Capturing Gestures**: The application detects hand gestures in real-time. Upon recognizing a gesture (e.g., showing a certain number of fingers), it captures an image.
- **Uploading to Google Drive**: Captured images are automatically uploaded to the specified Google Drive folder.

## Dependencies

- `opencv-python-headless`: For handling webcam input and image processing.
- `mediapipe`: For hand gesture recognition.
- `PySide6`: For creating the graphical user interface.
- `pydrive2`: For Google Drive integration and file uploads.

## Contributing

Contributions to GestoSync are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
