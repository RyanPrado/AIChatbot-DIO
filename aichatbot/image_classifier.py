
from loguru import logger
import os
import torch


class ImageClassifier:
    def __init__(self):
        logger.info("Iniciando a classe de classificação de imagens")
        self._model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        logger.info("Iniciado modelo da rede YoloV5s")

    def _validate_path(self, path):
        
        if len(path) > 0 and os.path.exists(path) and os.path.isfile(path):
            return True
            
        return False

    def _request_image_path(self):
        path = str(input("Digite o caminho da imagem: "))
        return path.strip()

    def predict_image(self, path=None):
        if path is None:
            path = self._request_image_path()

        if self._validate_path(path) is not True:
            raise ValueError(f"Invalid path format {path}")
        
        results = self._model(path)
        return results.pandas().xyxy[0]['name'].tolist()

        