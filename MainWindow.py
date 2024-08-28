from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox
from MatplotlibWidget import MatplotlibWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Create the Matplotlib widget
        self.matplotlib_widget = MatplotlibWidget()
        self.layout.addWidget(self.matplotlib_widget)

        # Create input fields and button
        self.input_layout = QFormLayout()
        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.plot_button = QPushButton('Update Plot')

        # Create a dropdown menu for plot types
        self.plot_type_combo = QComboBox()
        self.plot_type_combo.addItems(['Line Plot', 'Bar Chart', 'Scatter Plot', 'Histogram', 'Pie Chart', 'Box Plot'])

        self.input_layout.addRow('X Values (comma-separated):', self.x_input)
        self.input_layout.addRow('Y Values (comma-separated):', self.y_input)
        self.input_layout.addRow('Plot Type:', self.plot_type_combo)
        self.input_layout.addWidget(self.plot_button)

        self.layout.addLayout(self.input_layout)

        # Connect button click event
        self.plot_button.clicked.connect(self.update_plot)

    def update_plot(self):
        # Get user input
        x_values = self.x_input.text()
        y_values = self.y_input.text()
        plot_type = self.plot_type_combo.currentText()

        try:
            # Convert input to lists of floats
            x = list(map(float, x_values.split(',')))
            y = list(map(float, y_values.split(',')))

            # Update the plot with user-specified type and color
            self.matplotlib_widget.update_plot(x, y, plot_type)

        except ValueError:
            self.matplotlib_widget.show_error('Invalid input')
