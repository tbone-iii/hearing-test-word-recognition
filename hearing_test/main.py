import random
from pathlib import Path

from gtts import gTTS
from pygame import mixer

OUTPUT_FOLDER_NAME = "output"
OUTPUT_FOLDER_PATH = Path(__file__).parent / Path(OUTPUT_FOLDER_NAME)

mixer.init()


def create_directory_folder_if_not_exists(directory: Path):
    if not directory.exists():
        directory.mkdir()


def get_n_random_words_from_file(n: int, path: str | Path) -> list[str]:
    words = []
    with open(path) as file:
        words = file.read().splitlines()

    return random.sample(words, n)


def create_wav_from_word_to_directory(word: str, directory: str | Path) -> Path:
    path_directory = Path(directory)
    create_directory_folder_if_not_exists(path_directory)

    file_path = path_directory / f"{word}.mp3"
    if file_path.exists():  # skip unnecessary reproduction
        return file_path

    tts = gTTS(text=word, lang="en")
    tts.save(file_path)

    return file_path


def main():
    NUMBER_OF_WORDS = 10

    # Get the words from the list
    words = get_n_random_words_from_file(
        NUMBER_OF_WORDS,
        OUTPUT_FOLDER_PATH.parent
        / "resources/top-1000-one-syllable-sorted-by-prevalence.txt",
    )

    # Create the word MP3s
    mp3_paths = [
        create_wav_from_word_to_directory(word, OUTPUT_FOLDER_PATH) for word in words
    ]

    # Play each MP3 on a loop, recording answers
    responses = []
    for path in mp3_paths:
        # play sound
        mixer.music.load(str(path))
        mixer.music.play()

        # capture response
        response = input("What word was just said? ")
        responses.append(response)

    # Display results
    results = []
    for word, response in zip(words, responses):
        print(f"YOU SAID:\t{response}")
        print(f" IT WAS :\t{word}")
        print()
        results.append(word == response)

    grade = round(sum(results) / len(words), 3) * 100
    print(f"Your results: {grade}% comprehension")


if __name__ == "__main__":
    main()
