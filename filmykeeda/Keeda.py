from .Cleaner import cleanerToCSV, cleanerToText
from .Download import download
from .Scripter import scripter


def downladData(nameList, dataPath=None, verbose=False):
    """Function to initate download of all the transcripts in
    a specified folder.
    
    Arguments:
        nameList {List/Str} -- Name(s) of all the movie(s)/series of which
                            transcripts are to be scraped of
    
    Keyword Arguments:
        dataPath {str} -- Path where the transcript folder is to be saved (default: {None})
        verbose {bool} -- Show details of current download (default: {False})
    """
    download(nameList, dataPath)


def getCSV(directoryPath, savePath, sticky=1):
    """Function to convert all the seperated transcripts into a signle CSV File
    
    Arguments:
        directoryPath {str} -- Path to folder with transcripts
        savePath {str} -- Path to save the CSV at
    
    Keyword Arguments:
        sticky {int} -- [Value of how many lines to be bundled togeather in a single row] (default: {1})
    """
    cleanerToCSV(directoryPath, savePath, sticky)


def getText(directoryPath, savePath):
    """Function to convert all the seperated transcripts into a signle .txt File
    
    Arguments:
        directoryPath {str} -- Path to folder with transcripts
        savePath {str} -- Path to save the .txt at
    """
    cleanerToText(directoryPath, savePath)


def getWriter(model, tokenizer="fastai"):
    """Intiates a scrip writer object necessary for script
    generation
    
    Arguments:
        model {str} -- Parameter to set the type of model to use
                        1. FastAI - ULMFiT
                        2. OpenAI - GPT2
    
    Keyword Arguments:
        tokenizer {str} -- Parameter to set the tokenizer to use with (default: {"fastai"})
                        ULMFiT model
                            1. Default FastAI Tokenizer
                            2. Sentence Peice Tokenizer
    Returns:
        [scripter object] -- Object to generate scripts.
    """
    return scripter(model, tokenizer)
