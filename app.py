import os
import zipfile
from pydub import AudioSegment
import streamlit as st


def convert_mp3_to_wav(zip_file):
    # Create a new zip file for the converted WAV files
    output_zip = zipfile.ZipFile("converted_wav_files.zip", "w")

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        # Extract the MP3 files from the input zip file
        zip_ref.extractall("input_mp3_files")

    # Convert each MP3 file to WAV format
    for file_name in os.listdir("input_mp3_files"):
        if file_name.endswith(".mp3"):
            mp3_file = os.path.join("input_mp3_files", file_name)
            wav_file = os.path.join("output_wav_files", f"{os.path.splitext(file_name)[0]}.wav")
            AudioSegment.from_file(mp3_file).export(wav_file, format="wav")

            # Add the converted WAV file to the output zip file
            output_zip.write(wav_file)

    # Close the output zip file
    output_zip.close()

    # Clean up the temporary directories
    os.system("rm -rf input_mp3_files output_wav_files")

    return "converted_wav_files.zip"


def main():
    st.title("MP3 to WAV Converter")

    # Get the user's input zip file
    input_zip_file = st.file_uploader("Upload a zip file containing MP3 files", type="zip")

    if input_zip_file is not None:
        # Create a temporary directory to extract the input MP3 files
        os.makedirs("input_mp3_files", exist_ok=True)

        # Create a temporary directory to store the output WAV files
        os.makedirs("output_wav_files", exist_ok=True)

        # Convert the MP3 files to WAV format and return the output zip file
        output_zip_file = convert_mp3_to_wav(input_zip_file)

        # Download the output zip file
        with open(output_zip_file, "rb") as f:
            st.download_button(label="Download Converted WAV Files", data=f.read(), file_name="converted_wav_files.zip")

        # Delete the output zip file
        os.remove(output_zip_file)


if __name__ == "__main__":
    main()
