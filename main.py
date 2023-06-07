import os
import sys
from pathlib import Path

def update_docindex():
    # docdir
    docdir = Path("doc")
    os.chdir(docdir)
    # dir to be used in the toc
    dirs_in_toc = ["misc", "math", "cs", "dae"]

    with open('index.md', 'w') as f:
        for d in dirs_in_toc:
            print(d, "\n", file = f)
            p = Path(d)
            paths = p.iterdir()
            for p in sorted(paths):
                print('- [{0}]({1})'.format(p.name, p),
                      file = f)
            print("\n\n", file = f)
            
if __name__ == '__main__':
    update_docindex()
