# esi_maker

This is a python module to make, load and unzip esi files.

ESI is a lightweight sound source file format that stores a folder of audio files into a single binary file, together with a setting file, where you can customize the mappings between note names and audio file names, and other specific note control informations.

ESI file stores the uncompressed data of each audio file in the folder you specify, and the information to unzip the audio files with their original file names, along with the settings.

ESI stands for `Easy Sampler Instrument`, which is used in [Easy Sampler](https://github.com/Rainbow-Dreamer/easy-sampler) as an audio samples sound source file format, together with SoundFont files and audio files.

For more details about ESI format, you can refer to the musicpy sampler module's wiki, [click here](https://github.com/Rainbow-Dreamer/musicpy/wiki/musicpy-sampler-module#more-about-esi-sound-module-format)

## Installation
Make sure you have installed python >= 3.7 first.

Run `pip install esi_maker` in cmd/terminal.

## Importing
```python
import esi_maker as es
```

## Usage
There are 3 functions in this python module, `make_esi`, `load_esi` and `unzip_esi`.
```python
make_esi(file_path,
         name='untitled.esi',
         settings=None,
         asfile=True,
         name_mappings=None,
         show_msg=True)

# this function will make an esi file at the path that the parameter `name` specified,
# the file extension of the esi file is esi

# file_path: the directory of folder than contains all of the audio files you want to
# include in the esi file

# name: the name of the esi file

# settings: the settings of the esi file, could be a string or a file path of a text file

# asfile: if set to True, then read settings as a file path of a text file, otherwise read as a string

# name_mappings: the dictionary maps note names to audio file names

# show_msg: print progress messages or not


load_esi(file_path, convert=True)

# this function will load a esi file, return an esi class instance

# file_path: the file path of the esi file you want to load

# convert: if set to True, the audio files in the esi file will be converted to
# pydub AudioSegment instances from binary data


unzip_esi(file_path, folder_name=None, show_msg=True)

# this function will unzip the audio files in the esi file to the folder you specify

# file_path: the file path of the esi file you want to unzip the audio files

# folder_name: the path of the folder you want to unzip the audio files to

# show_msg: print progress messages or not
```

The esi class:
```python
esi(samples,
    settings=None,
    name_mappings=None)

# samples: a dictionary which keys are the audio file names, values are the audio file binary data

# settings: the string represents settings

# name_mappings: the dictionary maps note names to audio file names

# file_names: this attribute is an auto-generated dictionary with audio file names
# without file extension maps to audio file names with file extension when an esi instance is initialized
```
