import PySimpleGUI as sg
import config


def make_window(theme):
    """This function proceeds in the following steps:
        1. Define the Menu Bar
        2. Define each tab.
        3. Within each tab, define the left side (input), right side(output) and then put them together.
        4. Define the Tab Groups
        5. Puts all the steps together and makes the window.

        Inputs:
            theme (sg.theme object): The thematic design choices of GUI Window colors and boxes

        Returns:
            window (sg.window object): The GUI window

        """

    # top of the program frame
#theme = sg.theme(config.theme)
    menu_def = [['&Application', ['&Exit']],
                ['&Help', ['&About', '&Sensors', '&Instructions']]]
    right_click_menu_def = [[], ['Display Instructions']]

    # Opening Tab
    start_left = [
        [sg.Text('Stochastically Placed Sensor Network Analyzer', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Image("Network-PNG-Transparent.png", size=(450, 450))]]

    start_right = [
        [sg.Text("About this Program", expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text(config.home_page_message, size=(40, 11),
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text("Access Instructions Anywhere", size=(40, 1), justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text(config.simple_instructions, size=(40, 4),
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)]]

    start_layout = [
        [sg.Col(start_left), sg.VerticalSeparator(), sg.Col(start_right)]]

    # Data Input Tab
    data_input_left = [
        [sg.Text('Existing Network Input', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text("Select your .CSV File: ", key="-FileInput1-"), sg.Input(size=(23, 1)), sg.FileBrowse()],
        [sg.Text("Select the sensor Comms Range: ", key="-CommsRange1-"), sg.Combo(config.rangelist)],
        [sg.Button("Generate and Run Analysis", key="-UploadAndRunAnalysis1-")]]

    data_input_right = [
        [sg.Text('Data Display', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Canvas(size=(600, 600), key='-CANVAS1a-')],
        [sg.Canvas(size=(600, 600), key='-CANVAS1b-')]]

    data_input_layout = [
        [sg.Col(data_input_left, p=10), sg.VerticalSeparator(), sg.Col(data_input_right, p=10)]]

    # Generate Random Network Airborne Tab
    gen_rand_left_airborne = [
        [sg.Text('Network Parameters for Random Generation', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text("Select the Deployment Orientation: ", key="-StartPoint2-"), sg.Combo(config.orientationlist)],
        [sg.Text("Select the Number of Sensors: ", key="-NumberSensors2-"), sg.Combo(config.num_sensors)],
        [sg.Text("Select the sensor Comms Range: ", key="-CommsRange2-"), sg.Combo(config.rangelist)],
        [sg.Button("Generate and Run Analysis", key="-AirborneAnalysis2-")]]

    gen_rand_right_airborne = [
        [sg.Text('Data Display', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Canvas(size=(config.figure_w, config.figure_h), key='-CANVAS2a-')],
        [sg.Canvas(size=(config.figure_w, config.figure_h), key='-CANVAS2b-')]]

    gen_rand_network_layout_airborne = [
        [sg.Col(gen_rand_left_airborne, p=10), sg.VerticalSeparator(), sg.Col(gen_rand_right_airborne, p=10)]]

    # Generate Random Network Artillery Tab
    gen_rand_left_artillery = [
        [sg.Text('Network Parameters for Random Generation', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text("Select the Number of Sensors: ", key="-NumberSensors3-"), sg.Combo(config.num_sensors)],
        [sg.Text("Select the sensor Comms Range: ", key="-CommsRange3-"), sg.Combo(config.rangelist)],
        [sg.Button("Generate and Run Analysis", key="-ArtilleryAnalysis3-")]]

    gen_rand_right_artillery = [
        [sg.Text('Data Display', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Canvas(size=(config.figure_w, config.figure_h), key='-CANVAS3a-')],  # where the MATPLOTLIB draws to
        [sg.Canvas(size=(config.figure_w, config.figure_h), key='-CANVAS3b-')]]

    gen_rand_network_layout_artillery = [
        [sg.Col(gen_rand_left_artillery, p=10), sg.VerticalSeparator(), sg.Col(gen_rand_right_artillery, p=10)]]

    # Reliability Analysis Tab
    reliability_left = [
        [sg.Text('Parameters for Reliability Analysis', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Text("Select the Number of Runs: ", key="-NumberRuns4-"), sg.Combo(config.num_of_runs)],
        [sg.Text("Select the Failure Rate per Day: ", key="-FailureRate4-"), sg.Combo(config.failure_rate)],
        [sg.Text("Select the Maximum Number of Days to simulate: ", key="-MaxDays4-"), sg.Combo(config.num_sensors)],
        [sg.Button("Run Analysis", key="-ReliabilityAnalysis4-")]]

    reliability_right = [
        [sg.Text('Network Dis-Connectivity Histogram', expand_x=True, justification='center',
                 font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
        [sg.Canvas(size=(config.figure_w, config.figure_h), key='-CANVAS4a-')],  # where the MATPLOTLIB draws to
        [sg.Canvas(size=(config.figure_w, config.figure_h), key='-CANVAS4b-')],
        [sg.Button("Empty Graph?", key="-NoReliabilityGraph-")]]

    reliability_analysis_layout = [
        [sg.Col(reliability_left, p=10), sg.VerticalSeparator(), sg.Col(reliability_right, p=10)]]

    # Overall Layout
    layout = [
        [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)]]

    layout += [[sg.TabGroup([[sg.Tab('Start', start_layout,
                                     key="-StartTab-"),
                              sg.Tab('Existing Network Input', data_input_layout,
                                     key="-DataInputTab-"),
                              sg.Tab('Generate Random Network AIRBORNE', gen_rand_network_layout_airborne,
                                     key="-AirborneTab-"),
                              sg.Tab('Generate Random Network ARTILLERY', gen_rand_network_layout_artillery,
                                     key="-ArtilleryTab-"),
                              sg.Tab('Reliability Analysis', reliability_analysis_layout,
                                     key="-ReliabilityTab-"),
                              ]], key='-TAB GROUP-', expand_x=True, expand_y=True)]]

    window = sg.Window('Sensor Network Analyzer', layout, grab_anywhere=True, margins=(0, 0),
                       right_click_menu=right_click_menu_def,
                       use_custom_titlebar=True, finalize=True, size=(1000, 800), keep_on_top=False, resizable=True)

    return window


print("GUI Layout is Uploaded")
