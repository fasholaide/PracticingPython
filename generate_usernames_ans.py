#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User",
            "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(),
                       user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9
    count = 0
    name_str = "NAME"
    id_str = "ID"
    username_str = "USERNAME"
    heading = "{0:<{nw}} {1:^6} {2:{uw}} {0:<{nw}} {1:^6} {2:{uw}}".format(name_str, id_str, username_str, nw=namewidth, uw=usernamewidth)
    lining = "{0:-<{nw}} {0:-<6} {0:-<{uw}} {0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth)
    print(heading)
    print(lining)
    
    names = []
    usernames = []
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        names.append(name)	
        usernames.append(user)

    for named1, usernamed1, named2, usernamed2 in zip(names[::2], usernames[::2], names[1::2], usernames[1::2]):
        if count >= 64:
            count = 0;
            print()
            print(heading)
            print(lining)
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}} {2:.<{nw}} ({3.id:4}) {3.username:{uw}}".format(
              named1, usernamed1, named2, usernamed2, nw=namewidth, uw=usernamewidth))
        count += 1


main()
