import sys
import pickle
import codecs


def main():
    phrasefile = codecs.open(sys.argv[1], "r", "ISO-8859-1")
    phraselist = []

    line_num = 0

    for phrase in phrasefile:
        print(str(line_num) + "| " + phrase + "(y/n) or q to quit: ", end="")
        selection = input()
        if selection.lower() == "y":
            phraselist.append(tuple((phrase, 1)))
        elif selection.lower() == "n":
            phraselist.append(tuple((phrase, 0)))
        elif selection.lower() == "q":
            break
        line_num += 1

    listdump = open("listdump.pkl", "wb")
    pickle.dump(phraselist, listdump)
    listdump.close()
    print("all done :)")


if __name__ == "__main__":
    main()