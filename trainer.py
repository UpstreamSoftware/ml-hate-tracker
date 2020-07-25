import sys
import pickle


def main():
    phrasefile = open(sys.argv[1])
    phraselist = []

    for phrase in phrasefile:
        print(phrase + "\n(y/n): ", end="")
        if(input().lower() == "y"):
            phraselist.append((phrase, 1))
        else:
            phraselist.append((phrase, 0))


    listdump = open("listdump.pkl", "wb")
    pickle.dump(phraselist, listdump)
    listdump.close()
    print("all done :)")

if __name__ == "__main__":
    main()