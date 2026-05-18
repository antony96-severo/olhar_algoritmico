import base64

import cv2

from src.services.capturar_frame import capturar_frame


def converter_frame_base64():
    frame = capturar_frame()

    if frame is None:
        return None

    sucesso, buffer = cv2.imencode(".jpg", frame)

    if not sucesso:
        return None

    imagem_base64 = base64.b64encode(buffer).decode("utf-8")

    return imagem_base64