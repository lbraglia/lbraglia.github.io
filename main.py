from pathlib import Path

debug = False


def update_index_recursive(d="doc"):
    index_fname = "index.md"
    index_path = Path(d + "/" + index_fname)
    with open(index_path, 'w') as index:
        for d in sorted(Path(d).iterdir()):
            if d.name != index_fname:
                # now d is a directory
                print(d.name, "\n", file=index)
                for f in sorted(d.iterdir()):
                    # f = f.relative_to(d)
                    print(f"- [{f.name}]({f})", file=index)
                print("\n\n", file=index)


def update_index_flat(d="slides/corso"):
    index_fname = "index.md"
    index_path = Path(d + "/" + index_fname)
    with open(index_path, 'w') as index:
        for f in sorted(Path(d).iterdir()):
            f = f.relative_to(d)
            if f.name != index_fname:
                print(f"- [{f.name}]({f.name})", file=index)


if __name__ == '__main__':
    update_index_recursive("doc")
    update_index_flat("slides/corso")
