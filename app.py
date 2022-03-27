import csv
from html import escape
import io


def read_csv(path, column_names):
    with open(path, newline='') as f:
        # why newline='': see footnote at the end of https://docs.python.org/3/library/csv.html
        reader = csv.reader(f)
        for row in reader:
            record = {name: value for name, value in zip(column_names, row)}
            yield record

def html_table(records):
    # records is expected to be a list of dicts
    column_names = []
    # first detect all posible keys (field names) that are present in records
    for record in records:
        for name in record.keys():
            if name not in column_names:
                column_names.append(name)
    # create the HTML line by line
    lines = []
    lines.append('<table>\n')
    lines.append('  <tr>\n')
    for name in column_names:
        lines.append('    <th>{}</th>\n'.format(escape(name)))
    lines.append('  </tr>\n')
    for record in records:
        lines.append('  <tr>\n')
        for name in column_names:
            value = record.get(name, '')
            lines.append('    <td>{}</td>\n'.format(escape(value)))
        lines.append('  </tr>\n')
    lines.append('</table>')
    # join the lines to a single string and return it
    return ''.join(lines)



    