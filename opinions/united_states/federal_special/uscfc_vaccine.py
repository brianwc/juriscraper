"""Scraper for the United States Court of Federal Claims
CourtID: uscfc
Court Short Name: Fed. Cl."""

import uscfc


class Site(uscfc.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.url = 'http://www.uscfc.uscourts.gov/aggregator/sources/7'
        self.court_id = self.__module__
        self.back_scrape_iterable = [1]

    def _download_backwards(self, page):
        self.url = 'http://www.uscfc.uscourts.gov/aggregator/sources/7?page=%s' % page
        self.html = self._download()
