"""
Model our creature and wrap it in one class.
First version on 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1

----------------------------------

Modified by Daniel Scrivener 09/2023
"""

from Component import Component
from Point import Point
import ColorType as Ct
from Shapes import Cube
from Shapes import Cylinder
import numpy as np


class ModelLinkage(Component):
    """
    Define our linkage model
    """

    ##### TODO 2: Model the Creature
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 
    #
    # In order to simplify the process of constructing your model, the rotational origin of each Shape has been offset by -1/2 * dz,
    # where dz is the total length of the shape along its z-axis. In other words, the rotational origin lies along the smallest 
    # local z-value rather than being at the translational origin, or the object's true center. 
    # 
    # This allows Shapes to rotate "at the joint" when chained together, much like segments of a limb. 
    #
    # In general, you should construct each component such that it is longest in its local z-direction: 
    # otherwise, rotations may not behave as expected.
    #
    # Please see Blackboard for an illustration of how this behavior works.

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        # Spider body: a central cube
        body = Cube(Point((0, 0, 0)), shaderProg, [1, 0.5, 0.5], Ct.NAVY)

        # Leg segments using link1, link2, link3, link4 structure
        legLength = 0.5
        legs = []
        for i in range(8):  # 8 legs
            base_pos = self.calculate_leg_position(i)  # Calculate position for each leg base
            link1 = Cube(Point(base_pos), shaderProg, [0.2, 0.2, legLength], Ct.BLUE)
            link2 = Cube(Point((0, 0, legLength)), shaderProg, [0.2, 0.2, legLength], Ct.SOFTBLUE)
            link3 = Cube(Point((0, 0, legLength)), shaderProg, [0.2, 0.2, legLength], Ct.CYAN)
            link4 = Cube(Point((0, 0, legLength)), shaderProg, [0.2, 0.2, legLength], Ct.CYAN)
            # Chain the leg links together
            link1.addChild(link2)
            link2.addChild(link3)
            link3.addChild(link4)

            # Attach leg to the body
            legs.append(link1)
            body.addChild(link1)

        # Adding body and legs to component list
        self.addChild(body)
        self.componentList = [body] + legs
        self.componentDict = {
            "body": body,
            **{f"leg{i+1}": legs[i] for i in range(8)}
        }
        ##### TODO 4: Define creature's joint behavior
        # Requirements:
        #   1. Set a reasonable rotation range for each joint,
        #      so that creature won't intersect itself or bend in unnatural ways
        #   2. Orientation of joint rotations for the left and right parts should mirror each other.

        # Define joint behaviors (rotation limits) for each link in the legs
        for i, leg in enumerate(legs):
            leg.setRotateExtent(leg.uAxis, -45, 45)  # First joint (link1)
            leg.children[0].setRotateExtent(leg.vAxis, -60, 60)  # Second joint (link2)
            leg.children[0].children[0].setRotateExtent(leg.wAxis, -60, 60)  # Third joint (link3)
            leg.children[0].children[0].children[0].setRotateExtent(leg.wAxis, -60, 60)  # Fourth joint (link4)

    def calculate_leg_position(self, leg_index):
        """
        Returns the calculated position for each leg based on its index.
        This method helps spread out the legs from the spider's body.
        """
        angle = (leg_index / 8) * 2 * np.pi  # Spread around in a circle
        x = np.cos(angle) * 0.5
        y = np.sin(angle) * 0.5
        return (x, y, 0)
