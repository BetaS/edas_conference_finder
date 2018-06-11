#!/usr/bin/env python3
#coding=utf-8
#author: BetaS (k09089@naver.com)

import pprint
import operator
import argparse

from src.Conference import *


def find(file, category, location, date, deadline):
    with open(file, "r", encoding="utf-8") as file:
        data = file.read()

        conference = parse_data(data)
        if len(category) > 0:
            conference = filter_by_category(conference, category)
        if len(location) > 0:
            conference = filter_by_location(conference, location)
        if date > 0:
            conference = filter_by_date(conference, date)
        if deadline > 0:
            conference = filter_by_deadline(conference, deadline)

        conference.sort(key=operator.attrgetter('deadline'))

        return conference


if __name__ == "__main__":
    parser = argparse.ArgumentParser("main.py")
    parser.add_argument("-f", "--file", help="HTML code file location (please see the 'sample.txt')", required=True)
    parser.add_argument("-d", "--date", help="filter by conference date from YYMMDD (ex: 181231 = Dec 31st 2018'.)", default="0", type=int)
    parser.add_argument("-D", "--deadline", help="filter by submit deadline from YYMMDD (ex: 181231 = Dec 31st 2018'.)", default="0", type=int)
    parser.add_argument("-c", "--category", help="filter by categories (ex: wireless, communication), accept list", default="")
    parser.add_argument("-l", "--location", help="filter by country or cities (ex: Korea or Seoul), accept list", default="")

    args = parser.parse_args()
    result = find(args.file, args.category.split(","), args.location.split(","), args.date, args.deadline)

    pprint.pprint(result)
    print()
    print("# of conference: " + str(len(result)))