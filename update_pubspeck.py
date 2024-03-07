def main():
    new_content: list[str] = []
    filename = "pubspec.yaml"
    with open(filename) as file:
        content = file.readlines()
        for line in content:
            if "url: https://github.com/" in line:
                line = line.replace("url: https://github.com/", "url: git@github.com:")
            new_content.append(line)

    with open(filename, "wt") as file:
        file.write("".join(new_content))


if __name__ == "__main__":
    main()
