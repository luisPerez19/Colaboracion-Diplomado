# Colaboracion-Diplomado
Este repositorio es creado con la finalidad de aprender las tecnologías de Git y GitHub en la cual todas las personas podrán colaborar con la finalidad de practicar.

¿Cómo ejecutar los juegos de Python?

Lo primero que debes hacer es clonar este repositorio (recuerda que puedes practicar realizando: fork, pull request e issues en el).
Desde la terminal puedes usar el comando ls para verificar que se encuentra en tu carpeta como se muestra a continuación (el nombre del repositorio es Colaboracion-Diplomado):
![imagen](https://user-images.githubusercontent.com/87548725/127193421-146e83d8-1dda-4971-9b0e-441062297f2a.png)

Dentro de el encontraras una carpeta "python" y este archivo README.md que estas leyendo en este mismo momento:
![imagen](https://user-images.githubusercontent.com/87548725/127193638-cb38bd14-3e20-480b-81b5-c2e185bd1f42.png)

Dentro de la carpeta python encontraras dos carpetas más, la primera contiene el famoso juego de pong (uno de los primeros juegos de la historia) y el segundo contiene el juego de la "viborita" jeje también conocido como snake, lo que debemos hacer es acceder a cualquier directorio del juego que nos interese (para este caso en particular escogeré el juego se la viborita) y dentro estará un archivo de python "snake.py" tal como se muestra a continuación:
![imagen](https://user-images.githubusercontent.com/87548725/127194354-a2af2865-4656-4723-9cbb-9e2ec65a31ae.png)

y utilizamos el siguiente comando para ejecutar el juego: 
![imagen](https://user-images.githubusercontent.com/87548725/127194529-ffcc6152-11f6-4c90-b076-07c7f6ef2c0e.png)

Si no te funciona, no te preocupes!!! lo que pasa es que hace falta instalar una biblioteca especial para que el programa funcione correctamente, por lo que si quieres instalar dicha biblioteca deberás de ejecutar el siguiente comando:
![imagen](https://user-images.githubusercontent.com/87548725/127194762-09c4aa86-cddd-429b-abc7-7431e3ef781a.png)

Y listo!!!, únicamente te queda ejecutar python3 snake.py (o python3 pong.py si te encuentras en la carpeta del juego de pong) y ya podras disfrutar de estos dos juegos.

Recuerda que no son perfectos pero podremos mejorarlos entre todos, si tienes algún jueguito (no importa el lenguaje de programación) o aportación que desees agregar al repositorio no dudes en hacerlo.


NOTAS Juego de Pong: 
Los controles para pong son los siguientes:
Jugador 1 (W = arriba, S = abajo)
Jugador 2 (↑ = arriba, ↓ = abajo) (flechas de arriba y abajo del teclado)

Dependiendo el sistema operativo la pelota puede ser muuuuuuy rápida o por el contrario algo lenta, si te sucede esto (por que a mi me sucedió), deberás modifircar el archivo pong.py y en las líneas 39 y 40 encontraras lo siguiente:
![imagen](https://user-images.githubusercontent.com/87548725/127196527-61029cdb-317b-4c75-9d3c-7b691b658dcb.png)

Simplemende modifica el valor, por ejemplo: si quieres que la pelota sea más lenta puedes colocar en ambos datos 0.2 o si quieres que sean más rápidas entonces 0.7, puedes jugar con estos valores y checar el código por si quieres hacer tantas modificaciones como quieras, Diviertete!!!

NOTAS Juego de Snake:
Los controles para snake son los siguientes:
Jugador (↑ = arriba, ↓ = abajo, → = derecha, ← = izquierda) (flechas de arriba, abajo, izquierda y derecha del teclado)

