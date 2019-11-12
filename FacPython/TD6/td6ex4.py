#coding: utf-8
import turtle;
#screen init
screen_width = 800;
screen_height = 600;
turtle.setup (width=screen_width, height=screen_height);

#moving
turtle.up();
turtle.goto(-200,0);
turtle.down();

#draw
for i in range(0, 8, 1):
    turtle.forward(100);
    turtle.left(90);
    turtle.forward(40);
    turtle.right(90);
    turtle.forward(40);
    turtle.right(90);
    turtle.forward(40);
    turtle.left(90);

#coding exit
#turtle.hideturtle();
turtle.exitonclick();