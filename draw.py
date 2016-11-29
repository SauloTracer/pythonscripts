import turtle

'''
Desenha um polígono regular de N lados
formado por N polígonos regulares de N
lados com metade do tamanho do polígono
maior.

Cada face do polígono é formada por um
polígono menor formando uma mandala.

Parâmetros:
 sides REQUIRED INT Número de lados do polígono a ser desenhado.
 pencolor OPTIONAL Turtle.color (String ou Numérico) Default "black" Define a cor das linhas desenhadas.
 bgcolor OPTIONAL Turtle.color (String ou Numérico) Default "lightblue" Define a cor de fundo da tela.
 initialPosition LIST[INT, INT] OPTIONAL Default [0,100] Define a posição inicial da caneta.
 distance INT OPTIONAL Default 100 Define o tamanho de cada face do polígono. Caso não seja divisível por 2, será adicionado de 1.
 clear BOOL OPTIONAL Default True Define se a tela deve ou não ser limpa antes de desenhar o novo polígono.
 showSteps BOOL OPTIONAL Default False Define se os passos do desenho devem ser exibidos ou apenas a figura completa.
'''
def draw(sides,
         pencolor = "black",
         bgcolor = "lightblue",
         initialPosition = [0,100],
         distance = 100,
         clear=True,
         showSteps=False):
    
    if distance%2 == 1:
        distance += 1

    turtle.penup()
    turtle.goto(initialPosition[0],initialPosition[1])
    turtle.pendown()

    if clear:
        turtle.clear()
    turtle.bgcolor(bgcolor)
    turtle.pencolor(pencolor)
    #if not showSteps:
        #turtle.tracer(0,0)

    for steps in range(sides):
        turtle.forward(distance)
        turtle.right(360/sides)
        for moresteps in range(sides):
            turtle.forward(distance/2)
            turtle.right(360/sides)
                
    #if not showSteps:
        #turtle.update()
