class YN:
    def askmkdir(message, name):
        import os
        print(str(message) + " Y/N")
        choice = input()
        if choice == "y" or choice == "Y":
            os.system("mkdir ./" + str(name))
        elif choice == "n" or choice == "N":
            pass
        else:
            print("Please Give Valid Answer")
    def askother(message):
        print(str(message) + " Y/N")
        choice = input()
        if choice == "y" or choice == "Y":
            return 1
        elif choice == "n" or choice == "N":
            return 0
        else:
            print("Please Give Valid Answer")
        
