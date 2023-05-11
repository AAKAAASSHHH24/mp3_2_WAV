import os
import sys
from pydub import AudioSegment

# Get the MP3 files folder and output folder from command line arguments
mp3_folder, output_folder = sys.argv[1:]

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Extract the MP3 files using list comprehension
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]

# Loop through all the MP3 files and convert them to WAV
for file_name in mp3_files:
    # Construct the output file path
    wav_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".wav")

    # Convert the MP3 file to WAV and save it
    AudioSegment.from_mp3(os.path.join(mp3_folder, file_name)).export(wav_path, format="wav")
    print(f"Converted {file_name} to {os.path.basename(wav_path)}")
