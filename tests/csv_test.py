from copy import deepcopy
import pandas as pd


def compare_csv(data_path: str = 'csv_files/crawl-results.csv', test_data_path: str = 'csv_files/crawler-test.com.csv'):
    data = pd.read_csv(data_path)
    test_data = pd.read_csv(test_data_path)

    links = data['url'].tolist()
    test_links = test_data['url'].tolist()

    result1 = deepcopy(test_links)
    result2 = deepcopy(links)

    [result1.remove(link) for link in test_links if link in links]
    [result2.remove(link) for link in links if link in test_links]

    print(f'Links length: {len(links)}')
    print(f'Test Links length: {len(test_links)}')
    print(f'Test Links Left {result1}')
    print(f'Links Left {result2}')
    print(f'Test Link urls left {len(result1)}')
    print(f'Link urls left {len(result2)}')


def main():
    compare_csv()


if __name__ == '__main__':
    main()