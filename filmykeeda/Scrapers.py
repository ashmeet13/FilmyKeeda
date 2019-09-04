import os

import requests

from bs4 import BeautifulSoup


class scrapers:
    @staticmethod
    def imsdbScraper(link):
        """Scraper for imsdp website
        
        Arguments:
            link {String} -- Link for the movie page with transcript
        
        Returns:
            String -- The movie script
        """
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        script = soup.find("td", {"class": "scrtext"})
        return script.get_text()

    def extract_href(self, linkstr):
        linkstr = linkstr[linkstr.index("href") + 6 :]
        return linkstr[: linkstr.index('"')]

    @staticmethod
    def westWingScraper(obj, dirpath):
        """Scraper for The West Wing Series and save them too
        
        Arguments:
            obj {Self} -- Object of scraper class
            dirpath {os path object} -- Path to directory to save transcripts in
        
        Returns:
            int -- Number of episodes which could not be scraped.
        """
        failCount = 0
        westwingDir = os.path.join(dirpath, "The_West_Wing")
        if not os.path.exists(westwingDir):
            os.mkdir(westwingDir)
        innerLinks = []
        mainLink = "http://westwingwiki.com/the-wiki/scripts/season-"
        for i in range(1, 8):
            link = mainLink + str(i) + "/"
            page = requests.get(link)
            soup = BeautifulSoup(page.content, "html.parser")
            summary = soup.find("div", {"class": "entry-summary"})
            paras = summary.find_all("p")
            for pa in paras:
                innerLinks.append(obj.extract_href(str(pa)))
        innerLinks[
            6
        ] = "http://westwingwiki.com/2014/04/season-1-episode-7-state-dinner/"
        for i in range(len(innerLinks)):
            textFile = os.path.join(westwingDir, "The_West_Wing_" + str(i) + ".txt")
            try:
                with open(textFile, "w") as mainFile:
                    page = requests.get(innerLinks[i])
                    soup = BeautifulSoup(page.content, "html.parser")
                    wrapper = soup.find("div", {"class": "entry-content"})
                    script = wrapper.find("pre")
                    mainFile.write(script.get_text())
            except:
                failCount += 1
                os.remove(textFile)
        return failCount
