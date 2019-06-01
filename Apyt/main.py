from pathlib import Path
from Choices import YN
import os
import getpass
debug = 0
def clear():
    print("\n" * 999)
def main():
    clear()
    print("Apyt By @machport")
    print("1. Download Programs")
    print("2. exit")
    username = getpass.getuser()
    choice = input(str(username) + ":")
    if choice == "1":
        clear()
        files = []
        for i in open("./Files", "r").read().split("\n"):
            files.append(i.split("URL"))
        files.pop()
        if debug:
            print(files)
        fileinput = input("package:")
        for i in files:
            i = list(map(lambda foo: foo.replace(' ', ''), i))
            for i2 in i:
                if fileinput == i2:
                    print("MATCH FOUND")
                    if not Path('./OUT/').is_dir():
                        os.system("mkdir ./OUT/")
                    os.system("curl " + i[1] + " > ./" + i[0])
                    os.system("mkdir ./OUT/" + i[0])
                    os.system("unzip ./" + i[0] + " -d ./OUT/" + i[0])
                    os.system("rm ./" + i[0])
    elif choice == "2":
        exit()
    main()

if __name__ == '__main__':
    main()
