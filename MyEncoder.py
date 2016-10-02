# coding=utf-8

import json

from LinkItem import LinkItem
from Url import Url


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, LinkItem):
            # convert object to a dict
            d = {}
            d['category'] = o.category
            d['links'] = o.links
            return d
        elif isinstance(o, Url):
            d = {}
            d['url'] = o.url
            d['title'] = o.title
            return d
        return json.JSONEncoder.default(self, o)
