import argparse
import os
import subprocess

EXTENSION_MAP = {
    'py': 'python',
    'rb': 'ruby'
}

class Poppy(object):

    def __init__(self, fname='_poppy.py'):
        self.fname = fname
        self.editor = os.environ.get('POPPY_EDITOR', 'vim')

        # create the file if it doesn't exist
        # and close file immediately after
        open(self.fname, 'a').close()

    def edit(self):

        cmd = [self.editor, self.fname]
        subprocess.call(cmd)

    def new(self):
        open(self.fname, 'w').close()

    def run(self):

        extension = self.fname.split('.')[1]
        if extension not in EXTENSION_MAP.keys():
            print("Can't determine interpreter for {} file".format(extension))
            return

        interpreter = EXTENSION_MAP.get(extension)
        subprocess.call([interpreter, self.fname])


def main():
    poppy = Poppy()

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new', help="Create new blank poppy file", action='store_true')
    parser.add_argument('-r', '--run', help="Run interpreter for file after editing", action='store_true')
    args = parser.parse_args()

    if args.new:
        poppy.new()

    poppy.edit()

    if args.run:
        poppy.run()

if __name__ == '__main__':
    main()
