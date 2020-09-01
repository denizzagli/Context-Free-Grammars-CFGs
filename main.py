# The libraries used in this assignment are below. I just needed the random library.

import random

#################################### Part 1: Language Generation with CFG ##############################################

# The dataset function opens the file in the pattern it takes as a parameter first. Then, it processes the necessary
# information about CFG and creates a dictionary using this information. Returns the dictionary containing all CFG
# rules. At the end of the process, the opened file, which is given as a path, is closed.

def dataset(filePath):
    input_file = open(filePath, "r")
    ROOT = []
    S = []
    VP = []
    NP = []
    PP = []
    Noun = []
    Verb = []
    Det = []
    Adj = []
    Prep = []
    Pronoun = []
    for line in input_file.readlines():
        line = line.rstrip("\n")
        list_temp = line.split("\t")
        if list_temp[0] == "ROOT":
            ROOT.append(list_temp[1])
        if list_temp[0] == "S":
            S.append(list_temp[1])
        if list_temp[0] == "VP":
            VP.append(list_temp[1])
        if list_temp[0] == "NP":
            NP.append(list_temp[1])
        if list_temp[0] == "PP":
            PP.append(list_temp[1])
        if list_temp[0] == "Noun":
            Noun.append(list_temp[1])
        if list_temp[0] == "Verb":
            Verb.append(list_temp[1])
        if list_temp[0] == "Det":
            Det.append(list_temp[1])
        if list_temp[0] == "Adj":
            Adj.append(list_temp[1])
        if list_temp[0] == "Prep":
            Prep.append(list_temp[1])
        if list_temp[0] == "Pronoun":
            Pronoun.append(list_temp[1])
    CFG = {}
    CFG["ROOT"] = ROOT
    CFG["S"] = S
    CFG["VP"] = VP
    CFG["NP"] = NP
    CFG["PP"] = PP
    CFG["Noun"] = Noun
    CFG["Verb"] = Verb
    CFG["Det"] = Det
    CFG["Adj"] = Adj
    CFG["Prep"] = Prep
    CFG["Pronoun"] = Verb
    input_file.close()
    return CFG

# The CFG rules that the dataset function returns are given below as an example.

# {'ROOT': ['S .', 'S !', 'is it true that S ?'], 'S': ['NP VP'], 'VP': ['Verb NP'], 'NP': ['Det Noun', 'Pronoun',
# 'NP PP'], 'PP': ['Prep NP'], 'Noun': ['Adj Noun', 'president', 'sandwich', 'pickle', 'mouse', 'floor'], 'Verb': ['ate'
# , 'wanted', 'kissed', 'washed', 'pickled', 'is', 'prefer', 'like', 'need', 'want'], 'Det': ['the', 'a', 'every',
# 'this', 'that'], 'Adj': ['fine', 'delicious', 'beautiful', 'old'], 'Prep': ['with', 'on', 'under', 'in', 'to', 'from']
# , 'Pronoun': ['ate', 'wanted', 'kissed', 'washed', 'pickled', 'is', 'prefer', 'like', 'need', 'want']}

# This function allows us to create random sentences. It allows us to form gramatically correct sentences by making
# random options within the determined rules. It is a recursive algorithm. Two nested functions are defined. The parent
# function creates a list to hold the words that will form the sentence and enlarges and returns the first letter of the
# sentence resulting from the recursive algorithm. Recursive algorithm, on the other hand, tries to produce sentences
# starting from the rule. Of course, the parameter must be S or ROOT to be a sentence.

def random_sentence_generator(CFG):
    sentence = []
    def sentence_generator(CFG, rule):
        if rule not in list(CFG.keys()):
            return rule
        else:
            str_temp = random.choice(CFG[rule])
            list_temp = str_temp.split(" ")
            for item in list_temp:
                result = sentence_generator(CFG, item)
                sentence.append(result)
    sentence_generator(CFG, "ROOT")
    sentence = [i for i in sentence if i]
    result = ""
    for item in sentence:
        result = result + item + " "
    result = result[:-1]
    result = result.capitalize()
    return result

# Example random sentences created:

# Is it true that pickled washed like ?
# Is it true that a pickle wanted kissed ?
# Every president kissed that floor !

# Test function of Part 1

def test_part1():
    CFG = dataset("cfg.gr")
    sentence = random_sentence_generator(CFG)
    print(sentence)

########################################################################################################################

#################################### Part 2: Parsing Sentences with CYK Parser #########################################

# The dataset function opens the file in the pattern it takes as a parameter first. Then, it processes the necessary
# information about CFG and creates a dictionary using this information. Returns the dictionary containing all CFG
# rules. At the end of the process, the opened file, which is given as a path, is closed. It is exactly the same with
# the dataset function of Part 1.

def rules(folderPath):
    input_file = open(folderPath, "r")
    ROOT = []
    S = []
    VP = []
    NP = []
    PP = []
    Noun = []
    Verb = []
    Det = []
    Adj = []
    Prep = []
    Pronoun = []
    for line in input_file.readlines():
        line = line.rstrip("\n")
        list_temp = line.split("\t")
        if list_temp[0] == "ROOT":
            ROOT.append(list_temp[1])
        if list_temp[0] == "S":
            S.append(list_temp[1])
        if list_temp[0] == "VP":
            VP.append(list_temp[1])
        if list_temp[0] == "NP":
            NP.append(list_temp[1])
        if list_temp[0] == "PP":
            PP.append(list_temp[1])
        if list_temp[0] == "Noun":
            Noun.append(list_temp[1])
        if list_temp[0] == "Verb":
            Verb.append(list_temp[1])
        if list_temp[0] == "Det":
            Det.append(list_temp[1])
        if list_temp[0] == "Adj":
            Adj.append(list_temp[1])
        if list_temp[0] == "Prep":
            Prep.append(list_temp[1])
        if list_temp[0] == "Pronoun":
            Pronoun.append(list_temp[1])
    CFG = {}
    CFG["ROOT"] = ROOT
    CFG["S"] = S
    CFG["VP"] = VP
    CFG["NP"] = NP
    CFG["PP"] = PP
    CFG["Noun"] = Noun
    CFG["Verb"] = Verb
    CFG["Det"] = Det
    CFG["Adj"] = Adj
    CFG["Prep"] = Prep
    CFG["Pronoun"] = Verb
    return CFG

# The CFG rules that the dataset function returns are given below as an example.

# {'ROOT': ['S .', 'S !', 'is it true that S ?'], 'S': ['NP VP'], 'VP': ['Verb NP'], 'NP': ['Det Noun', 'Pronoun',
# 'NP PP'], 'PP': ['Prep NP'], 'Noun': ['Adj Noun', 'president', 'sandwich', 'pickle', 'mouse', 'floor'], 'Verb': ['ate'
# , 'wanted', 'kissed', 'washed', 'pickled', 'is', 'prefer', 'like', 'need', 'want'], 'Det': ['the', 'a', 'every',
# 'this', 'that'], 'Adj': ['fine', 'delicious', 'beautiful', 'old'], 'Prep': ['with', 'on', 'under', 'in', 'to', 'from']
# , 'Pronoun': ['ate', 'wanted', 'kissed', 'washed', 'pickled', 'is', 'prefer', 'like', 'need', 'want']}

# This function allows us to create random sentences. It allows us to form gramatically correct sentences by making
# random options within the determined rules. It is a recursive algorithm. Two nested functions are defined. The parent
# function creates a list to hold the words that will form the sentence and enlarges and returns the first letter of the
# sentence resulting from the recursive algorithm. Recursive algorithm, on the other hand, tries to produce sentences
# starting from the rule. Of course, the parameter must be S or ROOT to be a sentence. The difference from the function
# in Part 1 is to produce 20 different claws and write these sentences in an output file. It then returns these
# sentences.

def randsentence(CFG, output_file):
    sentence = []
    def sentence_generator(CFG, rule):
        if rule not in list(CFG.keys()):
            return rule
        else:
            str_temp = random.choice(CFG[rule])
            list_temp = str_temp.split(" ")
            for item in list_temp:
                result = sentence_generator(CFG, item)
                sentence.append(result)
    output = open(output_file, "w+")
    all_sentences = []
    for index in range(0, 20):
        sentence_generator(CFG, "ROOT")
        sentence = [i for i in sentence if i]
        result = ""
        for item in sentence:
            result = result + item + " "
        result = result[:-1] + "\n"
        result = result.capitalize()
        output.write(result)
        all_sentences.append(result)
        sentence = []
    output.close()
    return all_sentences

# My source when programming the CYK algorithm is "https://www.xarg.org/tools/cyk-algorithm/". My CYK algorithm
# primarily performs the preprocess process. These operations remove punctuation marks and clear non-vocabulary words if
# they came from ROOT. We find non terminals derived from words of the sentence formed after preprocess. We create the
# base of the table we created from these non terminals. Then the CYK algorithm starts. The elements in the other rows
# travel in a iterative way to find out which non terminal they are derived from. This process continues until the last
# element of the table. If the last element is S, the sentence becomes gramatically correct. If not, it is not
# gramatically false or sentence.

def CYKParser(CFG, sentence):
    temp_sentence = sentence[:-2]
    temp_str = temp_sentence[0:15]
    if temp_str == "Is it true that":
        temp_sentence = temp_sentence[16:]
    else:
        temp_sentence = temp_sentence.lower()
    word_list = temp_sentence.split(" ")
    table = []
    word_list_length = len(word_list)
    while word_list_length != 0:
        list_temp = []
        for count in range(0, word_list_length):
            list_temp.append([])
        table.append(list_temp)
        word_list_length = word_list_length - 1
    for index in range(0, len(word_list)):
        for non_terminal in list(CFG.keys()):
            if word_list[index] in CFG[non_terminal]:
                control = 0
                for item in list(CFG.keys()):
                    if non_terminal in CFG[item]:
                        table[0][index].append(item)
                        control = control + 1
                if control == 0:
                    table[0][index].append(non_terminal)
    for index1 in range(1, len(word_list)):
        for index2 in range(0, len(word_list) - index1):
            for index3 in range(0, index1):
                if len(table[index3][index2]) != 0 and len(table[index1 - index3 - 1][index2 + index3 + 1]) != 0:
                    for item1 in table[index3][index2]:
                        for item2 in table[index1 - index3 - 1][index2 + index3 + 1]:
                            str_temp = item1 + " " + item2
                            for item3 in list(CFG.keys()):
                                if str_temp in CFG[item3]:
                                    if item3 not in table[index1][index2]:
                                        table[index1][index2].append(item3)
    if len(table[-1]) == 0:
        print("Grammatically Not Correct")
    else:
        if table[-1][0][0] != "S":
            print("Grammatically Not Correct")
        else:
            print("Grammatically Correct")

# Let's examine the sentence "Every sandwich like the delicious president !"

# The table formed as a result of this sentence is as follows:
# [[['Det'], ['Noun'], ['Verb', 'NP'], ['Det'], ['Adj'], ['Noun']], [['NP'], [], [], [], ['Noun']], [[], [], [], ['NP']]
# , [[], [], ['VP']], [[], []], [['S']]]

# Since the top element of the table is S, this is a sentence and is grammatically correct.

# Test function for Part 2

def test_part2():
    CFG = rules("cfg.gr")
    sentences = randsentence(CFG, "output.txt")
    for sentence in sentences:
        sentence = sentence.rstrip("\n")
        print(sentence)
        CYKParser(CFG, sentence)
        print()

########################################################################################################################


def main():
    print("Part 1 Test:\n")
    test_part1()
    print()
    print("------------------------------------------------------------------------")
    print()
    print("Part 2 Test:\n")
    test_part2()

main()
