import face_recognition
import cv2
import numpy as np
import logging
from PyQt5.QtCore import QObject, pyqtSignal

class FaceComparison(QObject):
    # Signal to update progress ( to be used in the thread)
    progress_updated = pyqtSignal(int)

    def __init__(self, image_path1, image_path2, threshold):  # constructor
        super().__init__()
        self.image_path1 = image_path1
        self.image_path2 = image_path2
        self.image1 = self.load_and_preprocess_image(image_path1)
        self.image2 = self.load_and_preprocess_image(image_path2)
        self.face1 = None
        self.face2 = None
        self.features1 = None
        self.features2 = None
        self.threshold = threshold
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def resize_image(self, image, max_width=640, max_height=480):
        # Resize image to fit within max dimensions
        height, width, _ = image.shape
        aspect_ratio = width / height
        if width > max_width or height > max_height:
            if aspect_ratio > 1:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
            return cv2.resize(image, (new_width, new_height))
        return image

    def load_and_preprocess_image(self, image_path):
        # Load image from file, resize, convert color format
        try:
            image = face_recognition.load_image_file(image_path)
            image = self.resize_image(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image
        except Exception as e:
            logging.error(f"Error loading image {image_path}: {e}")
            raise


    def detect_face(self, image):
        # Detect first face in the image and return its coordinates
        face_locations = face_recognition.face_locations(image)
        if not face_locations:
            raise ValueError("No face found")
        logging.info(f"Detected face at: {face_locations[0]}")
        return face_locations[0]

    def extract_features(self, image, face_coordinates):
        # Extract facial features (encodings) from the detected face
        top, right, bottom, left = face_coordinates
        face_image = image[top:bottom, left:right]
        face_image = cv2.resize(face_image, (160, 160))
        face_encodings = face_recognition.face_encodings(face_image)
        if not face_encodings:
            raise ValueError("No face encodings found")
        else:
            logging.info(f"Extracted features: {face_encodings[0]}")
            return face_encodings[0]

    def calculate_similarity(self, feature_vector1, feature_vector2):
        # Calculate similarity score between two feature vectors according to Euclidean distance formula
        distance = np.linalg.norm(feature_vector1 - feature_vector2)
        similarity_score = 1 / (1 + distance)
        logging.info(f"Calculated similarity score: {similarity_score}")
        return similarity_score

    def interpret_similarity(self, similarity_score):
        # Interpret similarity score based on the threshold
        if similarity_score >= self.threshold:
            return "Faces are SIMILAR"
        else:
            return "Faces are DIFFERENT"

    def compare_faces(self):
        # Main method to compare two faces and return similarity score and result + error handling
        try:
            self.progress_updated.emit(10)
            self.face1 = self.detect_face(self.image1)
            self.progress_updated.emit(30)
        except ValueError as e:
            logging.error(f"Error detecting face in image 1: {e}")
            return None, f"Error detecting face in image 1: {e}"

        try:
            self.face2 = self.detect_face(self.image2)
            self.progress_updated.emit(50)
        except ValueError as e:
            logging.error(f"Error detecting face in image 2: {e}")
            return None, f"Error detecting face in image 2: {e}"

        try:
            self.features1 = self.extract_features(self.image1, self.face1)
            self.progress_updated.emit(70)
        except ValueError as e:
            logging.error(f"Error extracting features from face 1: {e}")
            return None, f"Error extracting features from face 1: {e}"

        try:
            self.features2 = self.extract_features(self.image2, self.face2)
            self.progress_updated.emit(90)
        except ValueError as e:
            logging.error(f"Error extracting features from face 2: {e}")
            return None, f"Error extracting features from face 2: {e}"

        try:
            similarity_score = self.calculate_similarity(self.features1, self.features2)
            result = self.interpret_similarity(similarity_score)
            self.progress_updated.emit(100)
            return similarity_score, result
        except Exception as e:
            logging.error(f"An error occurred during similarity calculation: {e}")
            return None, f"An error occurred during similarity calculation: {e}"