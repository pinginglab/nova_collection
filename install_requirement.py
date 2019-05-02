from subprocess import call

# read requirements.txt file, create list of package names
requirements = open('requirement', 'r')
item = requirements.readlines()
for package in item:
    try:
        call("pip install " + package.split()[0], shell=True)
        print("[*] install {}".format(package.split()[0]))
    except Exception as e:
        print(e.__str__())
