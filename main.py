from PPlay.window import *
from PPlay.sprite import *
import random

janela = Window(450, 650)
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

janela.set_title("Flappy Mairu")
fundo = Sprite('fundo.png')

estadosPossiveis = ["MENU", "GAME", "GAME OVER"]
estadoAtual = "MENU"
ultimoEstado = ""

velCano = 15

cano = Sprite('cano.png')
listaCanos = []
distanciaVerticalEntreCanos = 150
distanciaEntreCanos = velCano * 20



gravidade = 1
velPulo = 25
velMax = 30
vel = 0
podePular = True


mouseApertado = False

clock = pygame.time.Clock()

def checaClick(botao, mouse):
    return botao.x < mouse[0] and botao.x + botao.width > mouse[0] and botao.y < mouse[1] and botao.y + botao.height > mouse[1]


while True:
    fundo.draw()
    dt = clock.tick(60)

    if estadoAtual == "MENU":
        if ultimoEstado != "MENU":
            player = Sprite('mairon.png')
            player.x = janela.width/8
            player.y = janela.height/2 - player.height/2
            fundo = Sprite("fundo.png")
            ultimoEstado = "MENU"
            fundo.draw()
            menu = Sprite('menu.png')

        if mouse.is_button_pressed(1):
            estadoAtual = "GAME"

        menu.draw()

    if estadoAtual == "GAME":
        if ultimoEstado != estadoAtual:
            listaCanos = []
            cano = Sprite('cano.png')
            cano.x = janela.width + 100
            cano.y = janela.height / 2 + distanciaVerticalEntreCanos / 2
            listaCanos.append(cano)
            cano = Sprite('cano2.png')
            cano.x = janela.width + 100
            cano.y = janela.height / 2 - cano.height - distanciaVerticalEntreCanos / 2
            listaCanos.append(cano)

            ultimoEstado = estadoAtual
            player.x = janela.width / 8
            player.y = janela.height / 2 - player.height / 2
        vel += gravidade
        player.y += (vel/100) * dt
        if (vel >= velMax):
            vel = velMax
        if(mouse.is_button_pressed(1) and podePular):
            vel = -velPulo
            podePular = False
            print("pula!")
        elif(not mouse.is_button_pressed(1)):
            podePular = True
        if player.y <= 0 or player.y + player.height > janela.height:
            if(player.y > 0):
                ultimo_y = janela.height - player.height
            else:
                ultimo_y = 0
            ultimoEstado = estadoAtual
            estadoAtual = "GAME OVER"
        print(len(listaCanos))
        for objeto in listaCanos:
            objeto.x -= velCano/100 * dt
            objeto.draw()
            if (objeto.collided(player)):
                estadoAtual = "GAME OVER"
                ultimo_x = player.x
                ultimo_y = player.y
            if objeto.x <= -objeto.width:
                listaCanos.remove(objeto)
            if(objeto.x <= janela.width - distanciaEntreCanos and len(listaCanos) < 5):
                meioY = random.randint(distanciaVerticalEntreCanos, janela.height - distanciaVerticalEntreCanos)
                cano = Sprite('cano.png')
                cano.x = listaCanos[-1].x + distanciaEntreCanos
                cano.y = meioY + distanciaVerticalEntreCanos / 2
                listaCanos.append(cano)
                cano = Sprite('cano2.png')
                cano.x = listaCanos[-1].x
                cano.y = meioY - cano.height - distanciaVerticalEntreCanos / 2
                listaCanos.append(cano)





    if estadoAtual == "GAME OVER":
        if ultimoEstado != estadoAtual:
            ultimoEstado = estadoAtual
            player = Sprite("mairon dead.png")
            fundo = Sprite("game over.png")
            player.x = ultimo_x
            player.y = ultimo_y
        if(not mouse.is_button_pressed(1) and mouseApertado):
            estadoAtual = "MENU"
        if(mouse.is_button_pressed(1)):
            mouseApertado = True
        else:
            mouseApertado = False


    player.draw()
    janela.update()