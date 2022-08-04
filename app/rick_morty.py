# -*- coding: utf-8 -*-
__author__ = "SirHades696"
__email__ = "djnonasrm@gmail.com"

from urllib.request import Request, urlopen
import json


def find_characters(page: int) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
    }
    url = "https://rickandmortyapi.com/api/character?page=" + str(page)
    request = Request(url=url, headers=headers)
    url_open = json.loads(urlopen(request).read())
    return url_open["results"]
