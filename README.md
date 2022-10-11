
## Web Crawler

This app is build as CLI.
The main goal for this app is to fetch and process data from the specified website and all its subpages linked from the main page and subpages of subpages etc.


---

## Introduction

This app uses asynchronous requests to fetch all the subpages in a recurrent way.
It stores than the data in a specified CSV or JSON file.
There is also an option to print the structure of the page as a tree.
The data of scraped pages contains link, title, number of internal links, number of external links, number of times url was referenced by other pages.
For simplicity links that start with http are counted as external links.



## Documentation


#### crawl.py --page 'url' --format 'csv/json' --output 'output'
This script fetches subpages from the given 'url'. Results are saved in 'csv/json' format in 'output'
where each row is representing one page, with the following columns/keys:
<br>
&#x2022; link
<br>
&#x2022; title
<br>
&#x2022; number of internal links
<br>
&#x2022; number of external links
<br>
&#x2022; number of times url was referenced by other pages*

#### print_tree.py --page 'url'
This script prints the structure of the page as a tree in the following format:
Main page (5)
<br>
&nbsp; subpage1 (2)
<br>
&nbsp;&nbsp;&nbsp; subpage1_1 (0)
<br>
&nbsp;&nbsp;&nbsp; subpage1_2 (0)
<br>
&nbsp; subpage2 (1)
<br>
 &nbsp;&nbsp;&nbsp;  subpage2_1 (0)

There are also two additional arguments:

--allow_redirects, the redirects are also fetched by default is set to False 

--max_depth, maximum depth of subpages, by default is set to 2

Example:

crawl.py --page 'url' --format 'csv/json' --output 'output' --max_depth 3 --allow_redirects


## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2022, Tim Schopinski 