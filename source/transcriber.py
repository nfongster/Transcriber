from vosk import Model, KaldiRecognizer


def transcribe(data: bytes, frequency: int, model_dir: str):
    model = Model(model_dir)
    recognizer = KaldiRecognizer(model, frequency)
    if recognizer.AcceptWaveform(data):
        return recognizer.Result()
    else:
        return recognizer.PartialResult()
