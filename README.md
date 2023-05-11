# MP3 to WAV Converter

This script is designed to convert MP3 files to WAV format using the pydub library. It takes in two command-line arguments: the path to the folder containing the MP3 files, and the path to the folder where the converted WAV files should be saved

### Installation

To use this script, you'll need to have the pydub library installed. You can install it using pip:

pip install pydub
### Usage

To use this script, run the following command:
```python demo.py [MP3 folder path] [output folder path]```

Replace [MP3 folder path] with the path to the folder containing the MP3 files you want to convert, and replace [output folder path] with the path to the folder where you want to save the converted WAV files.

For example, if your MP3 files are stored in a folder called mp3_files and you want to save the converted WAV files in a folder called wav_files, you would run the following command:

```python demo.py mp3_files/ wav_files/```

The script will then convert all MP3 files in the mp3_files folder to WAV format and save them in the wav_files folder.

### Dependencies

This script requires the following dependencies:

`Python 3.x`
`pydub`
`os`
`sys`
