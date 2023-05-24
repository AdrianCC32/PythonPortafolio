import cv2
import dlib

# Cargar el detector de rostros de dlib (HOG)
detector_rostros = dlib.get_frontal_face_detector()

# Cargar el modelo de reconocimiento facial de dlib
modelo_reconocimiento = dlib.shape_predictor(
    "shape_predictor_5_face_landmarks.dat")

# Cargar el clasificador de expresiones faciales
clasificador_expresiones = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Cargar el clasificador de emociones
clasificador_emociones = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml")

# Cargar el modelo de detección de puntos faciales de dlib
predictor_facial = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")

# Función para detectar rostros en una imagen


def detectar_rostros_imagen(imagen):
    # Convertir la imagen a escala de grises
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen
    rostros = detector_rostros(grises)

    return rostros

# Función para detectar rostros en un video en tiempo real


def detectar_rostros_video():
    # Inicializar el capturador de video
    capturador = cv2.VideoCapture(0)

    while True:
        # Leer el siguiente fotograma del video
        ret, fotograma = capturador.read()

        # Convertir el fotograma a escala de grises
        grises = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)

        # Detectar rostros en el fotograma
        rostros = detector_rostros(grises)

        # Iterar sobre los rostros detectados
        for rostro in rostros:
            # Obtener las coordenadas del rectángulo del rostro
            x, y, w, h = rostro.left(), rostro.top(), rostro.width(), rostro.height()

            # Dibujar el rectángulo del rostro en el fotograma
            cv2.rectangle(fotograma, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Obtener los puntos faciales del rostro
            puntos_faciales = predictor_facial(grises, rostro)

            # Reconocer la expresión facial
            expresion = clasificar_expresion(fotograma, puntos_faciales)

            # Mostrar la expresión reconocida junto al rostro
            cv2.putText(fotograma, expresion, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Mostrar el fotograma resultante
        cv2.imshow("Detección de rostros", fotograma)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar el capturador de video y cerrar las ventanas
    capturador.release()
    cv2.destroyAllWindows()

# Función para clasificar la expresión facial


def clasificar_expresion(imagen, puntos_faciales):
    # Convertir los puntos faciales a una lista de tuplas
    puntos = puntos_faciales_to_lista(puntos_faciales)

    # Detectar la expresión facial
    expresion = "Desconocida"
    if len(clasificador_expresiones.detectMultiScale(imagen, scaleFactor=1.1, minNeighbors=20, minSize=(30, 30))) > 0:
        expresion = "Sonriendo"
    return expresion


# Función para convertir los puntos faciales de dlib a una lista de tuplas
def puntos_faciales_to_lista(puntos_faciales):
    puntos = [(punto.x, punto.y) for punto in puntos_faciales.parts()]
    return puntos


# Ejecutar 
detectar_rostros_video()
