from sys import argv
try:
    t=argv[1]
except IndexError:
    print("Arguments: run, install, uninstall, update")
    exit()
if argv[1] == "uninstall":
    import os
    os.system("rm ./files")
    os.system("rm -rf ./OUT/")
elif argv[1] == "install":
    import os
    from pathlib import Path
    if not Path('./Files').is_file():
        os.system("curl https://hlmoore.github.io/Files > ./Files")
    else:
        print("Already Installed")
elif argv[1] == "run":
    import os
    os.system("python3 ./main.py")
elif argv[1] == "update":
    import os
    os.system("curl https://hlmoore.github.io/Files > ./Files")
else:
    print("Arguments: run, install, uninstall, update")
