# Hearing Test - Word Recognition
## DISCLAIMER
DISCLAIMER: This is not a medical test by any means. If you suspect that you have hearing problems, please go get professionally tested and diagnosed. The purpose of this tool is for entertainment. Doing poorly on this test may suggest you should seek a professional audiologist for help.

## Purpose
When testing speech audiometry, there is a test where single-syllable words are spoken, and the patient must state what they hear (even if they don't know what it is). I have created this tool based on this word recognition test. For more information, visit this short
[Hopkins Medicine article](https://www.hopkinsmedicine.org/health/conditions-and-diseases/hearing-loss/speech-audiometry).


## Requirements
Currently only tested on `Python 3.11.0`


## Installation
Clone the project and using the PDM lock file, establish your virtual environment to run the project in.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## Usage
Run the `main.py` file via command line. The script will generate a predetermined number of .mp3 samples that will automatically play. You must answer with what you think the stated word is (via enter). The spelling of your response must be identical.

## Future Development
I'd like to swap out the current `gTTS` text generation for something more modern and natural-sounding, probably AI-generated audio.
