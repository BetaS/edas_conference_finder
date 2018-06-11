#coding=utf-8
#author: BetaS (k09089@naver.com)

import re
from datetime import datetime
from dateutil.parser import parse


def parse_data(data):
    # split by line

    r = re.compile(r"<tr.*?>([\S\s]*?)</tr>")
    result = r.findall(data)

    return [Item.create(item) for item in result]


class Item:
    @classmethod
    def create(cls, str):
        r = re.compile(r"<td.*?>([\S\s]*?)</td>")
        column = r.findall(str)

        if len(column) == 7:
            id = re.findall(r"showConferenceDetails.php\?c=(\d+?)\"", column[3])[0]
            name = re.findall(r"<abbr.*?>([\S\s]*?)</abbr>", column[1])[0]
            cate = re.findall(r"<div.*?>([\S\s]*?)</div>", column[0])[0]
            location = re.findall(r"<div.*?>([\S\s]*?)</div>", column[4])[0]
            date = parse(re.findall(r"<div.*?>([\S\s]*?)</div>", column[4])[1])
            deadline = datetime.fromtimestamp(int(re.findall(r"\"time.php\?t=(\d+?)\"", column[5])[0]))
            url = re.findall(r"<a.*?href=\"(.*?)\">", column[3])[0]

            return Item(id, name, cate, location, date, deadline, url)
        else:
            return None

    def __init__(self, id, name, cate, location, date, deadline, url):
        self.id = id
        self.name = name
        self.category = cate
        self.location = location
        self.date = date
        self.deadline = deadline
        self.url = url

    def __str__(self):
        return "#"+self.id+"|"+self.name+"|"+self.location+"|"+str(self.get_date())+"|"+str(self.get_deadline())+"|https://edas.info/showConferenceDetails.php?c="+self.id

    def __repr__(self):
        return self.__str__()

    def get_date(self):
        return int(self.date.strftime('%Y%m%d'))

    def get_deadline(self):
        return int(self.deadline.strftime('%Y%m%d'))


def filter_by_category(conference, cate):
    return list(filter(lambda c: any(word.strip().lower() in c.category.lower() for word in cate), conference))


def filter_by_location(conference, location):
    return list(filter(lambda c: any(word.strip().lower() in c.location.lower() for word in location), conference))


def filter_by_date(conference, date):
    return list(filter(lambda c: c.get_date() <= date, conference))


def filter_by_deadline(conference, date):
    return list(filter(lambda c: c.get_deadline() >= date, conference))
