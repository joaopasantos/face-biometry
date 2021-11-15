import cv2

def video():
    # Inicia a captura de vídeo da Webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Loop para a apresentação do vídeo
    while True:
        success, capture = cap.read()
        if not success:
            cap.release()
            cv2.destroyAllWindows()
            raise RuntimeError('Falha ao tentar capturar o vídeo.')
            break
        cv2.imshow('Webcam', capture) # Apresenta o vídeo sendo capturado para o usuário
        k = cv2.waitKey(1)
        # ESC pressionado
        if k%256 == 27:
            print("Escape pressionado, fechando janelas...")
            cap.release()
            cv2.destroyAllWindows()
            raise RuntimeError('Usuário cancelou a captura de imagem.')
            break
        # ESPAÇO pressionado
        elif k%256 == 32:
            img = capture # Captura a imagem
            break
    # Finaliza a captura e fecha as instâncias de janelas
    cap.release()
    cv2.destroyAllWindows()
    return img