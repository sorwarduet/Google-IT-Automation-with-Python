import os
import csv


def read_the_csv():
    f = open('info.txt')

    csv_file = csv.reader(f)

    for row in csv_file:
        name, phone, address = row
        print('Name:{} Phone:{} Address:{}'.format(name, phone, address))


# read_the_csv()

def write_the_csv():
    hosts = [['workstation.local', '127.0.0.1'], ['cloud', '192.34.56.4']]

    with open('hosts.csv', 'w') as hosts_csv:
        writer = csv.writer(hosts_csv)
        writer.writerows(hosts)


write_the_csv()

import csv


def read_csv_file():
    with open('software.csv') as software:
        reader = csv.DictReader(software)
        for row in reader:
            print('{row["name"]} has {}'.format(row["users"]))

            # read_csv_file()

    users = [
        {'name': 'Sorwar', 'username': 'sorwarduet', 'department': 'CSE'},
        {'name': 'Rahat', 'username': 'rahat', 'department': 'CSE'}
    ]

    def write_csv_dic(users):
        with open('users.csv', 'w') as users_file:
            fieldnames = ['name', 'username', 'department']
            writer = csv.DictWriter(users_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(users)

    write_csv_dic(users)
