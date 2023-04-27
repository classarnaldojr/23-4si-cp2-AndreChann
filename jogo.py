import cv2

import numpy as np

import matplotlib.pyplot as plt

video = cv2.VideoCapture('pedra-papel-tesoura.mp4') #Capturar Vídeo

#inicializando variáveis da pontuação
pontos_jogador1 = 0
pontos_jogador2 = 0
jogadas_anteriores = []
resultado = ""

if not video.isOpened():
    raise Exception("Ocorreu um erro") #Exception caso não abrir
    
while True:

    ret, frame = video.read() #Ler o frame do vídeo

    foto = frame.copy() #Copia do frame para fazer outro retorno

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Converte BGR para HSV

    img = cv2.blur(img_hsv, (15, 15), 0)  # Blur na Imagem para ajudar a detecção

    # HSV Ranges
    lower_hsv_1 = np.array([0, 20, 10])  
    higher_hsv_1 = np.array([18, 200, 200])  

    lower_hsv_2 = np.array([0, 1, 1])  
    higher_hsv_2 = np.array([255, 150, 250])  

    mask_1 = cv2.inRange(img, lower_hsv_1, higher_hsv_1)  # Máscara 1

    mask_2 = cv2.inRange(img, lower_hsv_2, higher_hsv_2)  # Máscara 2

    img_filtro = cv2.bitwise_or(mask_1, mask_2)  # Imagem filtrada (para calcular Massa do Objeto)

    contours, _ = cv2.findContours(img_filtro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Encontrar os Contornos da Imagem img_filtro

    cv2.drawContours(foto, contours, -1, [0, 255, 0], 3) #Contorno das mãos na cor verde

    c1 = contours[1] #Atribuindo Jogador 1
    c2 = contours[0] #Atribuindo Jogador 2

    sla = cv2.moments(c1) #Retirando Dicionário dos Contornos do Jogador 1
    sla2 = cv2.moments(c2) #Retirando Dicionário dos Contornos do Jogador 2

    area1 = int(sla['m00']) #Retirando Valor da área total do objeto do jogador 1)
    area2 = int(sla2['m00'])#Retirando Valor da área total do objeto do jogador 2)

    # Atribuindo os objetos do jogo de acordo com a área total do jogador 1
    if area1 < 58000:
        area1 = "Tesoura"

    elif area1 > 58000 and area1 < 70000:
        area1 = "Pedra"

    elif area1 > 70000:
        area1 = "Papel"

    # Atribuindo os objetos do jogo de acordo com a área total do jogador 2
    if area2 < 58000:
        area2 = "Tesoura"

    elif area2 > 58000 and area2 < 70000:
        area2 = "Pedra"

    elif area2 > 70000:
        area2 = "Papel"

    # Invertendo uma das rodadas que foram processadas invertidas
    if area1 == "Pedra" and area2 == "Tesoura":
        area1 = "Tesoura"
        area2 = "Pedra"

    if len(jogadas_anteriores) == 0:
        if area1 == area2:
            resultado = "Empate!"
            jogadas_anteriores.append((area1, area2))
        elif (area1 == "Tesoura" and area2 == "Papel"):
                resultado = "Jogador 1 Venceu!"
                pontos_jogador1 = pontos_jogador1 + 1
                jogadas_anteriores.append((area1, area2))
        elif (area1 == "Papel" and area2 == "Tesoura"):
            resultado = "Jogador 2 Venceu!"
            pontos_jogador2 = pontos_jogador2 + 1
            jogadas_anteriores.append((area1, area2))
        elif (area1 == "Pedra" and area2 == "Tesoura"):
            resultado = "Jogador 1 Venceu!"
            pontos_jogador1 = pontos_jogador1 + 1
            jogadas_anteriores.append((area1, area2))
        elif (area1 == "Tesoura" and area2 == "Pedra"):
            resultado = "Jogador 2 Venceu!"
            pontos_jogador2 = pontos_jogador2 + 1
            jogadas_anteriores.append((area1, area2))
        elif (area1 == "Papel" and area2 == "Pedra"):
            resultado = "Jogador 1 Venceu!"
            pontos_jogador1 = pontos_jogador1 + 1
            jogadas_anteriores.append((area1, area2))
        elif (area1 == "Pedra" and area2 == "Papel"):
            resultado = "Jogador 2 Venceu!"
            pontos_jogador2 = pontos_jogador2 + 1
            jogadas_anteriores.append((area1, area2))
    else:
        if (area1, area2) != jogadas_anteriores[-1]:
            # atualizar as pontuações de acordo com a jogada atual
            if area1 == area2:
                resultado = "Empate!"
                jogadas_anteriores.append((area1, area2))
            elif (area1 == "Tesoura" and area2 == "Papel"):
                resultado = "Jogador 1 Venceu!"
                pontos_jogador1 = pontos_jogador1 + 1
                jogadas_anteriores.append((area1, area2))
            elif (area1 == "Papel" and area2 == "Tesoura"):
                resultado = "Jogador 2 Venceu!"
                pontos_jogador2 = pontos_jogador2 + 1
                jogadas_anteriores.append((area1, area2))
            elif (area1 == "Pedra" and area2 == "Tesoura"):
                resultado = "Jogador 1 Venceu!"
                pontos_jogador1 = pontos_jogador1 + 1
                jogadas_anteriores.append((area1, area2))
            elif (area1 == "Tesoura" and area2 == "Pedra"):
                resultado = "Jogador 2 Venceu!"
                pontos_jogador2 = pontos_jogador2 + 1
                jogadas_anteriores.append((area1, area2))
            elif (area1 == "Papel" and area2 == "Pedra"):
                resultado = "Jogador 1 Venceu!"
                pontos_jogador1 = pontos_jogador1 + 1
                jogadas_anteriores.append((area1, area2))
            elif (area1 == "Pedra" and area2 == "Papel"):
                resultado = "Jogador 2 Venceu!"
                pontos_jogador2 = pontos_jogador2 + 1
                jogadas_anteriores.append((area1, area2))    

    # Título
    (cv2.putText(foto,
                 "Pedra, Papel e Tesoura",
                 (500, 80),
                 cv2.FONT_HERSHEY_SIMPLEX,
                 2, (0, 0, 0), 5,
                cv2.LINE_AA))

    # Exibe a jogada do Jogador 1
    (cv2.putText(foto,
                 ("Jogador 1: " + str(area1)),
                 (25, 170),                         
                 cv2.FONT_HERSHEY_SIMPLEX,
                 2, (0, 0, 0), 4, cv2.LINE_AA))
    # Exibe a jogada do Jogador 2
    (cv2.putText(foto,
                 ("Jogador 2: " + str(area2)),
                 (25, 270),
                 cv2.FONT_HERSHEY_SIMPLEX,          
                 2, (0, 0, 0), 4, cv2.LINE_AA))
    # Resultado da Round
    (cv2.putText(foto,
                 str(resultado),
                 (510, 900),
                 cv2.FONT_HERSHEY_SIMPLEX,          
                 3,
                 (0, 0, 255), 5, cv2.LINE_AA))

    # Pontuação do Jogador 1
    (cv2.putText(foto,
                ("Placar Jogador 1 = " + str(pontos_jogador1)),
                (1100, 170),                            
                cv2.FONT_HERSHEY_SIMPLEX,
                2,(255, 0, 0), 3, cv2.LINE_AA))

    # Pontuação do Jogador 2
    (cv2.putText(foto,
                ("Placar Jogador 2 = " + str(pontos_jogador2)),
                (1100, 270),
                cv2.FONT_HERSHEY_SIMPLEX,             
                2,(255, 0, 0), 3, cv2.LINE_AA))

    # Ajuste das janelas de vídeo
    frame = cv2.resize(img_filtro, (640, 480))
    img_final = cv2.resize(foto, (640, 480))

    cv2.imshow("Desenho das maos", frame)
    cv2.imshow("Game final", img_final)

    # ESC para encerrar a execução
    key = cv2.waitKey(20)
    if key == 27:  
        break

    if not ret:
        break

video.release()

cv2.destroyAllWindows()


