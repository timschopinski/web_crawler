import json
from copy import deepcopy
import pandas as pd
from argument_manager import ArgumentManager
from crawler import Crawler


def compare_csv(data_path: str = 'csv_files/crawl-results.csv', test_data_path: str = 'csv_files/crawler-test.com.csv'):
    data = pd.read_csv(data_path)
    test_data = pd.read_csv(test_data_path)

    links = data['url'].tolist()
    test_links = test_data['url'].tolist()
    # links.remove('https://crawler-test.com/other/expiring_page_for_removed_test/1665250820.5592597')
    # links.remove('https://crawler-test.com/relativeurl:withcolon')
    # test_links.remove('https://crawler-test.com/other/expiring_page_for_removed_test/1664806911.49134')
    #
    # data.sort_values(["url"], axis=0, ascending=[True], inplace=True)
    # test_data.sort_values(["url"], axis=0, ascending=[True], inplace=True)
    # data = data.reset_index(drop=True)
    # test_data = test_data.reset_index(drop=True)

    # print(data)
    # print(test_data)

    # df = pd.concat([data, test_data])
    # df = df.reset_index(drop=True)
    # df_gpby = df.groupby(list(df.columns))
    # idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
    # df.reindex(idx)
    # print(df)



    # df_diff = pd.concat([data, test_data]).drop_duplicates(keep=False)
    # print(df_diff.values)



    # diff_df = pd.merge(data, test_data, how='outer', indicator='Exist')
    #
    # diff_df = diff_df.loc[diff_df['Exist'] != 'both']
    # print(diff_df)
    #

    # df = pd.merge(data, test_data, left_index=True, right_index=True)
    # print(df)


    # print(f'{data_path} \t {test_data_path}')
    # for link in links:
    #     if link


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