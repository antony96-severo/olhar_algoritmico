import cv2


def capturar_frame():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return None

    sucesso, frame = camera.read()

    camera.release()

    if not sucesso:
        return None

    return frame