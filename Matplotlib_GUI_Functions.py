import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


"""
DOCSTRING NOTES:
    The first function draws the graph on the sg Canvas object in PySimpleGUI.
    The second function deletes the MATPLOTLIB figure object.
    This is so matplotlib doesn't draw over previously created objects

"""


def draw_figure(canvas, figure):
    """Draws the figure for plotting into the GUI

    Inputs:
        canvas (PySimpleGui Object): The canvas to draw to in PySimpleGui
        figure (The matplotlib figure): The figure image, taken from the OR functions in other parts of the program

    Returns:
        The drawn figure which displays in the GUI"""

    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_figure_agg(figure_canvas_agg):
    """Deletes the current set of figures so that new figures can plot properly in the App

    Inputs: the current drawn figure held in memory
    Returns: None
    """

    figure_canvas_agg.get_tk_widget().forget()
    plt.close('all')

print("Matplotlib Interface Functions are Uploaded")