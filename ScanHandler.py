import requests
import yaml
from requests.structures import CaseInsensitiveDict


def request_scan(url):
    """This function accepts url and scans it for potential harm.
    Returns the response from the scan"""
    with open('config.yml', 'r') as read_config:
        config_file = yaml.full_load(read_config)
        read_config.close()
    api = config_file['API_CONNECTION']['API'] + url
    headers = CaseInsensitiveDict()
    headers["x-apikey"] = config_file['API_CONNECTION']['API_KEY']
    resp = requests.get(api, headers=headers).json()
    return resp


def parse_response(resp):
    """This function accepts response json from the API scan requests
    Returns a list of the essential parameters including risk state, total voting and the domain's'category"""

    data_property = resp["data"][0]
    last_analysis_stats = data_property["attributes"]["last_analysis_stats"]
    total_votes = data_property["attributes"]["total_votes"]
    categories = data_property["attributes"]["categories"]
    parameters_dict = {'analysis': last_analysis_stats, 'votes': total_votes, 'categories': categories}

    return parameters_dict

