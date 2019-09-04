from filmykeeda import Keeda
from filmykeeda.utils.LangTokenizer import LangTokenizer
import os

scriptWriter = Keeda.getWriter("ULMFiT", tokenizer="SentencePiece")

text = """
FRANCIS
There are two kinds of pain.
Good pain - the sort of pain that motivates, that makes you strong.
Then there’s bad pain - useless pain, the sort of pain that’s only suffering.
I welcome the former. I have no patience for the latter.
"""

word_limit = 1500

print(scriptWriter.generate(text,word_limit))