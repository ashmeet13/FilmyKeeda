import logging
import os

import requests

from bs4 import BeautifulSoup
from .Scrapers import scrapers

logging.getLogger().setLevel(logging.INFO)


class download:
    """Will download all the transcripts by Aaron Sorking of the movies/series
    specified by the user.
    
    Raises:
        ValueError: names not specified as list or string(in case of one item to download)
    """

    def __init__(self, names, dataPath=None, verbose=False):
        """Initalise the downloading of transcripts by making sure
        movie names have been recieved and the directory is made in
        which the data is to be stored
        
        Arguments:
            names {String/List} -- [Names of the Movies/Series to download transcipts of]
        
        Keyword Arguments:
            dataPath {os path object} -- [Path to the directory to store downloaded transcripts] (default: {None})
            verbose {bool} -- [Show download details] (default: {False})
        
        Raises:
            ValueError: names not specified as list or string(in case of one item to download)
        """
        self.dataPath = dataPath
        self.directory_init()
        self.verbose = verbose
        if isinstance(names, str):
            self.names = [names]
        elif isinstance(names, list):
            self.names = names
        else:
            raise ValueError("Name should be list or string")
        self.scrape_iter()

    def directory_init(self):
        """Initalise the directory and set it up to store the scraped results in
        """
        if self.dataPath is None:
            cwd = os.getcwd()
            self.dataPath = os.path.join(os.path.dirname(cwd), "Data")
        if not os.path.exists(self.dataPath):
            os.mkdir(self.dataPath)

    def scrape_iter(self):
        """Start scraping the movies specified by the user
        """
        if self.verbose:
            logging.info(self.names)
        for name in self.names:
            if self.verbose:
                logging.info("Scraping:", name)
            if name == "The West Wing":
                failCount = scrapers.westWingScraper(scrapers(), self.dataPath)
                if self.verbose:
                    logging.info("Failed Scraping", failCount, "episodes...")
            elif name == "The Social Network":
                scriptFile = os.path.join(
                    self.dataPath, name.replace(" ", "_") + ".txt"
                )
                with open(scriptFile, "w") as file:
                    file.write(
                        scrapers.imsdbScraper(
                            "https://www.imsdb.com/scripts/Social-Network,-The.html"
                        )
                    )
            elif name == "A Few Good Men":
                scriptFile = os.path.join(
                    self.dataPath, name.replace(" ", "_") + ".txt"
                )
                with open(scriptFile, "w") as file:
                    file.write(
                        scrapers.imsdbScraper(
                            "https://www.imsdb.com/scripts/A-Few-Good-Men.html"
                        )
                    )
            elif name == "The American President":
                scriptFile = os.path.join(
                    self.dataPath, name.replace(" ", "_") + ".txt"
                )
                with open(scriptFile, "w") as file:
                    file.write(
                        scrapers.imsdbScraper(
                            "https://www.imsdb.com/scripts/American-President,-The.html"
                        )
                    )
            else:
                logging.warning("Transcript not available:", name)
