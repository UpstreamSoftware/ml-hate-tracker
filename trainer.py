import sys
import pickle
import codecs


def main():
    phrasefile = codecs.open(sys.argv[1], "r", "ISO-8859-1")
    phraselist = []

    line_num = 0

    if len(sys.argv) == 3:
        phrasefile.seek(sys.argv[2])

    for phrase in phrasefile:
        print("{} -- {}| {}(y/n) or q to quit: ".format(str(line_num), phrasefile.tell(), phrase) , end="")
        selection = input().lower()
        while(selection not in "ynq"):
            selection = input()
        if selection == "y":
            phraselist.append(tuple((phrase, 1)))
        elif selection == "n" or selection == "":
            phraselist.append(tuple((phrase, 0)))
        elif selection == "q":
            break
        line_num += 1

    listdump = open("listdumps/alec_listdump_use_for_testing.pkl", "wb")
    pickle.dump(phraselist, listdump)
    listdump.close()
    print("all done :)")


if __name__ == "__main__":
    main()