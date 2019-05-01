# This is the main file for pingpongsp19

from tkinter import *
import table, ball, bat

# initialise global variables
x_velocity = 10
y_velocity = 0
score_left = 0
score_right = 0
first_serve = True

# order a window from the tkinter window factory
window = Tk()
window.title("Pingpong For IS3020 SPRING 19")
       
# order a table from the table class
pp_table = table.Table(window, net_colour="white", vertical_net=True)

# order a ball from the ball factory
pp_ball = ball.Ball(table=pp_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="yellow", x_start=288, y_start=188)

# order a left and right bat from the bat class
bat_L = bat.Bat(table=pp_table, width=15, height=100, x_posn=20, y_posn=150, colour="blue")
bat_R = bat.Bat(table=pp_table, width=15, height=100, x_posn=575, y_posn=150, colour="red")

#### functions:
def game_flow():
    global first_serve
    global score_left
    global score_right
    
    # wait for first serve:
    if(first_serve == True):
        pp_ball.stop_ball()
        first_serve = False
    
    # detect if ball has hit the bats:
    bat_L.detect_collision(pp_ball)
    bat_R.detect_collision(pp_ball)

    # detect if the ball has hit the left wall:
    if(pp_ball.x_posn <= 3):
        pp_ball.stop_ball()
        pp_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        pp_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        pp_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
        score_left = score_left + 1
        if(score_left >= 10):
            score_left = "W"
            score_right = "L"
        first_serve = True
        pp_table.draw_score(score_left, score_right)

    # detect if the ball has hit the right wall:
    if(pp_ball.x_posn + pp_ball.width >= pp_table.width - 3):
        pp_ball.stop_ball()
        pp_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        pp_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        pp_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
        score_right = score_right + 1
        if(score_right >= 5):
            score_right = "W"
            score_left = "L"
        first_serve=True
        pp_table.draw_score(score_left, score_right)
     
    pp_ball.move_next()
    window.after(50, game_flow)

# restart_game function here:
def restart_game(master):
    global score_left
    global score_right
    pp_ball.start_ball(x_speed=x_velocity, y_speed=0)
    if(score_left == "W" or score_left == "L"):
        score_left = 0
        print = "Team 1"
        score_right = 0
    pp_table.draw_score(score_left, score_right)

# bind the controls of the bats to keys on the keyboard
window.bind("q", bat_L.move_up)
window.bind("a", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

# bind restart to the spacebar
window.bind("<space>", restart_game)

# call the game_flow loop
game_flow()

# start the tkinter loop process
window.mainloop()
