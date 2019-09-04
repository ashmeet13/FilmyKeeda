import os

import filmykeeda.utils.modelDownload as connection
import sentencepiece as spm
from fastai.basic_train import load_learner
from fastai.text import *


class LangTokenizer(BaseTokenizer):
    """SentencePiece Tokenizer class that is to be imported to use
       ULMFiT model with the SentencePiece Tokenizer.
    """

    def __init__(self, lang, vocab_size: int = 50000):
        self.vocab_size = vocab_size
        self.sp = spm.SentencePieceProcessor()
        self.checkModelFile()
        self.sp.Load(os.path.join("models", "en_lm.model"))
        self.vocab = Vocab([self.sp.IdToPiece(int(i)) for i in range(self.vocab_size)])

    def tokenizer(self, t: str) -> List[str]:
        return self.sp.EncodeAsPieces(t)

    def detokenizer(self, t: List[str]) -> str:
        return self.sp.DecodePieces(t)

    def checkModelFile(self):
        """Will download the neccessary tokenizer model file.
        """
        if not os.path.exists(os.path.join(os.getcwd(), "models", "en_lm.model")):
            connection.downloadModelFile(
                id="1OI-dAcc8XihF-dvDO7Osyu4PxrPHxXZl",
                destination=os.path.join(os.getcwd(), "models", "en_lm.model"),
            )
