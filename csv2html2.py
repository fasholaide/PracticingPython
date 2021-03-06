#!/usr/bin/env python3

import sys


def main():
    val = process_options()
    if val[0] is None:
        print()##Do nothing
    else:    
        maxwidth = val[0]
        print(maxwidth)
        form = val[1]
        print(form)
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, form)
                count += 1
            except EOFError:
                break
        print_end()

def process_options():
    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("usage:\n{0} [maxwidth=int] [format=str] < infile.csv > outfile.html".format(sys.argv[0]))
            return [None, None]
        maxWidth = 100
        formatted = ".0f"
        maxi = str()
        form = str()
        if len(sys.argv) == 3:
            if sys.argv[1].startswith("maxwidth"):
                maxi = sys.argv[1].split("=")[1]
            if sys.argv[1].startswith("format"):
                form = sys.argv[1].split("=")[1]
            if sys.argv[2].startswith("maxwidth"):
                maxi = sys.argv[2].split("=")[1]
            if sys.argv[2].startswith("format"):
                form = sys.argv[2].split("=")[1]

            if int(maxi):
                maxWidth = int(maxi)
            if form is not None:
                formatted = form
        return [maxWidth, formatted]
    except IndexError:
        print("usage:\n{0} [maxwidth=int] [format=str] < infile.csv > outfile.html".format(sys.argv[0]))

def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, form):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x), form))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(
                            escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def print_end():
    print("</table>")


main()
