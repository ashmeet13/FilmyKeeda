from filmykeeda import Keeda
import os

scriptWriter = Keeda.getWriter("GPT2")

text = """
FRANCIS
There are two kinds of pain.
Good pain - the sort of pain that motivates, that makes you strong.
Then there’s bad pain - useless pain, the sort of pain that’s only suffering.
I welcome the former. I have no patience for the latter.
"""


scriptWriter.generate(text,1500)