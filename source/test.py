from vosk import Model, KaldiRecognizer


def transcribe(data, frequency):
    model = Model(r'C:\Users\Nick\PycharmProjects\Transcriber\source\vosk-model-small-en-us-0.15')
    recognizer = KaldiRecognizer(model, frequency)
    if recognizer.AcceptWaveform(data):
        return recognizer.Result()
    else:
        return recognizer.PartialResult()
