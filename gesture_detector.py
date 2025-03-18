import cv2
import mediapipe as mp

# Module: Hand Gesture Detection
class HandGestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gesture(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        gesture = None
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                fingers = self.count_fingers(hand_landmarks)
                gesture = f"No.fingers {fingers}"
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return gesture

    def count_fingers(self, landmarks):
        tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
        fingers = 0

        # Check thumb separately (compare x-coordinates for left/right hand)
        if landmarks.landmark[tips[0]].x > landmarks.landmark[tips[0] - 1].x:
            fingers += 1  # Thumb is up

        # Check other four fingers (compare y-coordinates)
        for i in range(1, 5):  # Index to Pinky
            if landmarks.landmark[tips[i]].y < landmarks.landmark[tips[i] - 2].y:
                fingers += 1  # Finger is up

        return fingers

