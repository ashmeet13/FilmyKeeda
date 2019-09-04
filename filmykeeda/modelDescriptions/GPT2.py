import logging
import os
import tarfile

import filmykeeda.utils.modelDownload as connection
import gpt_2_simple as gpt2

logging.getLogger().setLevel(logging.INFO)


class GPT2:
    def __init__(self):
        """Initalize the GPT2 model
        """
        self.checkpointFiles = [
            "vocab.bpe",
            "model-1000.meta",
            "model-1000.index",
            "model-1000.data-00000-of-00001",
            "hparams.json",
            "events.out.tfevents.1565109747.6bad2fa838cd",
            "encoder.json",
            "counter",
            "checkpoint",
        ]
        self.checkModelFile()
        logging.info("Model file present!")
        logging.info("Loading model ...")
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(
            self.sess, run_name=self.runFolder, checkpoint_dir=self.modelFolder
        )

    def checkModelFile(self):
        """Check if every necessary file is present in the models
        folder and if not then download and save.
        """
        logging.info("Checking GPT2 Model File ...")
        if not os.path.exists(os.path.join(os.getcwd(), "models")):
            os.mkdir(os.path.join(os.getcwd(), "models"))
        self.modelFolder = os.path.join(os.getcwd(), "models")
        downloadFlag = False
        for checkpointFile in self.checkpointFiles:
            if not os.path.exists(
                os.path.join(self.modelFolder, "GPT2", checkpointFile)
            ):
                downloadFlag = True
                break
        if downloadFlag:
            if os.path.exists(os.path.join(self.modelFolder, "GPT2")):
                os.remove(os.path.join(self.modelFolder, "GPT2"))
            self.downloadCompressedFile()
        self.runFolder = os.path.join(self.modelFolder, "GPT2")

    def downloadCompressedFile(self):
        """Download the compressed model from Google Drive
        """
        logging.warning("File Missing...")
        logging.info("Downloading File...")
        connection.downloadModelFile(
            id="1AVjqBj7xaB2_GrSJUdKqWD2UeTpo8BnS",
            destination=os.path.join(self.modelFolder, "GPT2.tar.gz"),
        )
        self.decompressFile()

    def decompressFile(self):
        """Decompress the model files into the folder.
        """
        logging.info("Extracting File...")
        with tarfile.open(
            os.path.join(self.modelFolder, "GPT2.tar.gz"), "r:gz"
        ) as reader:
            reader.extractall(self.modelFolder)

    def generate(self, text, n_words=1000):
        """Generate GPT2 text from a trained model
        
        Arguments:
            text {str} -- Prompt for the model
        
        Keyword Arguments:
            n_words {int} -- Length of the generated text (default: {1000})
        
        Returns:
            str -- Generated Text
        """
        return gpt2.generate(
            self.sess,
            run_name=self.runFolder,
            checkpoint_dir=self.modelFolder,
            prefix=text,
            length=n_words,
        )
