import re
import requests


def get_url_text(url):
    # TODO: add complex logic and catch errors in GET method
    raw_url_text = requests.get(url).text
    return raw_url_text


def check_main_url(**kwargs):
    raw_url_text = get_url_text(kwargs['main_url'])
    matched_phrases = list(re.findall(kwargs['search_text'], raw_url_text))
    if sum([phrase == kwargs['search_text'] for phrase in matched_phrases]) == kwargs['count_text']:
        return False

    else:
        return True
