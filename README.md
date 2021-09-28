# Free and Offline Foreign Speech Recognition

Free and offline foreign (non-English) speech recognition with Python and SpeechRecognition / Pocketsphinx.

![preview.jpg](./img/preview.jpg)

## Setup

Read [these instructions](TODO) to know how to install foreign models if you want to do non-English offline speech recognition.

By default, the language parameter is specified to English (`language='en-US'` in 38 line) so you can try it without any additional installation. One library you have to install is [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), you can do it with the simple pip command `pip install SpeechRecognition`.

See the tutorial above to install [Pocketsphinx](https://pypi.org/project/pocketsphinx/) to do offline speech recognition. If you can work online simply replace `recognize_sphinx()` with `recognize_google()` in 38 line. In this case, you don't need to install Pocketsphinx and download foreign models.

## Practical Use

As any python script it can be run with the following command: `python script_name.py parameter1, parameter2 ...`.

This script has two parameters:
- first (required) - name of the .wav file to recognize
- second (optional) - name of the text file to write recognized text. If not specified, uses `first_parameter.txt`

Examples:
- `python foreign_speech_recognition.py audio.wav` (writes text in `audio.txt`)
- `python foreign_speech_recognition.py audio.wav audio_outout.txt`
- `python foreign_speech_recognition.py 'sounds\filename.wav'` (recognize `current_folder\sounds\filename.wav`)
- `python foreign_speech_recognition.py 'D:\sounds\filename.wav'`
