import os
import sys
import time
import speech_recognition as sr
# install with `pip install SpeechRecognition`


def recognize_offline(audio_filename, text_filename, language='en-US'):
    '''
    Recognize audio from 'audio_filename' with offline Sphinx model and 
    write text on the screen and into 'text_filename' file.

    Parameters:
        audio_filename (str): name of the audio file to recognize
        text_filename (str): name of the text file to write recognized text
        language (str): language of the speech. Default is 'en-US'

    Returns:
        None
    '''

    print(f"Reading your file '{audio_filename}'...")
    audio_file = sr.AudioFile(audio_filename)
    r = sr.Recognizer()

    with audio_file as af:
        r.adjust_for_ambient_noise(af)  # clearing sound from noise
        audio = r.record(af)

    print(f"'{audio_filename}' file was successfully read and cleaned from noise")
    print('Start converting to text. It may take some time...')
    start_time = time.time()

    # recognize speech using Sphinx
    try:
        text = r.recognize_sphinx(audio, language=language)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        sys.exit()
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        sys.exit()

    time_elapsed = time.strftime(
        '%H:%M:%S', time.gmtime(time.time() - start_time))
    print(f'Done! Elapsed time = {time_elapsed}\n')

    print("\tSphinx thinks you said:\n")
    print(text)

    print(f"\nSaving text to '{text_filename}'...")
    with open(text_filename, "w") as text_file:
        text_file.write(text)
    print(f"Text successfully saved")


def main():
    if len(sys.argv) == 1:  # if parameter wasn't specified
        print('Set filename as a parameter. For example:')
        print('>>> python script_offline_sr.py filename.wav')
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

    recognize_offline(audio_filename, text_filename)


if __name__ == "__main__":
    main()
