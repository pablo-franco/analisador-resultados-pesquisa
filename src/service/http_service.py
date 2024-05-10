import requests

from src.service.enum import SearchType

google_tbm_param = {
    SearchType.ALL: '',
    SearchType.IMAGE: 'isch',
    SearchType.NEWS: 'nws',
    SearchType.VIDEO: 'vid'
}

def google_search(search_text, search_type):
    uri = 'https://www.google.com/search'
    search_parameters = f'?q={search_text.replace(' ', '+')}'
    tbm = f'&tbm={google_tbm_param[search_type]}' if google_tbm_param[search_type] else ''
    full_path = uri + search_parameters + tbm
    response = requests.get(full_path)
    return response.text