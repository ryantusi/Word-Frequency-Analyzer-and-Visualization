# WordFrequency Module
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

class WordFrequency:
    def __init__(self, text):
        self.text = text

    def get_frequency(self):
        # tokenizing each word
        tokens = word_tokenize(self._text.lower())

        # Remove punctuation and stopwords
        table = str.maketrans('', '', string.punctuation)
        words = [word.translate(table) for word in tokens if word.isalpha()]

        # Removing stopwords like "the", "is" .etc
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]

        # Count word frequencies
        word_freq = Counter(filtered_words)

        # Display top N most frequent words
        top_words = word_freq.most_common(10)
        top_words = dict(top_words)
        return top_words

    def create_chart(self, top_words):
        if not top_words:
            raise ValueError("Usage: obj.create_chart(top_words)")
        plt.bar(top_words.keys(), top_words.values())
        plt.title('Top 10 Word Frequencies')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("static/barchart.png")

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not text:
            raise ValueError("Enter text to analyze word frequency")
        self._text = text
