# Free and Offline Foreign Speech Recognition

Free and offline foreign (non-English) speech recognition with Python, Google API vosk and SpeechRecognition / Pocketsphinx.

For speech recognition with timestamps see [timestamps folder](https://gitlab.com/Winston-90/foreign_speech_recognition/-/tree/main/timestamps).

![foreign_speech_recognition_preview.jpg](./img/foreign_speech_recognition_preview.jpg)

## Setup

Read [these instructions](https://medium.com/@andimid/offline-foreign-speech-recognition-32d8d63de2dc) to know what library you need to setup and how to do it. They are also available [here](https://gitlab.com/Winston-90/foreign_speech_recognition/-/blob/main/tutorial.md).

- Online speech recognition with Google API:
  - `pip install SpeechRecognition`
- Offline speech recognition with vosk:
  - `pip install vosk`
  - download [vosk model](https://alphacephei.com/vosk/models), unzip it and specify path to the model in program
- Offline Speech Recognition with SpeechRecognition and Pocketsphinx:
  - `pip install SpeechRecognition`
  - `python -m pip install --upgrade pip setuptools wheel`
  - `pip install --upgrade pocketsphinx`
  - download [foreign models for pocketsphinx](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/), unzip and setup it

## Overview Jupyter Notebook

See [overview jupyter notebook](https://gitlab.com/Winston-90/foreign_speech_recognition/-/blob/main/speech_recognition_python.ipynb), which contains examples of all methods.

Open it with [jupyter](https://jupyter.org/) or see directly in a browser.

## Scripts Practical Use 

As any python script any of these tree scripts (`.py` files) can be run with the following command: `python script_name.py parameter1, parameter2 ...`.

Every script has two parameters:
- first (required) - name of the .wav file to recognize
- second (optional) - name of the text file to write recognized text. If not specified, uses `first_parameter.txt`

Examples:
- `python script_online_sr.py audio.wav` (writes text in `audio.txt`)
- `python script_online_sr.py audio.wav audio_outout.txt`
- `python script_vosk.py 'sounds\filename.wav'` (recognize `current_folder\sounds\filename.wav`)
- `python script_offline_sr.py 'D:\sounds\filename.wav'`
