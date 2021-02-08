import turtle

window = turtle.Screen()

colors=['black', 'orange']

t = turtle.Pen()
t.speed(0)


    
for x in range(360):
    t.pencolor(colors[1])
    t.width(x/100+1)
    t.forward(x + 20)
    t.right(59)

turtle.mainloop()