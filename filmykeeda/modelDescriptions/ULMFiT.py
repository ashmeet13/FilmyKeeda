import logging
import os

import filmykeeda.utils.modelDownload as connection
from fastai.basic_train import load_learner
from fastai.text import *
from filmykeeda.utils.LangTokenizer import LangTokenizer

logging.getLogger().setLevel(logging.INFO)


class ULMFiT:
    def __init__(self, tokenizer="fastai"):
        """Initalize the ULMFiT model for script generation
        
        Keyword Arguments:
            tokenizer {str} -- Text tokenizer to use for script generation (default: {"fastai"})
                                1. fastai
                                2. sentencepiece
        """
        self.tokenizer = tokenizer
        self.checkModelFile()
        logging.info("Model file present!")
        self.predictor = load_learner(self.modelFolder, self.modelFile)

    def checkModelFile(self):
        """Check for model file to be present. If not download the
        file from google drive
        """
        logging.info("Checking ULMFiT Model File ...")
        if not os.path.exists(os.path.join(os.getcwd(), "models")):
            os.mkdir(os.path.join(os.getcwd(), "models"))
        self.modelFolder = os.path.join(os.getcwd(), "models")
        if self.tokenizer == "fastai":
            if not os.path.exists(os.path.join(self.modelFolder, "enFastAI-lm.pkl")):
                logging.warning("Model file absent")
                logging.info("Downloading file ...")
                connection.downloadModelFile(
                    id="1Q--3r5z55vd8bFltHFok0KFm93QtE45A",
                    destination=os.path.join(self.modelFolder, "enFastAI-lm.pkl"),
                )
            self.modelFile = os.path.join(self.modelFolder, "enFastAI-lm.pkl")

        elif self.tokenizer == "SentencePiece":
            if not os.path.exists(
                os.path.join(self.modelFolder, "enSentencePiece-lm.pkl")
            ):
                logging.warning("Model file absent")
                logging.info("Downloading file ...")
                connection.downloadModelFile(
                    id="1--VGVfm297bPXTTEOrt9-MAtBHlF2orh",
                    destination=os.path.join(
                        self.modelFolder, "enSentencePiece-lm.pkl"
                    ),
                )
            self.modelFile = os.path.join(self.modelFolder, "enSentencePiece-lm.pkl")

    def generate(self, text, n_words=1000):
        """Generate ULMFiT text from a trained model
        
        Arguments:
            text {str} -- Prompt for the model
        
        Keyword Arguments:
            n_words {int} -- Length of the generated text (default: {1000})
        
        Returns:
            str -- Generated Text
        """
        return self.predictor.predict(text, n_words)
