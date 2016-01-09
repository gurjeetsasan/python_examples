#!/usr/bin/python/

import csv

c = csv.writer(open("MYFILE.csv", "wb"))
c.writerow(["Name","Address","Telephone","Fax","E-mail","Others"])



