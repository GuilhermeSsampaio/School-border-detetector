import cv2
import numpy as np

# Carrega a imagem em escala de cinza
imagem = cv2.imread('teste.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica detecção de bordas usando Canny
bordas = cv2.Canny(imagem, 22, 38)

# Inverte as cores para traços pretos e fundo branco
resultado = cv2.bitwise_not(bordas)

# Função para imprimir a imagem de saída
def imprimir_imagem(imagem):
    from PIL import Image
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        cv2.imwrite(temp_file.name, imagem)
        temp_file.close()
        Image.open(temp_file.name).show()
        os.remove(temp_file.name)

# Vetoriza a imagem usando o algoritmo de contorno
contornos, _ = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imagem_vetorizada = np.ones_like(imagem) * 255  # Fundo branco
cv2.drawContours(imagem_vetorizada, contornos, -1, (0, 0, 0), 2)  # Desenha o contorno preto mais grosso

# Aplica um filtro de nitidez para melhorar a nitidez
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
imagem_vetorizada = cv2.filter2D(imagem_vetorizada, -1, kernel)

# Salva a imagem resultante
cv2.imwrite('resultado.jpg', imagem_vetorizada)

# Imprime a imagem resultante
imprimir_imagem(imagem_vetorizada)

imagens_juntas = np.concatenate((imagem, imagem_vetorizada), axis=1)

# Mostra o resultado
cv2.imshow('Original vs Bordas Detectadas', imagens_juntas)
cv2.waitKey(0)
cv2.destroyAllWindows()
