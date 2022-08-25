# DSS_Project_APP
Stochastic Network Analyzer Application


Welcome!

We assume that:

1) You have anaconda installed on your system and are familiar with it's use.
2) You have already extracted the files from the zip folder because you are reading this readme file.

########## Instructions to get the program running ######################

So let's get started.  Please follow the following steps:

1) Use the environment manager in the anaconda navigator to install necessary 
packages for Network Visualization DSS to function if you don't have them already:

matplotlib
networkx
numpy
pandas
pysimplegui
scipy
seaborn
statsmodels

2) Check to ensure that all files extracted from .zip folder remain in the same directory (i.e. folder) within local files.

3) Ensure that environment containing necessary dependencies is activated.

4) Launch Jupyter Notebook.

5) Using Jupyter Notebook, navigate to and open 'Network_Visualizer.ipynb".

6) Run all of the cells in the notebook.  This is best done by clicking "cell" in the menu bar and selecting "Run All Cells"

You should now be running the program!

############################# Instructions for using the program ###############################

Instructions are embedded into the application.  They can reached from the Menu Bar -> Help -> Instructions or 
by right clicking within the application.  

Once the interface is open, navigate through tabs to your preferred network generation method.  
	If you have a .csv from an existing network, go to the network input tab to upload the file. 
	if you want to conduct hypothetical analysis on a to be deployed network, go to the appropriate tab by title.

After you have either uploaded a network or generated a hypothetical one, you can conduct a reliability analysis by going to the 
reliability analysis tab.

All tabs have dropdown list inputs.  As long as all inputs on each tab is selected with a value, 
clicking the run button on the bottom left side will produce the desired output.  

Error messages, if they occur, will guide you to functionality with corrective and easy-to-understand instructions.

Furthermore, instructions are embedded into the application.  They can reached from the Menu Bar -> Help -> Instructions or 
by right clicking within the application.  

Also in the help section of the menu bar is the about page and a page about the sensors modeled in this program.

To test the functionality of creating a network from a CSV file, we provided 3 sample files.  
The user may choose to use any of the the example CSV files provided with the visualizer.

########################## Known python and package versions that work   ##############################

In the unlikely case that the versions of the packages you're running conflict with each other and cause instability, 
we've included the versions of everything you need that is known to work together.

python version:
  - python=3.8.13=hcf16a7b_0_cpython

dependency versions:
  - matplotlib-base=3.5.3=py38he529843_0
  - networkx=2.8.5=pyhd8ed1ab_0
  - numpy=1.23.1=py38h223ccf5_0
  - pandas=1.4.3=py38hcc40339_0
  - pysimplegui=4.60.3=pyhd8ed1ab_0
  - scipy=1.9.0=py38h91810f7_0
  - seaborn=0.11.2=hd8ed1ab_0
  - seaborn-base=0.11.2=pyhd8ed1ab_0
  - statsmodels=0.13.2=py38hbdcd294_0
