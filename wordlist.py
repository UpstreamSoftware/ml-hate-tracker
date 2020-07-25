from collections import Counter

def main():
    c = Counter()
    for phrase in open("wordlists/biglist.txt"):
        c[phrase] += 1
    print(c.most_common(10))


if __name__ == "__main__":
    main()