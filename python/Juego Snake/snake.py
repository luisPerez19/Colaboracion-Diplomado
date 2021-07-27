import turtle
import time # importa el modulo tiempo
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

#creacion y configuracion de la ventana
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#cabeza de la serpiente, creacion de elemento grafico e implementacion de caracteristicas
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()#quita el rastro de nuestro objeto
cabeza.goto(0, 0)#es para poscicionar nuestro elemento en el punto 0,0 (el centro)
cabeza.direction = "stop"

#creacion de la "comida"
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()#quita el rastro de nuestro objeto
comida.goto(0, 100)

#segmentos o cuerpo de la serpiente
segmentos = []

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0            High Score: 0", align = "center", font = ("Courier", 16, "normal"))

#Funciones
def arriba():
	cabeza.direction = "up"

def abajo():
	cabeza.direction = "down"

def izquierda():
	cabeza.direction = "left"

def derecha():
	cabeza.direction = "right"

#Teclado
wn.listen() #presta atencion a los eventos que puedan ocurrir
wn.onkeypress(arriba, "Up") #los parametros que recibe son dos, el metodo de la direccion a la cual ir y ademas la tecla con la cual se ejecutara la accion, si se aprieta o llega un evento del teclado "Up" es para reconocer la tecla de "arriba" y es necesario que la primera letra sea en mayuscula
wn.onkeypress(abajo, "Down") #si se aprieta o llega un evento del teclado "Down" es para reconocer la tecla de "abajo"
wn.onkeypress(izquierda, "Left") #si se aprieta o llega un evento del teclado "Left" es para reconocer la tecla de "izquierda"
wn.onkeypress(derecha, "Right") #si se aprieta o llega un evento del teclado "Right" es para reconocer la tecla de "derecha"

def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor() #da la coordenada en y de la cabeza de la serpiente
		cabeza.sety(y + 20) #actualiza la poscicion de la serpiente en y

	if cabeza.direction == "down":
		y = cabeza.ycor() 
		cabeza.sety(y - 20) 

	if cabeza.direction == "left":
		y = cabeza.xcor() #da la coordenada en x de la cabeza de la serpiente
		cabeza.setx(y - 20) #actualiza la poscicion de la serpiente en x

	if cabeza.direction == "right":
		y = cabeza.xcor() 
		cabeza.setx(y + 20) 


while True:
	wn.update()

	#colisiones bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0, 0)
		cabeza.direction = "stop"

		#Esconde los segmentos
		for segmento in segmentos:
			segmento.goto(2000, 2000)

		#limpiar lista de segemtos
		segmentos.clear()

		#resetear marcador
		score = 0
		texto.clear()
		texto.write("Score: {}            High Score: {}".format(score, high_score), align = "center", font = ("Courier", 16, "normal"))

	if cabeza.distance(comida) < 20: # lo que hace esta linea es medir la distancia de la cabeza a la comida
		x = random.randint(-14, 14)*20
		y = random.randint(-14, 14)*20 
		comida.goto(x, y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup() #creacion del "objeto" que se va a agregar a la lista
		segmentos.append(nuevo_segmento)

		#aumentar marcador 
		score += 10

		if score > high_score:
			high_score = score

		texto.clear()
		texto.write("Score: {}            High Score: {}".format(score, high_score), align = "center", font = ("Courier", 16, "normal"))

	#Mover el cuerpo de la serpiente
	totalSeg = len(segmentos)
	for index in range(totalSeg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x, y)

	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x, y)


	mov()

	#colisiones con el cuerpo
	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0, 0)
			cabeza.direction = "stop"

			#esconder los segmentos
			for segmento in segmentos:
				segmento.goto(-2000, -2000)

			segmentos.clear()

			#Resetear marcador
			score = 0
			texto.clear()
			texto.write("Score: {}            High Score: {}".format(score, high_score), align = "center", font = ("Courier", 16, "normal"))

	time.sleep(posponer) #pausa el programa la cantidad de tiempo puesta sleep es una funcion de time, recibe tiempo en s

turtle.mainloop() # sirve para que no se cierre la ventana 