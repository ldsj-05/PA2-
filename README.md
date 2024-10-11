# PA2
Leah Jones 
I collaborated with my TA's
CS480 Programming Assignment 2

Sketch.py: Manages the OpenGL environment, user input, and rendering. It sets up the creature model and axis, handles user input , and allows going through 5  poses.
Component.py: Defines components for the creature, handling transformations like translation, rotation, and scaling.
ModelLinkage.py: Constructs the creature model with a central body and legs, defines joint behaviors, and sets rotation limits to ensure natural movement.

In the Interrupt_Keyboard() function, I added tried to add keyboard controls for switching between the predefined poses using keys 1 through 5, but errors kept poppint up. If functional,  the user presses one of these keys, the pose function is called to update the creature. Within each pose function, I used the setCurrentAngle() method to adjust the rotation angles of the creature's limbs (legs) based on the pose requirements. Additionally, I changed the color of the limbs to allow it to give of a more minecraft look I was going for. 
