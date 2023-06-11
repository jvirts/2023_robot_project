# 2023_robot_project
Arduino / rpi robot repository and experiment results

This is a repository describing a simple robot build using arduino and raspberry pi along with a tracked vehicle robot chassis with brushed DC motors.  
See the .odt file (readable using LibreOffice Writer) for some details, also see the .dia file (readable using dia, an open source drawing tool) for how 
the connections were made.

The initial version of the dia diagram leaves out the HMC5883L electronic compass.
One of the goals of the project is to command the robot to turn a specified number of degrees.  Many of the initial experiments involve trying to calibrate 
the compass.  What I found is that the x axis variable was the only one which varied on the compass
