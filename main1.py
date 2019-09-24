#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade

SCREEN_WIDTH = 640  #This is the width that the screen will be 
SCREEN_HEIGHT = 480 #This is the height that the screen will be 
SCREEN_TITLE = "Move Mouse Example" #This is the title of the program

    #Class allows for the object which is the ball to run in the program
class Ball:
    def __init__(self, position_x, position_y, radius, color):
        # These put the ball in a certain position and they make the ball a certain size and color

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
    #This draws the ball in the variables that was used earlier

class MyGame(arcade.Window):    #This creates the animation and window

    def __init__(self, width, height, title):   #This puts the width height and title in the window of the animation

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)  #This makes the background grey

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
#This opens up the window for the ball animation
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y
    #This allows the user to use the mouse to move the ball
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK
    #This tracks the number of clicks an user does and changes the color of the ball
    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN
    #This turns the ball Auburn when the mouse is released 
    
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
#This makes the animation run 

if __name__ == "__main__":
    main()