from .modelDescriptions.GPT2 import GPT2
from .modelDescriptions.ULMFiT import ULMFiT


class scripter:
    """Scripter Class - Will produce text generative scripts
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, model="GPT2", tokenizer="fastai"):
        """Set model details and init model class
        
        Keyword Arguments:
            model {str} -- Model to use for script generation (default: {"GPT2"})
            tokenizer {str} -- Tokenizer to use with ULMFiT mode (default: {"fastai"})
        """
        self.model = model
        self.tokenizer = tokenizer
        self.setModelGenerator()

    def setModelGenerator(self):
        """Set model generator that will be used inside Script Generator Class to 
            call model utils for script generation
        """
        if self.model == "ULMFiT":
            self.generator = ULMFiT(self.tokenizer)
        elif self.model == "GPT2":
            self.generator = GPT2()

    def generate(self, text, n_words=1000):
        """ Will call generate module from modelUtils and return a generated script
        
        Arguments:
            text {str} -- Prompt to generate script out of
        
        Keyword Arguments:
            n_words {int} -- Length of the script. (default: {1000})
        
        Returns:
            [str] -- Generated Script
        """
        return self.generator.generate(text, n_words)
