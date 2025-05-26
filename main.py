from pathlib import Path


def update_index_recursive(root="doc"):
    index_fname = "index.md"
    index_path = Path(root + "/" + index_fname)
    with open(index_path, 'w') as index:
        for d in sorted(Path(root).iterdir()):
            if d.name != index_fname:
                # now d is a directory
                print(d.name, "\n", file=index)
                for f in sorted(d.iterdir()):
                    print(f"- [{f.name}]({f.relative_to(root)})", file=index)
                print("\n\n", file=index)


def update_index_flat(root="slides/corso"):
    index_fname = "index.md"
    index_path = Path(root + "/" + index_fname)
    with open(index_path, 'w') as index:
        for f in sorted(Path(root).iterdir()):
            f = f.relative_to(root)
            if f.name != index_fname:
                print(f"- [{f.name}]({f.name})", file=index)


if __name__ == '__main__':
    update_index_recursive("doc")
    # update_index_flat("slides/corso")
