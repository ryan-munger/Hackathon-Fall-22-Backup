import speech_recognition
import pyttsx3

def get_speech(match):
    recognizer = speech_recognition.Recognizer()

    while True:

        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=.1)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(text)

                for case in match:
                    if case in text:
                        return case
                return 'Error'

        except speech_recognition.UnknownValueError:
            return 'Error'
