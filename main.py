import argparse
import csv
import re
import unicodedata

forms = str.maketrans({"\u0623": "\u0627", "\u0625": "\u0627", "\u0622": "\u0627", "\u0671": "\u0627",
                       "\u0649": "\u064a", "\u0640": ""})

def fold(text):
    text = unicodedata.normalize("NFKC", text).translate(forms)
    text = re.sub(r"[\u064b-\u065f\u0670]", "", text)
    return " ".join(text.casefold().split())

parser = argparse.ArgumentParser(description="Add Arabic search keys to CSV")
parser.add_argument("source")
parser.add_argument("column")
parser.add_argument("target")
args = parser.parse_args()
try:
    with open(args.source, encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames or []
        if (args.column not in fields or "search_key" in fields
                or len(set(fields)) != len(fields)):
            raise ValueError("Check the source column, duplicate headers and search_key")
        rows = []
        for row in reader:
            if None in row or None in row.values():
                raise ValueError(f"Malformed row near line {reader.line_num}")
            row["search_key"] = fold(row[args.column])
            rows.append(row)
    with open(args.target, "x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=[*fields, "search_key"])
        writer.writeheader()
        writer.writerows(rows)
except (OSError, ValueError, csv.Error) as error:
    parser.exit(1, f"{error}\n")
