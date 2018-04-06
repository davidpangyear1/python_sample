# python_sample                                                                                                                                                                                             
This repository shows a sample standalone python program with some good practices.
This program is supposed to be packaged and run as a standalone program.
This program is NOT supposed to be installed by pip.

References:
1. https://python-packaging.readthedocs.io/en/latest/minimal.html
2. https://help.github.com/articles/fetching-a-remote/ 

## Directory structure

### Files about building eggs
*setup.py*

It contains the settings for building egg.

The following folders are created by setup.py:
*build/*
*dist/*
*python_sample.egg-info/*

*dist/* contains our final egg(s), and other two folders only contains intermediate files.

### Source codes
*__main__.py*

It serves as the entry point of our program. import python_sample module to use the source codes.

*python_sample/xxx.py*

We are making python files under the module *python_sample*
Note that *__init__.py* is necessary even if it is empty.
It tells python that this directory is a module.

*python_sample/xxx.pyc*

They are compiled python codes. Don't need to care about them. You can remove them if you want.

### Git files
*.git/*

This contains git information. Don't need to care about it.

*.gitignore*

This contains a list of file extensions that git will ignore.
This file is given by github, when you create a repository with the choice 'python'.

### Readme file
*README.md*

You should write useful information about your project. (You should overwrite this file and make your own one)

What is this project supposed to do?
How can we install it?
How can we run it?
What arguments can we use?
How are the files managed?

There are many things should be included.

### License file
Would not be included here. If you need it, go to read github information.(or let it create one for you)

## Packaging and running
### wheel and egg
It is supposed to package a project into a wheel files. (Few years ago, egg files are preferred)
However, the documentations of python wheel are sadly few.
And seems it is impossible to import/run python wheel without pip install. (at least, no direct documentations found)
So, we will still package it into a python egg.

### Packaging
To package your project, execute:
>python setup.py bdist_egg

Your file will be at, for example,
*dist/python_sample-1.0-py2.7.egg*

### Running
You can directly run it by:
>python python_sample-1.0-py2.7.egg [arg1 arg2 ...]

Then, it will search for the __main__.py file and execute it.
It should have the same effect as you run:
>python __main__.py

## Github integration
View https://help.github.com/articles/fetching-a-remote/ for more information about git.

### Download this repository from github
To clone this repository to your directoty system, execute:

>git clone https://github.com/davidpangyear1/python_sample.git

A folder named 'python_sample' would be created under your current working directory.

### Pull from this repository
To pull the master branch from this repository, go to your repository, execute:
>git pull https://github.com/davidpangyear1/python_sample.git master

### Push to this repository
To push the master branch to this repository, go to your repository, execute:
>git push https://github.com/davidpangyear1/python_sample.git master

username and password are necessary.
