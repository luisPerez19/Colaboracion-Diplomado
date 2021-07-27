import turtle

#marcador
marcador_a = 0
marcador_b = 0

#creación de ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) #este comando sirve para que se vea mas fluido

#jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid = 5, stretch_len = 1) #cambia el tamaño de nuestro objeto por dejecto mide 20x20 lo que hicimos aqui fue que tuviese 5 veces mas altura y la anchura se quedara igual 

#jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid = 5, stretch_len = 1)

#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.5 #movimiento de la pelota en x
pelota.dy = 0.5 #movimiento de la pelota en y

#linea divisora
division = turtle.Turtle()
division.color("white")
division.goto(0, 400)
division.goto(0, -400)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0          Jugador B: 0", align = "center", font = ("Courier", 16, "normal"))

#funciones

def jugadorA_up():
	y = jugadorA.ycor()
	y += 20
	jugadorA.sety(y)

def jugadorA_down():
	y = jugadorA.ycor()
	y -= 20
	jugadorA.sety(y)

def jugadorB_up():
	y = jugadorB.ycor()
	y += 20
	jugadorB.sety(y)

def jugadorB_down():
	y = jugadorB.ycor()
	y -= 20
	jugadorB.sety(y)

#teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w") #ligar la funcion a una tecla
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")

while True:
	wn.update()

	pelota.setx(pelota.xcor() + pelota.dx)
	pelota.sety(pelota.ycor() + pelota.dy)

	#bordes
	if pelota.ycor() > 290:
		pelota.dy *= -1 #invierte la direccion en y al tocar el techo
	if pelota.ycor() < -290:
		pelota.dy *= -1 #invierte la direccion en y al tocar el piso

	#bordes laterales
	if pelota.xcor() > 390:
		pelota.goto(0, 0) 
		pelota.dx *= -1
		marcador_a += 1
		pen.clear()
		pen.write("Jugador A: {}          Jugador B: {}".format(marcador_a,marcador_b), align = "center", font = ("Courier", 16, "normal"))

	if pelota.xcor() < -390:
		pelota.goto(0, 0)
		pelota.dx *= -1
		marcador_b += 1
		pen.clear()
		pen.write("Jugador A: {}          Jugador B: {}".format(marcador_a,marcador_b), align = "center", font = ("Courier", 16, "normal"))

	#colisiones
	if ((pelota.xcor() > 340 and pelota.xcor() < 350) #verifica si la pelota se encuentra en el rango x de la paleta
			and (pelota.ycor() < jugadorB.ycor() + 50 #verifica si la pelota se encuentra en el rango y de la paleta
			and pelota.ycor() > jugadorB.ycor() - 50)): #verifica si la pelota se encuentra en el rango y de la paleta
		pelota.dx *= -1

	if ((pelota.xcor() < -340 and pelota.xcor() > -350)
			and (pelota.ycor() < jugadorA.ycor() + 50
			and pelota.ycor() > jugadorA.ycor() - 50)):
		pelota.dx *= -1


turtle.mainloop() # sirve para que no se cierre la ventana 