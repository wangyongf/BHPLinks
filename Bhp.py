# coding=utf-8

# Baidu Home Page
class Bhp:
    def __init__(self):
        self.bhplinks = []

    def add_link_item(self, link_item):
        self.bhplinks.append(link_item)

    def get_bhp(self):
        return self.bhplinks
