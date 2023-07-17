import turtle

# render the GUI window
ws = turtle.Screen()
ws.title("Python Course - Doing Space Invaders Game with Turtle Module")
bgcolor = 'wheat'
ws.bgcolor(bgcolor)
ws.setup(width=1200, height=800)


# initial interface 
def display_main_menu(): 

    ws.exitonclick() 
    ws.mainloop()