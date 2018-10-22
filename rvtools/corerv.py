""" Module to read the conf file / vcenter, username and password """
import re
import os


class CoreCode(object):
    """  Main Class *CoreCode* responsible for read the conf file feature """

    def read_conf_file(self):
        """ Definition to read the conf file rvtools.conf """

        home_area = os.path.expanduser('~')

        try:
            fp_conf_file = open(home_area + "/.rvtools.conf", "r")
            for line in fp_conf_file:
                if re.search('^vcenter', line):
                    # VCENTER = re.split('=', re.search('^vcenter',line).string)[1]
                    self._vcenter = re.split('=', re.search('^vcenter', line).string)[1].strip()
                if re.search('^username', line):
                    # USERNAME = re.split('=', re.search('^username',line).string)[1]
                    self._username = re.split('=', re.search('^username', line).string)[1].strip()
                if re.search('^password', line):
                    # PASSWORD = re.split('=', re.search('^password',line).string)[1]
                    self._password = re.split('=', re.search('^password', line).string)[1].strip()
                if re.search('^directory', line):
                    # DIRECTORY = re.split('=', re.search('^directory',line).string)[1]
                    self._directory = re.split('=', re.search('^directory', line).string)[1].strip()

            return self
        except FileNotFoundError:
            print("There isn't the conf file on ~/.rvtools.conf, creating a new one now")
            print("according to the example below:")
            print("-----------------------")
            print("vcenter=<fqdn>")
            print("username=<vcenter username>")
            print("password=<password>")
            print("directory=<directory>")
            print("-----------------------")
            print("")
            print("Please update the info if you would like to persist the credentials")

            template_conf_file = open(home_area + "/.rvtools.conf", "w+")
            print("vcenter=<fqdn>", file=template_conf_file)
            print("username=<vcenter username>", file=template_conf_file)
            print("password=<password>", file=template_conf_file)
            print("directory=<directory>", file=template_conf_file)
            template_conf_file.close()
