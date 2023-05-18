import os
import sys


# https://stackoverflow.com/questions/9727673/ with little changes
def print_docindex(outfile = 'doc/index.md'):

    original_stdout = sys.stdout
    with open(outfile, 'w') as f:
        # redirect standard output to file
        sys.stdout = f
        # print("# doc\n")
        for root, dirs, files in os.walk("doc"):
            level = root.replace("doc", '').count(os.sep) - 1 
            if level == -1: # non mostrare doc
                continue
            # print directory as subtitle
            print("{0} \n".format(os.path.basename(root)))
            # print file and links
            for f in files:
                print('- [{}]({})'.format(f, os.path.join(os.path.basename(root), f)))
            print("\n")
    sys.stdout = original_stdout
            
if __name__ == '__main__':
    print_docindex()
