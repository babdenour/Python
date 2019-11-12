#coding: utf-8
import turtle;

#coding window
picture_width = 600;
picture_height = 540;
turtle.setup (width=picture_width, height=picture_height);

#draw square
turtle.right (90);
turtle.forward (100);
turtle.left(90);
turtle.forward (100);
turtle.left (90);
turtle.forward (100);
turtle.left(90);
turtle.forward (100);
#draw triangle
turtle.right (150);
turtle.forward (58);
turtle.right(60);
turtle.forward (58);

#moving cursor
turtle.up();
turtle.goto(102, 0);
turtle.down();
turtle.right(-30);
#draw square
turtle.right (90);
turtle.forward (100);
turtle.left(90);
turtle.forward (100);
turtle.left (90);
turtle.forward (100);
turtle.left(90);
turtle.forward (100);
#draw triangle
turtle.right (150);
turtle.forward (58);
turtle.right(60);
turtle.forward (58);

#code closing window
turtle.hideturtle();
turtle.exitonclick();