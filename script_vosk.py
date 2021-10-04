import os
import sys
import time
import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
# install with `pip install vosk`

SetLogLevel(0)


def recongize_vosk(audio_filename, text_filename, model_path='model') -> None:
    '''
    Recognize audio from 'audio_filename' with vosk model and 
    write text on the screen and into 'text_filename' file.

    Parameters:
        audio_filename (str): name of the audio file to recognize
        text_filename (str): name of the text file to write recognized text
        model_path (str): Path to vosk model. Default is 'model'.

    Returns:
        None
    '''

    print(f"Reading your file '{audio_filename}'...")
    wf = wave.open(audio_filename, "rb")
    print(f"'{audio_filename}' file was successfully read")

    # check if audio if mono wav
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit()

    print(f"Reading your vosk model '{model_path}'...")
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    print(f"'{model_path}' model was successfully read")

    print('Start converting to text. It may take some time...')
    start_time = time.time()

    results = []
    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)

    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    # forming a final string from the words
    text = ''
    for r in results:
        text += r['text'] + ' '

    time_elapsed = time.strftime(
        '%H:%M:%S', time.gmtime(time.time() - start_time))
    print(f'Done! Elapsed time = {time_elapsed}\n')

    print("\tVosk thinks you said:\n")
    print(text)

    print(f"\nSaving text to '{text_filename}'...")
    with open(text_filename, "w") as text_file:
        text_file.write(text)
    print(f"Text successfully saved")


def main():
    if len(sys.argv) == 1:  # if parameter wasn't specified
        print('Set filename as a parameter. For example:')
        print('>>> python script_vosk.py filename.wav')
        sys.exit()
    elif len(sys.argv) == 2:
        audio_filename = sys.argv[1]
        text_filename = audio_filename[:-3] + 'txt'
    else:
        audio_filename = sys.argv[1]
        text_filename = sys.argv[2]

    if not os.path.exists(audio_filename):
        print(f"File '{audio_filename}' doesn't exist")
        sys.exit()

    if not os.path.exists("model"):
        print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder")
        sys.exit()

    recongize_vosk(audio_filename, text_filename)


if __name__ == "__main__":
    main()
