######################### Defining GUI parameters, listboxes to use, lengthy text ################

# splash screen description
line1a = "This program is for the E-4 type Intel Analyst who is maintaining the Sensor Network over a Named Area of " \
         "Interest(NAI). "
line2a = "There are two use cases.  The user either has an existing network that he can input via CSV and run " \
         "reliability analysis on. "
line3a = "Or, he has an NAI that is not covered in mind.  "
line4a = "He can then generate a hypothetical sensor network, deployed via airdrop or artillery.  "
line5a = "Then, he can run reliability analysis on it and experiment with the number of sensors and type deployed."
home_page_message = line1a + line2a + line3a + line4a + line5a

# General Instructions
line1b = "1. Click on the tab that describes what you want to do. "
line2b = "2. Input your data (as applicable) or define your network parameters and click the button below the " \
         "parameters. "
line3b = "3. View the output.  If reliability analysis is desired, click the reliability analysis tab.  Your current " \
         "network stays inputted into the program. "
line4b = "4. Input the parameters for reliability analysis and click the button below the parameters."
line5b = "5. Interpret the Analysis Graph and Report."
instructions_message = line1b + line2b + line3b + line4b + line5b

simple_instructions = "Right click anywhere to pull up application instructions.  Or click the help button on the " \
                      "top menu. "

# GUI style theme
theme = "brownblue"

# Size of MATPLOTLIB graphic in GUI
figure_w, figure_h = 800, 800

# Lists for Combo Boxes in GUI
rangelist = ["5km", "10km", "15km"]
num_sensors = [25, 50, 75, 100]
num_of_runs = [250, 500, 750, 1000]
failure_rate = [.05, .10, .15, .20]
orientationlist = ['Horizontal', 'Slanted up', 'Slanted down', 'Vertical']

# Dictionaries to translate 'str' user input to the proper parameters
range_dictionary = {"5km": 5, "10km": 10, "15km": 15}
orientation_dictionary = {'Horizontal': [[0, 0], [120, 1]],
                          'Slanted up': [[1, 1], [85, 85]],
                          'Vertical': [[1, 1], [5, 120]],
                          'Slanted down': [[1, 85], [85, 2]]}
