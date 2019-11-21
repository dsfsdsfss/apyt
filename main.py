from pathlib import Path
import os
import getpass
debug = 0
def main():
    if not Path('./main').is_file():
        if not Path("./Sources").is_file():
            os.system("curl https://raw.githubusercontent.com/hlmoore/hlmoore.github.io/master/Sources > ./Sources")
        files = []
        for i in open("./Sources", "r").read().split("\n"):
            files.append(i.split("URL"))
        for i in files:
            print("curl " + i[1] + " > ./" + i[0])
            os.system("curl " + i[1] + " > ./" + i[0])
    print("Apyt By @machport")
    print("1. Download Package")
    print("2. Refresh Sources")
    print("3. Remove Package")
    print("4. exit")
    username = getpass.getuser()
    choice = input(str(username) + ":")
    if choice == "3":
        os.system("rm ./Out/" + str(input("package: ")))
    if choice == "2":
        files = []
        for i in open("./Sources", "r").read().split("\n"):
            files.append(i.split("URL"))
        if debug:
            print(files)
        for i in files:
            print("curl " + i[1] + " > ./" + i[0])
            os.system("curl " + i[1] + " > ./" + i[0])
    if choice == "1":
        source = input("source: ")
        files = []
        package = input("package: ")
        if not Path(source).is_file():
            print("Source Is Not Installed")
            exit()
        else:
            print(open(source, "r").read().split("\n"))
            for i in open(source, "r").read().split("\n"):
                files.append(i.split("URL"))
            if debug:
                print(files)
            for i in files:
                if str(package) == i[0].split(" ")[0]:
                    os.system("curl " + str(i[1]) + " > ./" + str(i[0].split(" ")[0]) + ".tmp")
                    tmpi = i[1]
                    print(tmpi.split("/").pop().split('"')[0].split(".").pop())
                    if tmpi.split("/").pop().split('"')[0].split(".").pop() == "dmg":
                        os.system("cp " + str(i[0].split(" ")[0]) + ".tmp" + " " + str(i[0].split(" ")[0]) + ".dmg")
                        os.system("rm ./" + str(i[0].split(" ")[0]) + ".tmp")
                        os.system("open " + str(i[0].split(" ")[0]) + ".dmg")
                    if tmpi.split("/").pop().split('"')[0].split(".").pop() == "zip":
                        os.system("cp " + str(i[0].split(" ")[0]) + ".tmp" + " " + str(i[0].split(" ")[0]) + ".zip")
                        os.system("rm ./" + str(i[0].split(" ")[0]) + ".tmp")
                        os.system("mkdir ./" + str(i[0].split(" ")[0]))
                        os.system("unzip ./" + str(i[0].split(" ")[0]) + ".zip -d" + "./" + str(i[0].split(" ")[0]))
    elif choice == "4":
        exit()
    main()

if __name__ == '__main__':
    main()
