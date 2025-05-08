import os
from pathlib import Path

debug = False


def update_index_recursive(d="doc"):
    # os.chdir(d)
    d_content = sorted(Path(".").iterdir())
    index_path = "index.md"
    with open(index_path, 'w') as index:
        for d in d_content:
            if d.name != index_path:
                # now d is a directory
                print(d.name, "\n", file=index)
                # p = Path(d)
                fs = d.iterdir() # files within
                for f in sorted(fs):
                    print(f"- [{f.name}]({f})", file=index)
                print("\n\n", file=index)


def update_index_flat(d="slides/corso"):
    # os.chdir(d)
    d_content = sorted(Path(d).iterdir())
    index_path = "index.md"
    with open(index_path, 'w') as index:
        for f in d_content:
            f = f.relative_to(d)
            if f.name != index_path:
                print(f"- [{f.name}]({f.name})", file=index)


if __name__ == '__main__':
    # update_index_recursive("doc")
    update_index_flat("./slides/corso")
