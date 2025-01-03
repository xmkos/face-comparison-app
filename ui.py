import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox, QProgressBar
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from comparison import FaceComparison

class FaceComparisonThread(QThread):
    # Signal to update progress
    progress_updated = pyqtSignal(int)
    # Signal to indicate comparison is done
    comparison_done = pyqtSignal(object, str)

    def __init__(self, image_path1, image_path2, threshold):  # constructor
        super().__init__()
        self.image_path1 = image_path1
        self.image_path2 = image_path2
        self.threshold = threshold


    def run(self):
        # Perform face comparison in a separate thread to avoid problems with the UI ( without it I've had problems with the UI freezing)
        try:
            face_comparison = FaceComparison(self.image_path1, self.image_path2, self.threshold)
            face_comparison.progress_updated.connect(self.progress_updated.emit)
            similarity_score, result = face_comparison.compare_faces()
            self.comparison_done.emit(similarity_score, result)
        except Exception as e:
            self.comparison_done.emit(None, str(e))

class FaceComparisonUI(QWidget):

    def __init__(self):  # constructor
        super().__init__()
        self.initUI()
        self.image_path1 = None
        self.image_path2 = None
        self.comparison_thread = None

    def initUI(self):
        # Initialize the UI components and layout
        self.setWindowTitle('Face Comparison')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('resources/app.png'))  # Set the window icon

        layout = QVBoxLayout()

        self.label1 = QLabel('Image 1: Not selected')
        self.label2 = QLabel('Image 2: Not selected')
        self.image_label1 = QLabel()
        self.image_label2 = QLabel()
        self.process_label = QLabel('Process: ')
        self.progress_bar = QProgressBar()

        self.btn_select_image1 = QPushButton('Select Image 1')
        self.btn_select_image2 = QPushButton('Select Image 2')
        self.btn_compare = QPushButton('Compare Faces')

        # Connect buttons to their respective functions
        self.btn_select_image1.clicked.connect(self.select_image1)
        self.btn_select_image2.clicked.connect(self.select_image2)
        self.btn_compare.clicked.connect(self.compare_faces)

        # Add widgets to the layout
        layout.addWidget(self.label1)
        layout.addWidget(self.image_label1)
        layout.addWidget(self.btn_select_image1)
        layout.addWidget(self.label2)
        layout.addWidget(self.image_label2)
        layout.addWidget(self.btn_select_image2)
        layout.addWidget(self.btn_compare)
        layout.addWidget(self.process_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def select_image1(self):
        # Open file dialog to select the first image
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image 1", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            self.image_path1 = file_name
            self.label1.setText(f'Image 1: {file_name}')
            pixmap = QPixmap(file_name)  # Show the selected image in the UI
            self.image_label1.setPixmap(pixmap.scaled(400, 300))

    def select_image2(self):
        # Open file dialog to select the second image
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image 2", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            self.image_path2 = file_name
            self.label2.setText(f'Image 2: {file_name}')
            pixmap = QPixmap(file_name)
            self.image_label2.setPixmap(pixmap.scaled(400, 300))

    def compare_faces(self):
        # Start the face comparison process
        if not self.image_path1 or not self.image_path2:
            QMessageBox.warning(self, "Warning", "Please select both images before comparing.")
            return

        self.process_label.setText('Process: Comparing faces...')
        self.progress_bar.setValue(0)

        # Create and start the comparison thread
        self.comparison_thread = FaceComparisonThread(self.image_path1, self.image_path2, threshold=0.6)
        self.comparison_thread.progress_updated.connect(self.update_progress)
        self.comparison_thread.comparison_done.connect(self.show_result)
        self.comparison_thread.start()

    def update_progress(self, value):
        # Update the progress bar value
        self.progress_bar.setValue(value)

    @pyqtSlot(object,str)  # decorator which validates the type of the arguments for the function
    def show_result(self, similarity_score, result):
        # Show the result in a message box
        if similarity_score is not None:
            QMessageBox.information(self, "Result", f'{result} (Similarity: {similarity_score * 100:.2f}%)')
            self.process_label.setText('Process: Complete')
        else:
            QMessageBox.warning(self, "Result", f'Error in face comparison: {result}')
            self.process_label.setText('Process: Error in running')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FaceComparisonUI()
    ex.show()
    sys.exit(app.exec_())
