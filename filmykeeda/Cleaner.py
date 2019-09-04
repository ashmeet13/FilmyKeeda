import os

import pandas as pd
from .utils.dataConverter import dataToList


class cleanerToCSV:
    """Accepts the path to the directory containing scripts
    and converts the text after cleaning to CSV file in a given directory
    """

    def __init__(self, directoryPath, savePath, nConversation=1):
        """Initates the process and saves a CSV file with rows of conversation
        
        Arguments:
            directoryPath {str} -- Path to transcript folder
            savePath {str} -- Path to save CSV file in
        
        Keyword Arguments:
            nConversation {int} -- [description] (default: {1})
        """
        self.directoryPath = directoryPath
        self.contents = os.listdir(directoryPath)
        self.strings = []
        self.stickTogeatherIndex = nConversation
        tempStrings = dataToList.getStrings(self.contents, self.directoryPath)
        self.totalLines = len(tempStrings)
        if self.stickTogeatherIndex == 1:
            self.strings = tempStrings
        else:
            self.makeConversations(tempStrings)
        df = pd.DataFrame(data={"Text": self.strings})
        df.to_csv(os.path.join(savePath, "Sorkin.csv"), index=False)

    def makeConversations(self, tempStrings):
        """Make conversational bundles to save in the CSV rather than
        single line conversation
        
        Arguments:
            tempStrings {List} -- Raw single line conversations from the scripts
        """
        start = 0
        end = self.stickTogeatherIndex
        while end <= self.totalLines:
            text = "\n".join(tempStrings[start:end])
            self.strings.append(text)
            start = start + self.stickTogeatherIndex - 1
            end = start + self.stickTogeatherIndex
        if end > self.totalLines:
            text = "\n".join(tempStrings[start:])
            self.strings.append(text)


class cleanerToText:
    """Accepts the path to the directory containing scripts
    and converts the text after cleaning to .txt file in a given directory
    """

    def __init__(self, directoryPath, savePath):
        """Initates the process and saves a .txt file with lines of conversation
        
        Arguments:
            directoryPath {str} -- Path to transcript folder
            savePath {str} -- Path to save CSV file in
        """
        self.directoryPath = directoryPath
        self.contents = os.listdir(directoryPath)
        self.savePath = os.path.join(savePath, "Sorkin.txt")
        self.strings = dataToList.getStrings(self.contents, directoryPath)
        with open(self.savePath, "w") as writer:
            for string in self.strings:
                writer.write(string)
                writer.write("\n")
