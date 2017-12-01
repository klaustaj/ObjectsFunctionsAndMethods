"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Aaron Klaustermeier.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    circle1_center = rg.Point(300,150)
    circle1 = rg.Circle(circle1_center, 25)
    circle1.fill_color = 'green'

    circle2_center = rg.Point(75, 200)
    circle2 = rg.Circle(circle2_center, 50)

    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()

    circle_center = rg.Point(350,100)
    circle = rg.Circle(circle_center, 20)
    circle.fill_color = 'blue'

    point1 = rg.Point(100,200)
    point2 = rg.Point(200,250)
    rectangle = rg.Rectangle(point1,point2)

    circle.attach_to(window)
    rectangle.attach_to(window)
    window.render()

    print("circle outline thickness:", circle.outline_thickness)
    print("circle fill color:", circle.fill_color)
    print("circle center:", circle.center)
    print("circle center x:", circle_center.x)
    print("circle center y:", circle_center.y)

    print("rectangle outline thickness:", rectangle.outline_thickness)
    print("rectangle fill color:", rectangle.fill_color)
    rect_cent = rectangle.get_center()
    print("rectangle center:", rect_cent)
    print("rectangle center x:", rect_cent.x)
    print("rectangle center y:", rect_cent.y)


    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    endpoint1_1 = rg.Point(0, 0)
    endpoint1_2 = rg.Point(300, 250)
    straight = rg.Line(endpoint1_1, endpoint1_2)

    endpoint2_1 = rg.Point(50, 200)
    endpoint2_2 = rg.Point(200, 200)
    also_straight = rg.Line(endpoint2_1, endpoint2_2)
    also_straight.thickness = 5

    mid = also_straight.get_midpoint()
    print('\nalso_straight midpoint:', mid)
    print('x coordinate of mid:', mid.x)
    print('y coordinate of mid:', mid.y)

    straight.attach_to(window)
    also_straight.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
