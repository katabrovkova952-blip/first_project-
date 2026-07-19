from lection_10.homework_10_2 import first_word
import pytest

@pytest.mark.parametrize("text, expected", [
    pytest.param("Hello world", "Hello", id="simple_sentence"),
    pytest.param(".., and so on ...", "and", id="punctuation marks"),
    pytest.param("don't touch it", "don't", id="with apostrophe")
])
def test_first_word(text, expected):
    assert first_word(text) == expected

@pytest.mark.parametrize("bad_text", [
    pytest.param("", id="empty"),
    pytest.param("...,.. .,", id="only_punctuation"),
    pytest.param("   ", id="only_spaces"),
])
def test_first_word_raises_on_no_words(bad_text):
    with pytest.raises(ValueError):
        first_word(bad_text)


