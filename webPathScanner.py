from argument import Argument

argument_parser = Argument()
# assigning arguments to args
args = argument_parser.args
url = args.url.rstrip('/')


def __main__():
    import os
    if not os.path.isfile(args.wordlist):
        print('The wordlist does not exist')
        exit(-1)


def dirsearch(paths):
    from requests import get
    for path in paths:
        r = get(f'{url}/{path}', allow_redirects=False)
        if r.status_code != 404:
            print(f'/{path}\t{r.status_code}')


if __name__ == '__main__':
    __main__()
