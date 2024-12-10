import cv2
import numpy as np

def conversao(imagem_path):
    # Carrega a imagem em escala de cinza
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)

    # Aplica detecção de bordas usando Canny
    bordas = cv2.Canny(imagem, 22, 38)

    # Inverte as cores para traços pretos e fundo branco
    resultado = cv2.bitwise_not(bordas)

    # Vetoriza a imagem usando o algoritmo de contorno
    contornos, _ = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    imagem_vetorizada = np.ones_like(imagem) * 255  # Fundo branco
    cv2.drawContours(imagem_vetorizada, contornos, -1, (0, 0, 0), 2)  # Desenha o contorno preto mais grosso

    # Aplica um filtro de nitidez para melhorar a nitidez
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    imagem_vetorizada = cv2.filter2D(imagem_vetorizada, -1, kernel)

   # Salva a imagem resultante
    resultado_path = 'resultado.jpg'
    cv2.imwrite(resultado_path, imagem_vetorizada)

    return resultado_path

