from aichatbot import config
from aichatbot.image_classifier import ImageClassifier

from loguru import logger
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import threading

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
        except Exception as e:
            if str(e).strip() != "":
                logger.error(e)
    return said

def speak(text : str):
    tts = gTTS(text=text,lang='pt')
    output_file = config.PROCESSED_DATA_DIR / "output.mp3"
    try:
        os.remove(output_file)
    except OSError:
        pass
    tts.save(output_file)
    playsound.playsound(output_file)

image_identifier = ImageClassifier()

CLASSES_MAPPING = dict(car = "Carros") 

@logger.catch
def main():
    while True:
        logger.info("Escutando...")
        try:
            text = get_audio().lower()
            if len(text) == 0:
                continue
            logger.debug(f"Úsuario: {text}")
            if ('identifique' in text or 'identifica' in text) and ('imagem' in text):
                threading.Thread(target=speak,args=("Cole a seguir o endereço da imagem:",)).start()
                try:
                    classes = image_identifier.predict_image()
                    if len(classes) > 0:
                        class_name = classes[0]
                        if classes[0] in CLASSES_MAPPING:
                            class_name= CLASSES_MAPPING[classes[0]]
                        logger.success(f"Encaminhando sugestões de {class_name}...")
                        threading.Thread(target=speak,args=(f"Encaminhando sugestões de {class_name}",)).start()
                    else:
                        threading.Thread(target=speak,args=("Nada relevante encontrado na imagem",)).start()

                except ValueError as e:
                    threading.Thread(target=speak,args=("Ocorreu um erro na leitura da imagem",)).start()
                    logger.error(e)
                except KeyboardInterrupt:
                    threading.Thread(target=speak,args=("Ação abortada",)).start()
                except Exception as e:
                    logger.error(e)

        except AttributeError:
            pass

if __name__ == "__main__":
    main()