# Free and Offline Foreign Speech Recognition with Python

## Introduction

In this tutorial, I will show you how to setup Python speech recognition libraries ([vosk](https://pypi.org/project/vosk/), [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) and [Pocketsphinx](https://pypi.org/project/pocketsphinx/)) to work offline with foreign (non-English) languages. 

Important! Read the next sentences carfully to now what library you need to setup:
- If **online speech recognition** is enough for you (you have access to the Internet), use *SpeechRecognition* library with Google API. Go to **Online Speech Recognition with SpeechRecognition** section.
- If you need **offline speech recognition**, you can install *Vosk* library OR *Pocketsphinx*. And finally, if you want to recognize **foreign (non-English) language offline**, you can use *Vosk* or *Pocketsphinx* with foreign model. Vosk library is easier to setup. Go to **Offline Speech Recognition with Vosk** OR **Offline Speech Recognition with SpeechRecognition and Pocketsphinx** sections.

![speech_recognition_library_selection.jpg](./img/speech_recognition_library_selection.jpg)

So as not to waste your time in this article I will decribe only installation process with minor examples. In the end of each section I will provide you links where you can learn more about speech recognition with particular library.

## Online Speech Recognition with SpeechRecognition

This is the easiest way. If you have access to the Internet, you can simply use Google API. **This also will allow you to work with different languages** by just setting the `language` parameter. 

All you need to do - install *SpeechRecognition* library with `pip install SpeechRecognition`. Then you can recognize audio with the next code:

```python
import speech_recognition as sr 

italian_audio = sr.AudioFile('italian_audio.wav')
r = sr.Recognizer()

with italian_audio as af:
    audio = r.record(af)

text = r.recognize_google(audio, language='it-IT')
print(f"Google thinks you said:\n {text}")
```

More information:
- [Introduction to Speech Recognition with Python](https://stackabuse.com/introduction-to-speech-recognition-with-python/)
- [The Ultimate Guide To Speech Recognition With Python](https://realpython.com/python-speech-recognition/)

## Offline Speech Recognition with Vosk

Vosk is offline speech recognition tool and it's easy to setup. First, you need install vosk with pip command - `pip install vosk`. If you have trouble installing, upgrade your pip / Python (see [Installation section on vosk site](https://alphacephei.com/vosk/install)).

Then you have [to download model](https://alphacephei.com/vosk/models) just simly clicking on it. If your model is not downloading for some reason, copy the link and open it in new window (for some reason it works). 

TODO gif with downloading

The recognition language will depend on the model you download. Then you need unpack model in some folder and you can use it. Vosk models output result in *json* format - this can be confusing for beginners, but allow you do **speech recognition with timestamps**. See GitLab repo for more code comments.

```python
import wave
import json
from vosk import Model, KaldiRecognizer

wf = wave.open('foreign_audio.wav', "rb")
model = Model('model')
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

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

print(f"Vosk thinks you said:\n {text}")
```

More information:
- [Vosk site](https://alphacephei.com/vosk/)
- [Vosk github repo](https://github.com/alphacep/vosk-api)

## Offline Speech Recognition with SpeechRecognition and Pocketsphinx

This is the most difficult way. At least here I got the largest number of errors. However, maybe vosk doesn't support your language, or you have your own reasons.

To use offline `recognize_sphinx()` method in *SpeechRecognition* library you have to install *Pocketsphinx*. Official [pocketsphinx documentation](https://pypi.org/project/pocketsphinx/) tells to run two commands:
- `python -m pip install --upgrade pip setuptools wheel`
- `pip install --upgrade pocketsphinx`

I got an error on the second one. so first I had to install [swing](http://www.swig.org/index.php) for windows, [here's how I did this](https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed) (note that if you use virtual environment python path will differ).

And then update Microsoft C++ Build Tools, [here's how I did this](https://docs.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html).

After that, you have to be able to use the offline `recognize_sphinx()` method, but only with the English language. So now you have to download and setup foreign pocketsphinx model.

You can [download foreign models for pocketsphinx here](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/). There are 15 languages available now.

For some languages, there are several variants of the models, for others - only one. Click on the selected model and after a few seconds, it will start downloading. Then unzip it - with the `tar` and `gz` format, [free 7zip archiver](https://www.7-zip.org/) can help you. If a model is downloaded in the `model.tar.gz` format, unzip it twice - first from `model.tar.gz` to `model.tar` and then from `model.tar` to `model`. 

As a result, you should get the folder with the following files:
- `.lm` file, 
- `.dic` file, 
- and other files with and without extensions.

Then go to folder where pocketsphinx models are located. In my case (I created virtual enviroment 'venv' with [Anaconda](https://www.anaconda.com/)) it is `C:\Users\USERNAME\anaconda3\envs\venv\Lib\site-packages\speech_recognition\pocketsphinx-data\`.

There you have to see one folder - `en-US`. Create a folder with the name of the language - `ru-RU` for Russian, `it-IT` for Italian, etc. See [other languages codes here](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134).

Into your folder, copy and rename `.lm` file to `language-model.lm.bin` and `.dic` file to `pronounciation-dictionary.dict`.

Then create the `acoustic-model` folder and copy all other files there (`feat.params, mdef, means, mixture_weights, noisedict, sendump, transition_matrices, variances`).

The final folder structure for the Russian language is: 

```
├───pocketsphinx-data
│   ├───en-US
│   │   ...
│   │   └───acoustic-model
│   └───ru-RU
│       ├───language-model.lm.bin
│       ├───pronounciation-dictionary.dict
│       └───acoustic-model
│           ├───feat.params  
│           ├───mdef  
│           ├───means  
│           ├───mixture_weights  
│           ├───noisedict  
│           ├───sendump  
│           ├───transition_matrices
│           └───variances
```

See [this github issue](https://github.com/Uberi/speech_recognition/issues/192) to know more. Official [speech_recognition](https://github.com/Uberi/speech_recognition) and [pocketsphinx](https://github.com/bambocher/pocketsphinx-python) repositories and [sphinx site](https://cmusphinx.github.io/) can also help you.

## Practical Use

If you did everything right, now you can use the `recognize_sphinx()` method by just setting the `language` parameter:

```python
import speech_recognition as sr 

audio_file = sr.AudioFile('foreign_audio.wav')
r = sr.Recognizer()

with audio_file as af:
    audio = r.record(af)

text = r.recognize_sphinx(audio, language='ru-RU')
print(f"Sphinx thinks you said:\n {text}")
```

A more extended version of this script is available [on GitLab](https://gitlab.com/Winston-90/foreign_speech_recognition). You can use it like any other python script. This script has two parameters:
- first (required) - name of the .wav file to recognize (`audio.wav`)
- second (optional) - name of the text file to write recognized text (`audio_outout.txt`). If not specified, uses first_parameter.txt (`audio.txt`)

For example `python foreign_speech_recognition.py audio.wav audio_outout.txt` command will recognize `audio.wav` file from the current folder and write the recognized text into `audio_outout.txt` file.

## Conclusions

It was the number of difficulties that prompted me to write this article. You may not encounter these problems or encounter others. Anyway, feel free to contact me if you have any problems. Maybe I can help you.

If you are native speaker accuracy can be very good, but if you are not it can be awful.