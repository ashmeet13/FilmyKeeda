from filmykeeda import Keeda
import os


path = os.path.join("Data")
scripts = [
    "The Social Network",
    "A Few Good Men",
    "The American President",
    "The West Wing"
]
Keeda.download(scripts, path, True)
Keeda.getCSV(path,os.getcwd())
Keeda.getText(path,os.getcwd())