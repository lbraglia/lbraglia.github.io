import os

outfile = "doc/index.md"

# https://stackoverflow.com/questions/9727673/ with little changes
def list_files(startpath = "doc"):
    print("```")
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep) - 1 
        if level == -1: # non mostrare doc
            continue
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}[{}]({})'.format(
                subindent, f,
                os.path.join(os.path.basename(root), f)))
    print("```")

            
            
if __name__ == '__main__':
    list_files()