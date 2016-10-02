# coding=utf-8


class LinkItem:
    def __init__(self, category):
        self.category = category
        self.links = []

    def add_link(self, link):
        self.links.append(link)
