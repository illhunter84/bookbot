import sys 

num_words = 0
FilePath = None

from stats import get_num_words
from stats import count_letters
from stats import sort_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        FilePath = sys.argv[1]
        num_words = get_num_words(FilePath)
        #print(f"{num_words} words found in the document")
        LetterList = count_letters(FilePath)
        SortedStats = sort_list(LetterList)
        #print(SortedStats)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {FilePath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in range(0, len(SortedStats)):
            print(f"{SortedStats[i]["char"]}: {SortedStats[i]["num"]}")
        print("============= END ===============")


main()

