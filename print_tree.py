from argument_manager import ArgumentManager
from data_collector import LinkTree
import sys


def main(argv):
    argument_manager = ArgumentManager()
    argument_manager.save_arguments(argv)
    link_tree = LinkTree()
    link_tree.create(argument_manager.page)
    link_tree.print_tree()


if __name__ == '__main__':
    main(sys.argv[1:])
