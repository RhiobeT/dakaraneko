#!/usr/bin/env python
import json
import argparse
from mal_scrapper import scrap_anime


class JSONFileNotFound(Exception):
    """Raised when the JSON file at the path specified is not found."""


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description="Script to scrap anime"
    )

    parser.add_argument(
        "--workfile",
        help="Path to the work file containing all the work data",
        required=True
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Path of the output of the data scrapped",
        required=True
    )

    args = parser.parse_args()
    path_workfile = args.workfile
    path_output = args.output

    with open(path_workfile, 'r') as f_work:
        with open(path_output, 'r+') as f_output:
            works = json.load(f_work)
            data = json.load(f_output)

            work_list = works['anime']

            for w in work_list:
                title = w['title']
                subtitle = w['subtitle']
                name = title
                if subtitle:
                    name = title + " ~ " + subtitle

                cond1 = name not in data
                #cond2 = name in data and not (
                #        'mal_title' in data[name] and 'link' in data[name])
                if cond1:
                    # Scrap if not already scrapped
                    query = title + " " + subtitle
                    if name in data:
                        query = data[name].get('mal_title', query)
                    print(query)
                    scrap_anime(title, data, query.strip(), json_file_path=path_output, subtitle=subtitle)
