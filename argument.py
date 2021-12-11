class Argument:
    def __init__(self):
        from argparse import ArgumentParser
        argument_parser = ArgumentParser('python3 webPathScanner')
        # argument for url
        argument_parser.add_argument('url', action='store', help='url of the victim')
        # argument for wordlists path
        argument_parser.add_argument('-w', '--wordlist', action='store', help='wordlists path', required=True)
        # argument for thread count
        argument_parser.add_argument('-t', '--thread', action='store', help='number of threads', type=int)
        self.args = argument_parser.parse_args()
