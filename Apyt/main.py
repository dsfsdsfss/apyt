from pathlib import Path
import os
import getpass
debug = 0
def main():
    if not Path('./Files').is_file():
        os.system("python3 ./Use.py install")
    print("Apyt By @machport")
    print("1. Download Package")
    print("2. Remove Package")
    print("3. exit")
    username = getpass.getuser()
    choice = input(str(username) + ":")
    if choice == "2":
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
                    #print(i2)
                    #print("MATCH FOUND")
                    os.system("rm -rf ./OUT/" + i2)
                    print("Removed!")
        #os.system("rm -rf ./OUT/" + choice + "/")
    if choice == "1":
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
                    #print("MATCH FOUND")
                    if not Path('./OUT/').is_dir():
                        os.system("mkdir ./OUT/")
                    if Path("./OUT/" + i[0]).is_dir():
                        print("Already Installed")
                        break
                    os.system("curl " + i[1] + " > ./" + i[0])
                    os.system("mkdir ./OUT/" + i[0])
                    os.system("unzip ./" + i[0] + " -d ./OUT/" + i[0])
                    os.system("rm -rf ./OUT/" + i[0] +"/__MACOSX")
                    os.system("rm ./" + i[0])
    elif choice == "3":
        exit()
    main()

if __name__ == '__main__':
    main()
