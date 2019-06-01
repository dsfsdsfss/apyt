from sys import argv
try:
    t=argv[1]
except IndexError:
    print("please give argument")
    exit()
if argv[1] == "uninstall":
    import os
    os.system("rm ./Sources")
elif argv[1] == "install":
    import os
    os.system("mkdir ./Sources")
elif argv[1] == "run":
    import os
    os.system("python3 ./main.py")
elif argv[1] == "update":
    import os
    os.system("curl https://hlmoore.github.io/Files > ./Files")
else:
    print("INVALID")
