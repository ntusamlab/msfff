# minimizedsupportfff


## Project Title
Novel Fused Filament Fabrication System for Additive Manufacturing with Minimized Support Structures
<br />
<br />
## Project Description
The algorithm can modify the G-code to cooperate with the discrete platform, which includes support-eliminating, path-rearranging, and adding the lifting motions.
<br />
<br />
## File List and Descriptions
CAD_files:
| Name | Description |
| --- | --- |
| CAD_files | the whole model used in the program |
| fan_holder | the extruder module |
| modules | the servo and other ready-made parts |
| plane_unit | the part of the platform |
| ladder/bridge/blade | the part of case study |
| code | the whole code in algorithm |
| test_main | main program to modify g-code |
| test_3dprint_arduino | program to start the printing and communicate with printer |
| test_platform_raise_correction | correction g-code before printing |
| requirements | library for python |
| module | all functions required |
| test_table | database of the experiment |
<br />
<br />
## Steps 
steps in order to run the code. 
1. please start from downloading or cloning the repository and all the way to run the code with required input data
2. use Cura to slice the stl. file and save the result into the 'gcode_cura'
3. run 'test_main.py' to modify the g-code and the result will automatically saved into 'test_output'
4. put the modified g-code into the SD card and set it into the printer
5. run 'test_3dprint_arduino.py' to start printing
6. The printer will pause as the platform is going to be lifted
7. after printing, the total time and support time will be shown
