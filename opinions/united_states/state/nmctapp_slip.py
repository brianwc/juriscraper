import nm_p


class Site(nm_p.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.url = 'http://www.nmcompcomm.us/nmcases/NMCASlip.aspx'
        self.court_id = self.__module__

    def _get_docket_numbers(self):
        path = '//table[@id="GridView1"]/tr/td[3]//text()'
        return list(self.html.xpath(path))

    def _get_neutral_citations(self):
        return None
