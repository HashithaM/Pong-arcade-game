# Pong-arcade-game
This is a simple pong arcade game with ball and two paddles
This code is for a simple Pong arcade game implemented using the Turtle module in Python. Let's break down the key components:

Import Statements:

The code starts by importing necessary modules such as Screen, Paddle, Ball, ScoreBoard, and time.
Initialization:

screen: Initializes the game window.
l_paddle and r_paddle: Create left and right paddles using the Paddle class.
ball: Create a ball object using the Ball class.
score_board: Create a scoreboard object using the ScoreBoard class.
Screen Setup:

Sets up the dimensions, background color, and title of the game window.
Turns off screen updating initially to improve performance.
Keyboard Bindings:

Binds keys "w" and "s" to move the left paddle up and down, respectively.
Binds the Up and Down arrow keys to move the right paddle up and down, respectively.
Main Game Loop:

Enters a while loop (game_on) to continuously update the game state.
Uses time.sleep() to control the speed of the ball's movement.
screen.update() updates the screen to reflect changes.
ball.move() updates the position of the ball.
Collision Detection:

Detects collisions with the top and bottom walls, making the ball bounce vertically (ball.bounce_y()).
Detects collisions with the paddles, making the ball bounce horizontally (ball.bounce_x()).
Score Tracking:

Tracks when the ball goes beyond the paddles' x-coordinate, indicating a point scored by the opponent.
Resets the ball's position and updates the respective score on the scoreboard.
Game Termination:

The game loop continues indefinitely until the window is closed (screen.exitonclick()).
This code creates a basic playable version of the classic Pong game where two players control paddles to hit a ball back and forth. The game ends when one player misses the ball, and their opponent scores a point.
