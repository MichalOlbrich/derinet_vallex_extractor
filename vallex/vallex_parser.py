import csv
from typing import List, Dict
import re

def read_nom_valex_input(path):
    lines = []
    lemmas = []
    lemmas_se = []
    with open(path) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            lines.append("\t".join(line))
            lemmas.append(line[3].split(" ")[0])
            lemmas_se.append(line[3])
    return lines, lemmas, lemmas_se

