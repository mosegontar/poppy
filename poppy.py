import argparse
import os
import subprocess


EXTENSION_MAP = {
    'py': 'python',
    'rb': 'ruby'
}

class Poppy(object):

    def __init__(self, editor):
        self.fname = '_poppy.py'
        self.editor = editor

        # create the file if it doesn't exist
        # and close file immediately after
        open(self.fname, 'a').close()

    def edit(self, new=False, run=False):

        if new:
            self._new()

        cmd = [self.editor, self.fname]
        subprocess.call(cmd)

        if run:
            self._run()

    def _new(self):
        open(self.fname, 'w').close()

    def _run(self):

        extension = self.fname.split('.')[1]
        if extension not in EXTENSION_MAP.keys():
            print("Can't determine interpreter for {} file".format(extension))
            return

        interpreter = EXTENSION_MAP.get(extension)
        subprocess.call([interpreter, self.fname])


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-  e', '--editor', default='vim')
    parser.add_argument('-n', '--new',
                        help="Create new blank poppy file",
                        action='store_true')
    parser.add_argument('-r', '--run',
                        help="Run interpreter for file after editing",
                        action='store_true')

    args = parser.parse_args()

    poppy = Poppy(args.editor)
    poppy.edit(args.new, args.run)


if __name__ == '__main__':
    main()
