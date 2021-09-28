# Free and Offline Foreign Speech Recognition
## with Python and SpeechRecognition, Pocketsphinx libraries

TODO

## SpeechRecognition and Pocketsphinx installation

I will describe the installation process in more detail than usual because I ran into some difficulties and spent quite a lot of time trying to figure them out. Everything can go smoothly in your case, and I will be only happy for you. But a large number of difficulties and the search for sources of their solution just prompted me to write this article.

Actually, we have to install one single library with one single pip command - `pip install SpeechRecognition`. Well, things are not so good.

I didn't have any problems with using Google API, but with the offline `recognize_sphinx()` method I got errors.

Official [pocketsphinx documentation](https://pypi.org/project/pocketsphinx/) tells to run two commands:
- `python -m pip install --upgrade pip setuptools wheel`
- `pip install --upgrade pocketsphinx`

I didn't have any problems with the first one, and again I got an error on the second one.

So first I had to install [swing](http://www.swig.org/index.php) for windows, [here's how I did this](https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed) (note that if you use virtual environment python path will differ).

And then update Microsoft C++ Build Tools, [here's how I did this](https://docs.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html).

After that, you have to be able to use the offline `recognize_sphinx()` method, but only with the English language.

## Foreign Model Download and Setup 

You can [download foreign models for pocketsphinx here](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/). There are 15 languages available now.

For some languages, there are several variants of the model, for others - only one. Click on the selected model and after a few seconds, it will start downloading. Then unzip it - with the `tar` and `gz` format, [free 7zip archiver](https://www.7-zip.org/) can help you. If a model is downloaded in the `model.tar.gz` format, unzip it twice - first from `model.tar.gz` to `model.tar` and then from `model.tar` to `model`. 

As a result, you should get the folder with the following files:
- `.lm` file, 
- `.dic` file, 
- and other files with and without extensions.

Then go to folder where pocketsphinx models are located. In my case (I created virtual enviroment 'venv' with [Anaconda](https://www.anaconda.com/)) this is `C:\Users\USERNAME\anaconda3\envs\venv\Lib\site-packages\speech_recognition\pocketsphinx-data\`.

Here you have to see one folder - `en-US`. Create a folder with the name of the language - `ru-RU` for Russian, `it-IT` for Italian, etc. 

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

A more extended version of this script is available [on GitLab](https://gitlab.com/Winston-90/foreign_speech_recognition). You can use it like: `python foreign_speech_recognition.py audio.wav audio_outout.txt`.

This script has two parameters:
- first (required) - name of the .wav file to recognize (`audio.wav`)
- second (optional) - name of the text file to write recognized text (`audio_outout.txt`). If not specified, uses first_parameter.txt (`audio.txt`)

