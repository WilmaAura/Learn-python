import turtle

# bikin turtle (pena) dan layar
t = turtle.Turtle()
s = turtle.Screen()

#Atur background layar jadi hitam
s.bgcolor('black')

# hati warna merah
t.fillcolor('red')
t.begin_fill()
t.left(50)
t.fd(120)
t.circle(45,200)
t.lt(221)
t.circle(45,200)
t.fd(130)
t.end_fill()
turtle.done()

