import re
import csv

with open('comments.csv', 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(filter(lambda x: len(x) > 0, reader))  # Remove blank rows

    for row in rows:
        comment = row[0]
        # Remove any URLs
        comment = re.sub(r'http\S+', '', comment)
        # Remove any special characters, emojis, and numbers
        comment = ''.join(c for c in comment if c.isalpha() or c.isspace())
        row[0] = comment.strip()

with open('comments.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)
