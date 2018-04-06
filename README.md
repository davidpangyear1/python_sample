# python_sample                                                                                                                                                                                             
This repository shows a sample standalone python program with some good practices.
This program is supposed to be packaged and run as a standalone program.
This program is NOT supposed to be installed by pip.

References:
1. https://python-packaging.readthedocs.io/en/latest/minimal.html
2. https://help.github.com/articles/fetching-a-remote/ 

## package and run
It is supposed to package a project into a wheel files. (Few years ago, egg files are preferred)
However, the documentations of python wheel are sadly few.
And it is impossible to import/run python wheel without pip install. (at least, no direct documentations found)
So, we will still package it into a python egg.
To package your project, execute:
>python setup.py bdist_egg

The following folders are created:
build/
dist/
python_sample.egg-info/

Your file is at, for example,
dist/python_sample-1.0-py2.7.egg

You can directly run it by
python python_sample-1.0-py2.7.egg

Then, it will search for the __main__.py file and execute it.

## github integration
View https://help.github.com/articles/fetching-a-remote/ for more information about git.

### download this repository from github
To clone this repository to your directoty system, execute:

>git clone https://github.com/davidpangyear1/python_sample.git

A folder named 'python_sample' would be created under your current working directory.

### pull from this repository
To pull the master branch from this repository, go to your repository, execute:
>git pull https://github.com/davidpangyear1/python_sample.git master

### push to this repository
To push the master branch to this repository, go to your repository, execute:
>git push https://github.com/davidpangyear1/python_sample.git master

username and password are necessary.
