# import json
# from html.parser import HTMLParser # https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
import requests
from bs4 import BeautifulSoup
import warnings
import re

def main():
    warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

    # exp = re.compile("[>0-9\"\':<?.()!@#$%^&*,\\-]")
    exp = re.compile("[>0-9]")

    board = "pol"

    r = requests.get("https://a.4cdn.org/{}/catalog.json".format(board))
    # for every thread on page 1, sort by bumps
    threads_dict = r.json()[0]["threads"] # page 1

    op_posts = [] # weighed more?
    replies = [] # weighed less?

    count = 0

    for thread in threads_dict:
        # stip html from here?

        # view every reply in thread and create dictionary of most common words
        op_id = thread["no"]
        r = requests.get("https://a.4cdn.org/{}/thread/{}.json".format(board, op_id))
        reply_dict = r.json()["posts"]

        for reply in reply_dict:
            if "sub" in reply:
                replies.append(reply["sub"])
            elif "com" in reply:
                # strip html from com
                replies.append(re.sub(exp, "", BeautifulSoup(reply["com"], "html.parser").get_text()))

    for phrase in replies:
        phraselist = open("phraselist.csv", "a")
        try:
            phraselist.write("\"{}\",".format(phrase.rstrip("\n")))
        except UnicodeEncodeError:
            pass
        phraselist.close()


if __name__ == "__main__":
    main()