#!/bin/bash
gnome-pomodoro & # Replace with the command to launch your application

while ! wmctrl -x -R "gnome-pomodoro"; do
    sleep 1
done

wmctrl -x -r "gnome-pomodoro" -e 0,3353,65,500,1106 # Replace with the desired position and size
# wmctrl -r "gnome-pomodoro" -e 0,x,y,width,height # Replace with the desired position and size
