
def check_conf_file():
    try:
        f = open("rvtools.conf","r")
    except FileNotFoundError:
        print("There isn't the conf file, please create a new one")
        print("according example below:")
        print ("-----------------------")
        print ("vcenter=<fqdn>")
        print ("username=<vcenter username>")
        print ("password=<password>")
        print ("-----------------------")


    print(f.read())
    

def main():
    print("Reading the conf file")
    check_conf_file()

if __name__ == "__main__":
    main()