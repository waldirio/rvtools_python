# rvtools python
Application to be executed on Linux and collect all information from vCenter

The idea is to be a similar application as RVTools [1] the main difference is, the application from website was designed to be executed only on MS platform, this version will be written in python 3 so will be possible execute on Linux environment.

About the final result, the idea is generate similar output *CSV files*.

The point here is not about COPY but just improve the Python skill and use the project [1] as reference once this one is a fantastic product!!!

Thank you and feel free to request Features / Enhancements.

Ps.: Necessary python 3.9 or greather.

# How to use??

First, install the python module
```
$ pip install rvtools-python
```

Now it's time to execute it.
```

$ rvtools
```

On the first run, will be created the file ~/.rvtools.conf
```
vcenter=<fqdn>
username=<vcenter username>
password=<password>
directory=<directory>
```
Note. the directory above is the area where all the `CSV` files will be saved by default.


You can just update the information on the file to be seamless and generate all reports without ask you the password again or you are able to pass the information all the time as parameter
```
$ rvtools --help
usage: rvtools [-h] [-s HOST] [-u USERNAME] [-p PASSWORD] [-d DIRECTORY]
               [-v VERBOSE]

RVTools Python parameters

optional arguments:
  -h, --help            show this help message and exit
  -s HOST, --host HOST  vCenter server to connect to
  -u USERNAME, --username USERNAME
                        vCenter username
  -p PASSWORD, --password PASSWORD
                        vCenter username password
  -d DIRECTORY, --directory DIRECTORY
                        Directory where will be saved all csv files. Should be
                        empty
  -v VERBOSE, --verbose VERBOSE
                        Show additional info.
$
```

The result will be the csv file created on the directory defined on the conf file by `directory=<directory>` or via CLI by `-d DIRECTORY`.
```
vinfo.csv
...
```

Hope you enjoy it. Still working to improve/add all features. Feel free to send your feedback or just submit the new Issue [here](https://github.com/waldirio/rvtools_python/issues).

Best
Waldirio

[1]. https://www.robware.net/rvtools/