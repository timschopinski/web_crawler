import json
from argument_manager import ArgumentManager
import pandas as pd
from link_tree import LinkTree


class Crawler:

    def __init__(self, argument_manager: ArgumentManager):
        self.argument_manager = argument_manager

    def save(self, data):
        if self.argument_manager.format == 'csv':
            df = pd.DataFrame(data)
            df.to_csv(self.argument_manager.output, index=False)
        elif self.argument_manager.format == 'json':
            with open(self.argument_manager.output, "w", encoding='utf8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)

    def crawl(self):
        link_tree = LinkTree()
        link_tree.create(self.argument_manager.page)
        self.save(link_tree.data)


