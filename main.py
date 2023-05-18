import os

# https://stackoverflow.com/questions/9727673/ with little changes
def list_files(startpath = "doc"):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep) - 1 
        if level == -1: # non mostrare doc
            continue
        indent = ' ' * 4 * (level)
        print('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('-{}[{}]({})'.format(
                subindent, f,
                os.path.join(os.path.basename(root), f)))
        print("\n")
            
            
if __name__ == '__main__':
    list_files()
