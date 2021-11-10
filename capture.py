import cv2

def video():
    # Inicia a captura de vídeo da Webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    while True:
        success, capture = cap.read()
        if not success:
            print('Falha ao tentar capturar o vídeo.')
            break
        frames = cv2.resize(capture, (0,0),None, 0.25,0.25)
        frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
        
        # facesCurrFrame = face_recognition.face_locations(frames)
        # encodingsCurrFrame = face_recognition.face_encodings(frames, facesCurrFrame)
                
        cv2.imshow('Webcam', capture)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressionado
            print("Escape pressionado, fechando janelas...")
            img = None
            success = False
            break
        elif k%256 == 32:
            # SPACE pressed
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, frame)
            # print("{} written!".format(img_name))
            # img_counter += 1
            img = capture
            break
    
    cap.release()
    
    cv2.destroyAllWindows()
    
    return success, img