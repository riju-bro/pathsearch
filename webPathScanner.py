from argument import Argument
from threading import Thread

argument_parser = Argument()
# assigning arguments to args
args = argument_parser.args
url = args.url.rstrip('/')
thread = args.thread


def __main__():
    import os
    if not os.path.isfile(args.wordlist):
        print('The wordlist does not exist')
        exit(-1)
    wordlist = open(args.wordlist, 'r')
    paths = wordlist.readlines()
    j = 0  # start index
    diff = int(len(paths)/thread)
    for i in range(diff, len(paths)+1, diff):
        t = Thread(target=dirsearch, args=(paths[j:i], ))
        t.start()
        j = i
    if i != len(paths):
        t = Thread(target=dirsearch, args=(paths[j:len(paths)], ))
        t.start()


def dirsearch(paths):
    from requests import get
    for path in paths:
        r = get(f'{url}/{path.strip()}', allow_redirects=False)
        if r.status_code != 404:
            print(f'/{path.strip()}\t{r.status_code}')


if __name__ == '__main__':
    __main__()
