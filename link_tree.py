from typing import List


class LinkTree:

    @classmethod
    def _print_sub_pages(cls, subpage_name: str, num_of_subpages: int, depth: int, index: int, max_depth: int):
        if depth >= max_depth:
            print(f'\t \t {subpage_name}_{index} (0)')
        else:
            print(f'\t {subpage_name} ({num_of_subpages})')

        for num in range(num_of_subpages):
            cls._print_sub_pages(f'subpage{index}', 0, depth+1, num+1, max_depth)

    @classmethod
    def print_tree(cls, data: List[dict]):
        initial_depth = 1
        max_depth = 2
        for index, page in enumerate(data):
            num_of_subpages = page['internal links count']
            if index == 0:
                print(f"Main page ({num_of_subpages})")
            else:
                cls._print_sub_pages(f'subpage{id}', num_of_subpages, initial_depth, index, max_depth)
