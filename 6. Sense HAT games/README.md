# Raspberry Pi - Sense HAT - 1. Maze game

```python
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()
r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)

x = 1
y = 1

game_over = False

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,r,r,r],
        [r,b,r,b,r,b,b,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,g,b,b,r],
        [r,r,r,r,r,r,r,r]]

def move_marble(pitch,roll,x,y):
    new_x = x
    new_y = y
    if 10 < pitch < 170 and x != 0:
        new_x -= 1
    elif 350 > pitch > 170 and x != 7 :
        new_x += 1
    if 10 < roll < 170 and y != 7:
        new_y += 1
    elif 350 > roll > 170 and y != 0 :
        new_y -= 1
    x,y = check_wall(x,y,new_x,new_y)
    return x,y

def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] != r:
        return new_x, new_y
    elif maze[new_y][x] != r:
        return x, new_y
    elif maze[y][new_x] != r:
        return new_x, y
    else:
        return x,y

def check_win(x,y):
    global game_over
    if maze[y][x] == g:
        game_over = True
        sense.show_message('You Win')

while not game_over:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x,y = move_marble(pitch,roll,x,y)
    check_win(x,y)
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.01)
    maze[y][x] = b
```

This code is a maze game that uses the Sense HAT on a Raspberry Pi. The code is written in Python and utilizes the sense_hat library to interact with the Sense HAT. Here is a step-by-step explanation of the code:

1. The first line imports the SenseHat class from the sense_hat library and the sleep function from the time library.

2. sense = SenseHat() creates an instance of the SenseHat class, which allows the code to interact with the Sense HAT.

3. sense.clear() clears the LED matrix on the Sense HAT.

4. r = (255,0,0), b = (0,0,0), w = (255,255,255), g = (0,255,0) creating variables for different colors.

5. x = 1 and y = 1 are the initial coordinates of the cursor on the LED matrix.

6. game_over = False is a flag variable that keeps track of whether the game is over or not.

7. maze is a two-dimensional list that represents the maze. The red color represents the walls, black color represents the empty spaces, white color represents cursor position and green represents the end point of the maze.

8. move_marble() function takes the current x,y position of cursor and pitch and roll value from the sensor. Then it calculates the new x,y position based on the pitch and roll value.

        1. The move_marble function takes in the pitch, roll, x, and y values of the cursor as its input arguments. The function uses these values to determine the new x and y coordinates of the cursor.

        2.It first creates two new variables called new_x and new_y, which are initially set to the current x and y coordinates of the cursor.

        3.Next, it uses an if-elif statement to check the pitch value of the cursor. If the pitch value is between 10 and 170, and the current x coordinate is not 0 (i.e., the cursor is not at the left edge of the matrix), it decrements the new_x value by 1. This moves the cursor one position to the left.

        4.If the pitch value is between 350 and 170, and the current x coordinate is not 7 (i.e., the cursor is not at the right edge of the matrix), it increments the new_x value by 1. This moves the cursor one position to the right.

        5.Next, it uses an if-elif statement to check the roll value of the cursor. If the roll value is between 10 and 170, and the current y coordinate is not 7 (i.e., the cursor is not at the bottom edge of the matrix), it increments the new_y value by 1. This moves the cursor one position down.

        6.If the roll value is between 350 and 170, and the current y coordinate is not 0 (i.e., the cursor is not at the top edge of the matrix), it decrements the new_y value by 1. This moves the cursor one position up.

        7.Finally, it calls the check_wall function and pass the current x,y and new_x,new_y coordinates. It returns the new coordinates which will be the new position of the cursor.

        8.This function is used to move the cursor based on the pitch and roll values. It ensures that the cursor does not move out of the LED matrix and does not move into the walls of the maze.
        
9. check_wall() function takes the current x,y position of cursor and new x,y position calculated by move_marble() function. It checks if the new x,y position is a wall, if true then it will return the original x,y position.
        
        1.The check_wall function takes in the current x, y, new_x, and new_y coordinates of the cursor as its input arguments. The function uses these values to check if the new position of the cursor is a wall or not.

        2.It first checks if the new position represented by new_x and new_y is a wall or not. If the value at the new position is not red (r), it returns the new_x and new_y coordinates, meaning the cursor can move to this new position.

        3.If the new position is a wall, it checks if the new_y is a wall or not. If it's not a wall, it returns the current x coordinate and the new_y coordinate. This means that the cursor can move to the new_y position but not new_x.

        4.If the new_y is also a wall, it checks if the new_x is a wall or not. If it's not a wall, it returns the new_x coordinate and the current y coordinate. This means that the cursor can move to the new_x position but not new_y.

        5.If both the new_x and new_y coordinates are walls, it returns the current x and y coordinates, meaning the cursor cannot move to the new position.

        6.This function is used to ensure that the cursor does not move into the walls of the maze. It checks if the new position of the cursor is a wall or not and returns the new coordinates which will be the new position of the cursor. It makes sure that cursor is only moved to a valid position and not into a wall.
        
10. check_win() function takes the current x,y position of cursor and checks if it is the end point of the maze, if true then it will show the message "You Win" on the LED matrix

        1.The check_win function takes in the x and y coordinates of the cursor as its input arguments. The function uses these values to check if the cursor has reached the end point of the maze or not.

        2.It first checks if the current position represented by x and y is the end point of the maze or not. If the value at the current position is green (g), it sets the global variable game_over to True, meaning that the game is over.

        3.Then it shows a message 'You Win', using the sense.show_message function, indicating that the player has won the game.

        4.If the current position is not the end point, the function does nothing and the while loop continues to run.

        5.This function is used to check if the cursor has reached the end point of the maze or not. It compares the current position of the cursor with the end point and if they match, it sets the game_over variable to true and shows the message 'You Win'.

11. while not game_over: is the main loop of the game. The loop continues until the game is over, which is determined by the game_over flag variable.

12. pitch = sense.get_orientation()['pitch'] and roll = sense.get_orientation()['roll'] are used to get the pitch and roll values from the Sense HAT's accelerometer.

13. x,y = move_marble(pitch,roll,x,y) updates the cursor position based on the pitch and roll values.

14. check_win(x,y) checks if the cursor has reached the end point of the maze.

15. maze[y][x] = w changes the color of the current cursor position to white

16. sense.set_pixels(sum(maze,[])) sets the pixels of the LED matrix to match the current state of the maze

17. sleep(0.01) is used to slow down the loop and make the cursor movement more visible.

18. maze[y][x] = b changes the color of the current cursor position back to black

19. The last line of the code is the end of the while loop and the end of the game
