import PySimpleGUI as sg
import config

from GUI_Layout import make_window
from Generate_Random_Networks_Functions import generate_center_out_network, generate_network_from_two_points
from Matplotlib_GUI_Functions import draw_figure, delete_figure_agg
from Read_In_CSV_Network import network_from_xy_csv
from Reliability_Analysis_Functions import average_network_durability
from text_reports import text_report_reliability, text_report


def main():
    """ This function creates the gui window and pulls all the previously defined functions created previously to
    operate the user interface. Allowing the DSS to function.

    Input:
        make_window(sg.theme())(function): Allows gui to open and operate
        functions defined above (functions): Internal functions for the DSS
    Returns:
        Functioning DSS
    """

    # initialize output variables here
    figure_canvas_agg = None
    figure_canvas_agg2 = None
    window = make_window(config.theme)

    while True:
        event, values = window.read()

        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

        elif event == "-UploadAndRunAnalysis1-":

            # ** IMPORTANT ** Clean up previous drawing before drawing again
            if figure_canvas_agg:
                delete_figure_agg(figure_canvas_agg)
            if figure_canvas_agg2:
                delete_figure_agg(figure_canvas_agg2)

            try:
                file = values[2]
                comms_range = config.range_dictionary[values[3]]

                G, X, Y, figure_canvas_agg = network_from_xy_csv(file, comms_range)
                figure_canvas_agg2 = text_report(G)

                figure_canvas_agg = draw_figure(window['-CANVAS1a-'].TKCanvas, figure_canvas_agg)
                figure_canvas_agg2 = draw_figure(window['-CANVAS1b-'].TKCanvas, figure_canvas_agg2)

            except KeyError:
                sg.popup("Error: Check to make sure all your parameters are filled out", keep_on_top=True)
                pass
            except:  #all other errors.  I acknowledge this is considered bad practice
                sg.popup("Error: Check to make you you selected the correct CSV file.",
                         "The real-world sensor network location report is produced in the correct x-coord, y-coord format",
                         "So it will work if you select the correct CSV.",
                         keep_on_top=True)
                pass

        elif event == "-AirborneAnalysis2-":
            if figure_canvas_agg:
                delete_figure_agg(figure_canvas_agg)
            if figure_canvas_agg2:
                delete_figure_agg(figure_canvas_agg2)

            try:
                left_point = config.orientation_dictionary[values[5]][0]
                right_point = config.orientation_dictionary[values[5]][1]
                num_sensors = values[6]
                comms_range = config.range_dictionary[values[7]]

                G, X, Y, figure_canvas_agg = generate_network_from_two_points(left_point, right_point,
                                                                              comms_range, max_num_sensors=num_sensors)
                figure_canvas_agg2 = text_report(G)

                figure_canvas_agg = draw_figure(window['-CANVAS2a-'].TKCanvas, figure_canvas_agg)
                figure_canvas_agg2 = draw_figure(window['-CANVAS2b-'].TKCanvas, figure_canvas_agg2)

            except:  #all other errors.  I acknowledge this is considered bad practice
                sg.popup("Error: Check to make sure all your parameters are filled out", keep_on_top=True)
                pass

        elif event == "-ArtilleryAnalysis3-":
            if figure_canvas_agg:
                delete_figure_agg(figure_canvas_agg)
            if figure_canvas_agg2:
                delete_figure_agg(figure_canvas_agg2)

            try:
                nodes = values[9]
                comms_range = config.range_dictionary[values[10]]

                G, X, Y, figure_canvas_agg = generate_center_out_network(nodes, comms_range)
                figure_canvas_agg2 = text_report(G)

                figure_canvas_agg = draw_figure(window['-CANVAS3a-'].TKCanvas, figure_canvas_agg)
                figure_canvas_agg2 = draw_figure(window['-CANVAS3b-'].TKCanvas, figure_canvas_agg2)

            except:  #all other errors.  I acknowledge this is considered bad practice
                sg.popup("Error: Check to make sure all your parameters are filled out", keep_on_top=True)
                pass

        elif event == "-ReliabilityAnalysis4-":
            if figure_canvas_agg:
                delete_figure_agg(figure_canvas_agg)
            if figure_canvas_agg2:
                delete_figure_agg(figure_canvas_agg2)

            try:
                network = G
                survivability = 100 - values[13] * 100
                days = values[14]
                replications = values[12]

                mean, lower_bound, upper_bound, figure_canvas_agg = average_network_durability(network, survivability,
                                                                                               days, replications)
                figure_canvas_agg2 = text_report_reliability(G, mean, lower_bound, upper_bound)

                figure_canvas_agg = draw_figure(window['-CANVAS4a-'].TKCanvas, figure_canvas_agg)
                figure_canvas_agg2 = draw_figure(window['-CANVAS4b-'].TKCanvas, figure_canvas_agg2)

            except UnboundLocalError:
                sg.popup("Error: There is no network to analyze.",
                         "Upload or generate a network first in the appropriate tab.", keep_on_top=True)
                pass

            except (KeyError, TypeError):
                sg.popup("Error: Check to make sure all your parameters are filled out", keep_on_top=True)
                pass

        elif event == 'Display Instructions':
            sg.popup("Instructions:",
                     config.line1b,
                     config.line2b,
                     config.line3b,
                     config.line4b,
                     config.line5b, keep_on_top=True)
        elif event == 'About':
            sg.popup("About:",
                     config.line1a,
                     config.line2a,
                     config.line3a,
                     config.line4a,
                     config.line5a, keep_on_top=True)

        elif event == 'Sensors':
            sg.popup("Sensors:",
                     "Each sensor in the US inventory comes in one of three types",
                     "The Mk1 has a comms radius of 5km and a scan radius of 2.5km",
                     "The Mk2 has a comms radius of 10km and a scan radius of 5km",
                     "The Mk3 has a comms radius of 15km and a scan radius of 7.5km",
                     "Because the sensor scan radius is one-half the comms radius, the enemy cannot pass undectected "
                     "between any connected sensors. "
                     "We additionally leverage this fact to define network reliability.  "
                     "The network goes from reliable to unreliable when the network is no longer connected.  "
                     "This is the moment that enemy can maneuver undetected THROUGH our sensor network.",
                     keep_on_top=True)
        elif event == '-NoReliabilityGraph-':
            sg.popup("The inputed graph is already not connected.",
                     "Please generate another graph before attempting to run an analysis.",
                     keep_on_top=True)

        elif event == 'Instructions':
            sg.popup("Instructions:",
                     config.line1b,
                     config.line2b,
                     config.line3b,
                     config.line4b,
                     config.line5b, keep_on_top=True)

    window.close()
    exit(0)


main()
