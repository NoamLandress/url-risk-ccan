import datetime


class ScanStats:

    def __init__(self):
        self.url = ''
        self.risk = ''
        self.total_voting = ''
        self.category = ''
        self.time = ''


def stats_scan_data(self, url, parameters_dict):

    set_url(self, url)
    set_category(self, parameters_dict['categories'])
    set_count_votes(self, parameters_dict['votes'])
    set_risk(self, parameters_dict['analysis'])
    set_datetime(self)
    stats = [self.url, self.risk, self.total_voting, self.category, self.time]
    return stats


def set_url(self, url):
    self.url = url


def set_datetime(self):
    self.time = datetime.datetime.now()


def set_category(self, categories):
    """"""
    category_dict = dict.fromkeys(categories.values(),0)
    for category in categories:
        category_dict[categories[category]] += 1
    self.category = str(sorted(category_dict)[0])


def set_count_votes(self, total_votes):
    """"""
    sum_of_votes = 0
    for vote in total_votes:
        sum_of_votes += total_votes[vote]
    self.total_voting = str(sum_of_votes)


def set_risk(self, last_analysis_stats):
    """"""
    risk_count = 0
    for analysis in last_analysis_stats:
        if analysis in ("malicious", "phishing", "malware") and last_analysis_stats[analysis] > 0:
            risk_count += 1
    if risk_count > 0:
        self.risk = "risk"
    else:
        self.risk = "safe"
