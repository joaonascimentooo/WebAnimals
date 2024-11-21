import cv2

def capture_emotion():
    print("Capturando emoções...")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if face_cascade.empty():
        print("Erro: arquivo de classificador Haar não encontrado.")
        return

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Erro ao acessar a câmera")
        return

    cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)  
    cap.set(cv2.CAP_PROP_CONTRAST, 0.5)    

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha na captura de frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_emotion()
