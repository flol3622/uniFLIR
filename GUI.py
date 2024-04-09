import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QSlider, QPushButton, QProgressBar, QHBoxLayout, QLineEdit
import matplotlib.pyplot as plt
from flir_image_extractor import FlirImageExtractor

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Processing App")
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.min_temp_label = QLabel("Minimum Temperature (°C):")
        layout.addWidget(self.min_temp_label)

        self.min_temp_layout = QHBoxLayout()
        layout.addLayout(self.min_temp_layout)

        self.min_temp_slider = QSlider(Qt.Horizontal)
        self.min_temp_slider.setMinimum(0)
        self.min_temp_slider.setMaximum(100)
        self.min_temp_slider.setTickInterval(5)
        self.min_temp_slider.setSingleStep(1)
        self.min_temp_slider.setValue(20)
        self.min_temp_slider.setTickPosition(QSlider.TicksBelow)
        self.min_temp_layout.addWidget(self.min_temp_slider)

        self.min_temp_line_edit = QLineEdit()
        self.min_temp_line_edit.setFixedWidth(50)
        self.min_temp_layout.addWidget(self.min_temp_line_edit)

        self.min_temp_line_edit.setText(str(self.min_temp_slider.value()))

        self.min_temp_line_edit.editingFinished.connect(self.update_min_temp_slider)

        self.min_temp_slider.valueChanged.connect(self.update_min_temp_line_edit)

        self.max_temp_label = QLabel("Maximum Temperature (°C):")
        layout.addWidget(self.max_temp_label)

        self.max_temp_layout = QHBoxLayout()
        layout.addLayout(self.max_temp_layout)

        self.max_temp_slider = QSlider(Qt.Horizontal)
        self.max_temp_slider.setMinimum(0)
        self.max_temp_slider.setMaximum(100)
        self.max_temp_slider.setTickInterval(5)
        self.max_temp_slider.setSingleStep(1)
        self.max_temp_slider.setValue(40)
        self.max_temp_slider.setTickPosition(QSlider.TicksBelow)
        self.max_temp_layout.addWidget(self.max_temp_slider)

        self.max_temp_line_edit = QLineEdit()
        self.max_temp_line_edit.setFixedWidth(50)
        self.max_temp_layout.addWidget(self.max_temp_line_edit)

        self.max_temp_line_edit.setText(str(self.max_temp_slider.value()))

        self.max_temp_line_edit.editingFinished.connect(self.update_max_temp_slider)

        self.max_temp_slider.valueChanged.connect(self.update_max_temp_line_edit)

        self.process_button = QPushButton("Process Images")
        self.process_button.clicked.connect(self.process_images)
        layout.addWidget(self.process_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        layout.addWidget(self.progress_bar)

    def update_min_temp_slider(self):
        value = float(self.min_temp_line_edit.text())
        if value >= 0 and value <= self.max_temp_slider.value():
            self.min_temp_slider.setValue(int(value * 2))

    def update_min_temp_line_edit(self):
        self.min_temp_line_edit.setText(str(self.min_temp_slider.value() / 2))

    def update_max_temp_slider(self):
        value = float(self.max_temp_line_edit.text())
        if value >= self.min_temp_slider.value() and value <= 100:
            self.max_temp_slider.setValue(int(value * 2))

    def update_max_temp_line_edit(self):
        self.max_temp_line_edit.setText(str(self.max_temp_slider.value() / 2))

    def process_images(self):
        self.process_button.setEnabled(False)
        self.process_button.setText("Processing...")
        QApplication.processEvents()  # Update GUI

        inFolder = "."
        outFolder = "out/"
        min_temp = self.min_temp_slider.value() / 2
        max_temp = self.max_temp_slider.value() / 2

        if not os.path.exists(outFolder):
            os.makedirs(outFolder)

        files = [filename for filename in os.listdir(inFolder) if filename.endswith(".jpg")]
        total_files = len(files)
        for index, filename in enumerate(files):
            filePath = os.path.join(inFolder, filename)
            raw = FlirImageExtractor()
            raw.process_image(filePath)
            thermal = raw.get_thermal_np()

            outPath = os.path.join(outFolder, filename)
            plt.imsave(outPath, thermal, cmap="plasma", vmin=min_temp, vmax=max_temp)

            remaining_files = total_files - (index + 1)
            progress = ((index + 1) / total_files) * 100
            self.progress_bar.setValue(progress)
            QApplication.processEvents()  # Update GUI
            print(f"Processed {filename}. Remaining files: {remaining_files}", end="\r")

        print("Processing complete.")
        self.process_button.setEnabled(True)
        self.process_button.setText("Process Images")

def main():
    app = QApplication(sys.argv)
    window = ImageProcessingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
