""" Module to read the conf file / vcenter, username and password """
import re

class CoreCode(object):
    """  Main Class *CoreCode* responsible for read the conf file feature """

    def read_conf_file(self):
        """ Definition to read the conf file rvtools.conf """
        try:
            fp_conf_file = open("rvtools/rvtools.conf", "r")
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
            return self
        except FileNotFoundError:
            print("There isn't the conf file, please create a new one")
            print("according example below:")
            print("-----------------------")
            print("vcenter=<fqdn>")
            print("username=<vcenter username>")
            print("password=<password>")
            print("-----------------------")
