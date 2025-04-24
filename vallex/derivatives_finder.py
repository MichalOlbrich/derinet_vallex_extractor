
from vallex import vallex_parser
from derinet.lemma import Lemma

def find_derivatives(suffix="ící", vallex_path="./data_sources/vallex/Vendula_3.tsv"):
    lines, lemmas, lemmas_se = vallex_parser.read_nom_valex_input(vallex_path)

    word_dict = {word: i for i, word in enumerate(lemmas)}

    n_of_all_direct = 0
    n_of_all_direct_non_zero = 0
    n_of_all_indirect = 0
    n_of_not_in_derinet = 0
    n_of_all_not_derivative = 0


    for lemma, lemma_se, line in zip(lemmas, lemmas_se, lines):
        if lemma in Lemma.lemma_dict:
            derinet_lemma: Lemma = Lemma.lemma_dict[lemma]
            has_derivative = False
            for child in derinet_lemma.children:
                if child.name.endswith(suffix):
                    print(line +  "\tDIRECT\t" + child.name + "\t" + str(child.abs_count) + "\t" + str(child.corp_freq) + "\t" + child.techlemma+ "\t" + child.tag)
                    if child.abs_count > 0:
                        n_of_all_direct_non_zero +=1
                    n_of_all_direct +=1
                    has_derivative = True
                    break
            # if has_derivative == False:
            #     if (lemma + "elný") in Lemma.lemma_dict:
            #         deriv_lemma =  Lemma.lemma_dict[(lemma + "elný")]
            #         # print(line +  "\tINDIRECT\t" + deriv_lemma.name + "\t" + str(deriv_lemma.abs_count) + "\t" + str(deriv_lemma.corp_freq)+ "\t" + deriv_lemma.techlemma+ "\t" + deriv_lemma.tag)
            #         print(lemma + "\t" + deriv_lemma.name + "\t" + str(deriv_lemma.abs_count) + "\t" + deriv_lemma.parent.name)
            #         n_of_all_indirect +=1
                else:
                    # print(line + "\tNO DERIVATIVE")
                    n_of_all_not_derivative +=1

        else:
            # print(line + "\tLEMMA NOT IN DERINET")
            n_of_not_in_derinet +=1


    print("n_of_all_direct",n_of_all_direct)
    print("n_of_all_direct_non_zero",n_of_all_direct_non_zero)
    print("n_of_all_indirect",n_of_all_indirect)
    print("n_of_all_not_derivative", n_of_all_not_derivative)
    print("n_of_not_in_derinet",n_of_not_in_derinet)

    # print("total",len(lemmas))