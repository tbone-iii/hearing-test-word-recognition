import pytest

import hearing_test.main as hearing_test

PATH = "hearing_test/resources/top-1000-one-syllable-sorted-by-prevalence.txt"


def test_random_sample_has_no_duplicate_words():
    words = hearing_test.get_n_random_words_from_file(10, PATH)
    assert len(set(words)) == len(words)


@pytest.mark.parametrize("n", [0, 10, 100])
def test_acquire_top_n_words_from_file_has_correct_length(n):
    words = hearing_test.get_n_random_words_from_file(n, PATH)
    assert len(words) == n


@pytest.mark.parametrize("word", ["dance", "trot", "eat"])
def test_create_mp3_from_word_with_correct_name(word):
    from pathlib import Path

    test_folder = Path("./test_output")
    file = hearing_test.create_wav_from_word_to_directory(word, test_folder)
    file = Path(file)
    assert file.exists(), "MP3 file does not exist."
    assert file.name == f"{word}.mp3", "File is named incorrectly."

    # Clean up test output folder
    file.unlink()
    test_folder.rmdir()
