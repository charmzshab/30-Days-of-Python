import os
import sys
import datetime
import requests
import pandas as pd
from requests_html import HTML


this_file = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file)
# BASE_DIR = os.path.dirname(__file__)


def url_to_txt(url, file_name="world.html", save=False, name=None):
    """
    returns the html content of the website
    """
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{name}.html", "w") as f:
                f.write(html_text)
        return html_text
    return None


def parse_and_extract(url, name="2020"):

    html_text = url_to_txt(url, name)
    if html_text == None:
        return
    r_html = HTML(html=html_text)  # formats the returned html response in to basic html
    table_class = ".imdb-scroll-table"  # html element selector
    # table_class = "#table"
    r_table = r_html.find(table_class)  # finds the specific element from the structure

    # print(r_table)
    table_data = []
    # table_data_dicts=[] ---> dict code

    header_names = []
    if len(r_table) == 0:
        return False
        # print(r_table[0].text)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")  # gets all the table rows --> this is a list
    header_row = rows[
        0
    ]  # retrieves the table header which is the first element in the list
    header_cols = header_row.find("th")
    header_names = [name.text for name in header_cols]

    for row in rows[
        1:
    ]:  # get the remaining row that contain the data without the header
        # print(row.text)
        cols = row.find("td")  # gets all the column cells per row
        row_data = []
        # row_dict_data = {} ---> dict code
        for i, col in enumerate(cols):
            # print(i, col.text, "\n\n")
            row_data.append(col.text)
            # header_name = header_names[i] ---> dict code
            # row_dict_data[header_name] = col.text ---> dict code
        table_data.append(row_data)
        # table_data_dict.append(row_data_dict) ---> dict code
    df = pd.DataFrame(table_data, columns=header_names)
    # df = pd.DataFrame(row_dict_data) ---> dict code
    path = os.path.join(BASE_DIR, "data")
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join("data", f"{name}.csv")
    df.to_csv(filepath, index=False)
    return True
    # print(header_names)
    # print(table_data)


def run(start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago + 1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"{start_year} not finished")
        start_year -= 1

