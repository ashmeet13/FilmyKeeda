import os
import re


class dataToList:
    @staticmethod
    def getStrings(contents, directoryPath):
        """Converts the distributed text files inside a folder into a
        cleaned string to save in desired format.
        
        Arguments:
            contents {str} -- Content to read and clean
            directoryPath {str} -- Path to the folder having all text files
        
        Returns:
            [str] -- Cleaned String
        """
        tempStrings = []
        for content in contents:
            if content.endswith(".txt"):
                textFile = os.path.join(directoryPath, content)
                with open(textFile, "r") as reader:
                    for line in reader.readlines():
                        line = line.strip()
                        if not re.match(r"^\s*$", line):
                            tempStrings.append(line)
            else:
                folderPath = os.path.join(directoryPath, content)
                innerFiles = os.listdir(folderPath)
                for innerFile in innerFiles:
                    if not innerFile.endswith(".txt"):
                        continue
                    textFile = os.path.join(folderPath, innerFile)
                    with open(textFile, "r") as reader:
                        for line in reader.readlines():
                            line = line.strip()
                            if not re.match(r"^\s*$", line):
                                tempStrings.append(line)
        return tempStrings
