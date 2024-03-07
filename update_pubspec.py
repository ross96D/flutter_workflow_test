import sys


def main(token: str):
    new_content: list[str] = []
    filename = "pubspec.yaml"
    with open(filename) as file:
        content = file.readlines()
        for line in content:
            if "url: https://github.com/" in line:
                line = line.replace(
                    "url: https://github.com/",
                    f"url: https://ross96D:{token}@github.com/",
                )
            new_content.append(line)

    with open(filename, "wt") as file:
        file.write("".join(new_content))


if __name__ == "__main__":
    if sys.argv.__len__() != 2:
        print("update pubspec takes 1 argument")
        exit(1)
    main(sys.argv[1])
