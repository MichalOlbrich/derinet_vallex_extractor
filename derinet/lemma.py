
from typing import Dict, List
class Lemma:
    id_dict: Dict[str, "Lemma"] = {}
    lemma_dict: Dict[str, "Lemma"] = {}
    def __init__(self, idn, name, pos, tag):
        self.tag = tag
        self.parent = None
        self.is_root: bool = False
        self.children: List["Lemma"] = []
        self.id = idn
        self.derinet_root_id = self.id.split(".")[0] + ".0"
        self.name: str = name
        self.pos = pos
        self.gender = "No"
        self.animacy = "No"
        self.is_loanword: str = "None"
        self.abs_count: int = 0
        self.corp_freq: float = 0
        self.tree_covered_in_segmentation: bool = False
        self.deriv_type = "None"
        self.techlemma = "None"

    def get_num_all_children(self) -> int:
        sum_of_children: int = 0
        if len(self.children) > 0:
            sum_of_children += len(self.children)
            for child in self.children:
                sum_of_children += child.get_num_all_children()
        return sum_of_children

    def __str__(self):
        return self.name

    def add_parent_ref(self, parent_ref: "Lemma"):
        self.parent: Lemma = parent_ref

    def add_child_ref(self, child: "Lemma"):
        self.children.append(child)

    def get_all_predecesors(self):
        if self.parent:
            return self.parent.name + " " + self.parent.get_all_predecesors()
        return ""

    # PRINT FUNCTIONS


    def print_segments(self):
        print(self.name, " [", end=" ")
        for seg in self.segments:
            print(self.name[seg.bounds[0]: seg.bounds[1]], end=" ")
        print("]")

    def print_derinet_segments(self):
        print(self.name, " [", end=" ")
        for seg in self.derinet_segments:
            print(self.name[seg.bounds[0]: seg.bounds[1]], end=" ")
        print("]")

    def print_segments_typed(self):
        print(self.name, " [", end=" ")
        for seg in self.segments:
            print(seg.seg_type.name, ": ", self.name[seg.bounds[0]: seg.bounds[1]], end="\t")
        print("]")

    def print_children(self, spaces=""):
        print(spaces, self.name, "\t", self.pos, "\t", self.id)
        for child in self.children:
            if child.abs_count > 2:
                child.print_children(spaces + " - ")



    def print_children_one_level(self):
        print(self.name, "\t", self.pos, "\t", self.id)
        for child in self.children:
            print(" - ", child.name, "\t", child.pos, "\t", child.id)

    def print_children_seg(self, spaces=""):
        print(spaces, end="")
        self.print_segments()
        for child in self.children:
            child.print_children_seg(spaces + " - ")

    def print_children_seg_typed(self, spaces=""):
        print(spaces, end="")
        self.print_segments_typed()
        for child in self.children:
            child.print_children_seg_typed(spaces + " - ")
