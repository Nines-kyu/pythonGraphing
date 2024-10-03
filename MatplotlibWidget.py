import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a Matplotlib figure and axis
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Create layout and add widgets
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)

        # Initial plot
        self.update_plot([], [], 'Line Plot')

    def update_plot(self, x, y, plot_type):
        # Clear the previous plot
        self.ax.clear()

        color = '#fb9111'

        # Plot new data based on selected type
        if plot_type == 'Line Plot':
            self.ax.plot(x, y, marker='o', color=color)
        elif plot_type == 'Bar Chart':
            self.ax.bar(x, y, color=color)
        elif plot_type == 'Scatter Plot':
            self.ax.scatter(x, y, color=color)
        elif plot_type == 'Histogram':
            self.ax.hist(y, bins=10, color=color)
        elif plot_type == 'Pie Chart':
            self.ax.pie(y, labels=x, autopct='%1.1f%%', startangle=140, colors=[color])
        elif plot_type == 'Box Plot':
            self.ax.boxplot([y], tick_labels=['Box Plot'], boxprops=dict(color=color))

        # Set titles and labels
        self.ax.set_title(f'{plot_type}')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')

        # Redraw the canvas
        self.canvas.draw()

    def show_error(self, message):
        # Clear the previous plot and show error message
        self.ax.clear()
        self.ax.text(0.5, 0.5, message, ha='center', va='center')
        self.canvas.draw()
