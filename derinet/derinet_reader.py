import csv
from derinet.lemma import Lemma
import re
from typing import List
import json
import sys


def read(infile):
    with open(infile) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        line: List[str]
        for line in tsv_file:
            if len(line) > 0:
                lemma = Lemma(line[0], line[2], line[3], line[1])
                Lemma.id_dict[line[0]] = lemma
                Lemma.lemma_dict[line[2]] = lemma
                if line[6] != "":
                    if int(re.split("\\.", line[6])[1]) < int(re.split("\\.", line[0])[1]):
                        lemma.add_parent_ref(Lemma.id_dict[line[6]])
                        Lemma.id_dict[line[6]].add_child_ref(lemma)
                else:
                    lemma.is_root = True
                if line[4] != "":
                    features: List[str] = line[4].split("&")
                    feature: str
                    for feature in features:
                        feature_pair = feature.split("=")
                        match feature_pair[0]:
                            case "Loanword":
                                if feature_pair[1] == "True":
                                    lemma.is_loanword = "True"
                                else:
                                    lemma.is_loanword = "False"
                            case "Gender":
                                lemma.gender = feature_pair[1]
                            case "Animacy":
                                lemma.animacy = feature_pair[1]
                json_info = json.loads(line[9])
                if "corpus_stats" in json_info:
                    if "absolute_count" in json_info["corpus_stats"]:
                        lemma.abs_count = json_info["corpus_stats"]["absolute_count"]
                    if "relative_frequency" in json_info["corpus_stats"]:
                        lemma.corp_freq = json_info["corpus_stats"]["relative_frequency"]
                if "techlemma" in json_info:
                    lemma.techlemma = json_info["techlemma"]
                    if line[7] != "":
                        features: List[str] = line[7].split("&")
                    feature: str
                    for feature in features:
                        feature_pair = feature.split("=")
                        match feature_pair[0]:
                            case "Type":
                                lemma.deriv_type = feature_pair[1]
                # if line[5] != "":
                #     morphs: List[str] = line[5].split("|")
                #     # print(lemma.name)
                #     for morph in morphs:
                #         morph_struct: List[str] = morph.split("&")
                #         end: str = morph_struct[0].split("=")[1]
                #         start: str = morph_struct[2].split("=")[1]
                #         if not start.isdigit():
                #             start = morph_struct[3].split("=")[1]
                #         type: str = morph_struct[3].split("=")[1]
                #         lemma.append_derinet_segment(int(start), int(end))

    sys.stderr.write("------ reading done -------")
