# Importing word_frequency module to test
import pytest
from word_frequency import WordFrequency

# Testing constructor and getter
def test_init():
    txt = WordFrequency("demo")
    assert txt.text == "demo"

# Testing get_frequency() function
def test_get_frequency():
    demo = WordFrequency("The quick brown fox jumps over the lazy dog. A quick brown dog jumps over a lazy fox. This is a simple example sentence for word frequency analysis. It demonstrates how the program counts word occurrences.")
    assert demo.get_frequency() == {'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'lazy': 2, 'dog': 2, 'word': 2, 'simple': 1, 'example': 1, 'sentence': 1}

# Testing errors
def test_error():
    with pytest.raises(ValueError):
        error = WordFrequency("")
