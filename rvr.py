import sys


def remove_version(filename):
    with open(filename) as f:
        packages = f.read().splitlines()
    seperator = '=='
    packages = [text.split(seperator, 1)[0] for package in packages]
    with open("requirments_updated.txt", "x") as f:
        for package in packages:
            f.write("%s\n" % package)


if __name__ == "__main__":
    remove_version(sys.argv[1])
