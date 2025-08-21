

def get_num_words(FilePath):
    with open(FilePath) as File:
        FileString = File.read()
    SplitString = FileString.split()
    return len(SplitString)

def count_letters(FilePath):
    with open(FilePath) as File:
        FileString = File.read()

    LetterDict = {}
    LetterList = []
    SplitString = FileString.split()

    for i in range(0, len(SplitString)):
        SplitWord = list(SplitString[i].lower())
        for i in range(0, len(SplitWord)):
            if SplitWord[i].isalpha():
                if not SplitWord[i] in LetterDict:
                    LetterDict[SplitWord[i]] = 1
                else:
                    LetterDict[SplitWord[i]] += 1
    for key, value in LetterDict.items():
        LetterList.append({"char": key, "num": value})
    return LetterList



def sort_on(items):
    return items["num"]

def sort_list(ListOfLetters):
    ListOfLetters.sort(reverse=True, key=sort_on)
    return ListOfLetters