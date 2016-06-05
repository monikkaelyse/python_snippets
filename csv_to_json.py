#!/usr/bin/python
import csv, json

import sys

files = sys.argv

for file_name in files:
    csvreader = csv.reader(open(file_name, 'rb'), delimiter=',', quotechar='"')
    data = []
    for row in csvreader:
        r_list = []
        json_struct = {}
        if csvreader.line_num == 1:
            headers = row
            continue

        for field in row:

            field = unicode(field, 'ISO-8859-1')

            r_list.append(field)

        for idx, hd in enumerate(headers):
            try:
                val = r_list[idx]
            except:
                val = ''
            json_struct[headers[idx]] = val

        data.append(json_struct)

    open(file_name + '.json', 'wb').write(json.dumps(data))