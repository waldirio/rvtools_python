# rvtools
Application to be executed on Linux and collect all information from vCenter

The idea is to be a similar application as RVTools [1] the main difference is, the application from website was designed to be executed only on MS platform, this version will be written in python 3.x so will be possible execute on Linux environment.

About the final result, the idea is generate one similar output *CSV files*.

The point here is not about COPY but just improve the Python skill and use the project [1] as reference once this one is a fantastic product !!!

Thank you and feel free to request Features / Enhancements.

# How to use??

First, clone this repo
```
git clone git@github.com:waldirio/rvtools.git
```
Now, it's time to create your virtual environment "I really recommend you to do that"
```
$ python3 -m venv /tmp/rvtools
```
Let's load the virtual environment
```
$ source /tmp/rvtools/bin/activate
(rvtools) [login@hostname ]$
```
Ok. Let's imagine I ran the git clone command on my home directory "/home/waldirio" then
```
$ cd /home/waldirio/rvtools
```
Now it's time to update pip and install requirements
```
(rvtools) [login@hostname rvtools]$ pip install --upgrade pip
(rvtools) [login@hostname rvtools]$ pip install -r requirements 
```

Now the last step. Let's configure the vCenter url, username and password on the file `rvtools/rvtools.conf`
```
vcenter=vcenter.fqdn.here
username=username_here
password=password_here
```

and ... run it.
```
(rvtools) [login@hostname rvtools]$ rvtools/rvtools.py 
Reading the conf file
vcenter: vcenter.fqdn.here
user: username_here
...
```

Hope you enjoy it. Still working to improve/add all features. Feel free to send your feedback.

Best
Waldirio
waldirio@gmail.com

[1]. https://www.robware.net/rvtools/
