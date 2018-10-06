#!/usr/bin/env python
import json
import os
import argparse


ANIME_QUERY_NAME = "anime"


class JSONFileNotFound(Exception):
    """Raised when the JSON file at the path specified is not found."""


def dumpworktypes(filepath, workfile_dict):
    """Dump worktypes from dump data file to python dictionnary
    """

    if not os.path.isfile(filepath):
        raise JSONFileNotFound(
                "JSON file at path '{}' not found.".format(filepath))

    with open(filepath, 'r') as f:
        # Parse the json file
        worktype_db = json.load(f)

        anime_pk = 0
        for wt_dict in worktype_db:
            # Retrieve worktypes pk
            query_name = wt_dict['fields']['query_name']
            if query_name == ANIME_QUERY_NAME:
                anime_pk = wt_dict['pk']
                break

        if query_name != ANIME_QUERY_NAME:
            raise Exception("Anime worktype has not been found.")

        # Update workfile dict
        workfile_dict[query_name] = []

        return anime_pk


def dumpworks(filepath, workfile_dict, anime_pk, scrapper_json=None):
    """Dump works from dump data to work dictionnary"""

    if not os.path.isfile(filepath):
        raise JSONFileNotFound(
                "JSON file at path '{}' not found.".format(filepath))

    with open(filepath) as f:
        # Parse the json file
        work_db = json.load(f)

        for w_dict in work_db:
            work_fields = w_dict['fields']

            work_entry = {}
            work_entry['title'] = work_fields['title']
            work_entry['subtitle'] = work_fields['subtitle']

            name = work_entry['title']
            if work_entry['subtitle']:
                name = name + " ~ " + work_entry['subtitle']

            if name in scrapper_json:
                # Add alternative titles

                alt_titles = scrapper_json[name].get(
                        'alternative_titles')
                work_entry['alternative_titles'] = alt_titles

            if anime_pk == work_fields['work_type']:
                # Update workfile dict
                workfile_dict[ANIME_QUERY_NAME].append(work_entry)


def dumpanimefile(
        path_worktype=None,
        path_work=None,
        path_scrapper=None,
        path_output=None):
    """Dump to anime file"""
    workfile_dict = {}

    anime_pk = dumpworktypes(path_worktype, workfile_dict)

    if path_scrapper:
        with open(path_scrapper, 'r') as f_scrp:
            scrap = json.load(f_scrp)
            dumpworks(path_work, workfile_dict, anime_pk, scrapper_json=scrap)
    else:
        dumpworks(path_work, workfile_dict, anime_pk)

    with open(path_output, 'w') as json_file:
        json.dump(workfile_dict, json_file, indent=2, sort_keys=True)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description="Convert Django dump Dakara db into work file"
    )

    parser.add_argument(
        "--path_worktype",
        help="Path of the JSON dump containing worktype data",
        required=True
    )

    parser.add_argument(
        "--path_work",
        help="Path of the JSON dump containing worktype data",
        required=True
    )

    parser.add_argument(
        "--path_scrapper",
        help="Path to the data scrapper",
        default=""
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Path of the work file output",
        required=True
    )

    args = parser.parse_args()
    path_worktype = args.path_worktype
    path_work = args.path_work
    path_scrapper = args.path_scrapper
    path_output = args.output

    dumpanimefile(
            path_worktype=path_worktype,
            path_work=path_work,
            path_scrapper=path_scrapper,
            path_output=path_output)
