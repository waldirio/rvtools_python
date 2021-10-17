#!/usr/bin/env python
""" Main rvtools module """

import sys
import os
import ssl
import argparse
import requests
import urllib3
from pyVim import connect

from rvtools.corerv import *
from rvtools.vinfo.vinfo import *


# requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings()

def get_args():
    parser = argparse.ArgumentParser(description="RVTools Python parameters")

    parser.add_argument('-s', '--host',
                        required=False,
                        action='store',
                        help='vCenter server to connect to')

    parser.add_argument('-u', '--username',
                        required=False,
                        action='store',
                        help='vCenter username')

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='vCenter username password')

    parser.add_argument('-d', '--directory',
                        required=False,
                        action='store',
                        help='Directory where will be saved all csv files. Should be empty')

    parser.add_argument('-v', '--verbose',
                        required=False,
                        action='store',
                        help='Show additional info.')


    args = parser.parse_args()

    return args


def main():
    """ Def responsible to start the vCenter connection and call all report modules """

    args = get_args()

    if (args.host is None or args.username is None or args.password is None or args.directory is None):
        print("Reading Conf File")
        obj = CoreCode()
        conn = obj.read_conf_file()
        if conn is None:
            sys.exit()
        else:
            server = conn._vcenter
            username = conn._username
            password = conn._password
            directory = conn._directory
            if server == '<fqdn>':
                print("You are using default values. Please update the file")
                print("~/.rvtools.conf or just pass all mandatory parameters.")
                sys.exit()
    else:
        print("Using flags")
        server = args.host
        username = args.username
        password = args.password
        directory = args.directory


    if not os.path.isdir(directory):
        print("You have to create the dir {}".format(directory))
        sys.exit()

    ssl_context = ssl._create_unverified_context()

    print("vcenter: {}\nuser: {}\n".format(server, username))

    service_instance = connect.SmartConnect(host=server, user=username, \
         pwd=password, port=443, sslContext=ssl_context)


    # VM Information
    # vinfo_collect(service_instance)
    vinfo_collect(service_instance, directory)


# https://code.vmware.com/apis/358/vsphere

if __name__ == "__main__":
    main()
