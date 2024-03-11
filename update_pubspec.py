import os
import pathlib


def get_path():
    resp = ""
    wd = os.getcwd()
    absolute = os.path.abspath(wd)
    if wd == "":
        return []
    base = os.path.basename(wd)

    if base == "backend" or base == "frontend":
        resp = pathlib.Path(absolute).parent.absolute().__str__()
    else:
        resp = absolute
    return resp


def list_pubspec() -> list[pathlib.Path]:
    resp: list[str] = []

    working_path = get_path()

    def walk(path: pathlib.Path, level: int):
        if level > 2:
            return None
        paths = []
        for entry in os.listdir(path.absolute().__str__()):
            if os.path.isdir(entry):
                p: None | list[pathlib.Path] = walk(
                    pathlib.Path(path).joinpath(entry),
                    level + 1,
                )
                if p is not None and p.__len__() > 0:
                    paths.append(*p)
            else:
                if entry == "pubspec.yaml" or entry == "pubspec.yml":
                    paths.append(
                        pathlib.Path(path).joinpath(entry),
                    )
        return paths

    resp = walk(pathlib.Path(working_path), 1)
    return resp


def main():
    for entry in list_pubspec():
        new_content: list[str] = []
        has_changed = False
        with open(entry.__str__()) as file:
            for line in file.readlines():
                if "url: https://github.com/" in line:
                    has_changed = True
                    line = line.replace(
                        "url: https://github.com/",
                        "url: git@github.com:",
                    )
                new_content.append(line)
        if has_changed:
            with open(entry.__str__(), "wt") as file:
                file.write("".join(new_content))


if __name__ == "__main__":
    main()
