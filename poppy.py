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

    def new(self):
        open(self.fname, 'w').close()

    def edit(self, run=True):
        cmd = [self.editor, self.fname]
        subprocess.call(cmd)

        if run:
            self._run()

    def _run(self):

        extension = self.fname.split('.')[1]
        if extension not in EXTENSION_MAP.keys():
            print("Can't determine interpreter for {} file".format(extension))
            return

        interpreter = EXTENSION_MAP.get(extension)
        subprocess.call([interpreter, self.fname])


if __name__ == '__main__':
    poppy = Poppy()
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print(args.echo)