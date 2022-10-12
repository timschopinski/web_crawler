from copy import deepcopy
import pandas as pd


def test_compare_csv(data_path: str = 'csv_files/crawl-results.csv',
                     test_data_path: str = 'csv_files/crawler-test.com.csv'):
    """Tests if two csv files are identical and prints the rows that are not equal"""

    collected_data = pd.read_csv(data_path)
    test_data = pd.read_csv(test_data_path)

    collected_data = collected_data.drop('title', axis=1)
    test_data = test_data.drop('title', axis=1)

    collected_data = collected_data.reset_index(drop=True)
    test_data = test_data.reset_index(drop=True)

    df_diff = pd.concat([collected_data, test_data]).drop_duplicates(keep=False)
    print(df_diff)

    assert df_diff['url'].count() == 0


def test_compare_urls(data_path: str = 'csv_files/crawl-results.csv',
                      test_data_path: str = 'csv_files/crawler-test.com.csv'):
    """"""
    collected_data = pd.read_csv(data_path)
    test_data = pd.read_csv(test_data_path)
    links = collected_data['url'].tolist()
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
    assert len(result1) == 0 and len(result2) == 0


def main():
    test_compare_urls()


if __name__ == '__main__':
    main()
