<!-- README.md -->

# Aliased Shell runner for python projects

This runs your python projects/packages from anywhere inside your shell, without the need to install the package or change directory. 
NOTE: Currently only pipenvs are implemented. Only tested on Windows 10. 
Feel free to clone and extend.

NOTE: a sample packageAlias.yml file can be found here: https://gitlab.com/larsmielke2/boakboak/-/tree/main/boakboak/apps


# Install
- pipenv install boakboak


### dependencies
- python 3.9 - 3.10
- pyyaml



# Problem boakboak tries to solve?
I have some python based services, which I want to run occasionally from anywhere inside the
shell using an aliased shell call.

Most importantly: I dont want to install all these services into my main environment.

For example:
- I want to save my files to a archive directory, for which I have a archive.py module.
- I want to convert a table to a json or yaml file for which I use a convert.py package.

I want to be able to flexibly add/remove these services from the aliased shell call.




# Usage
Create and packageAlias.yml file and name it like the shell call alias you like to use.
Example file:
- name like: /apps/packageAlias.yml (see example in directory below)
- save to: ... \Lib\site-packages\boakboak\apps\packageAlias.yml
- or save as boakboak.yml to: app directory of the callable app (same directory as setup.py)

## Run like
boak packageAlias -my parameters




## Steps

#### Example: Imaginary project which uses a archive.py module to archive files and folders.
- I will run my module from the shell, using "python -m archive -c 'my_archive_comment'" as I always do.
- From the sucessfully executed shell command, I copy the path, cmds and optional args to archive.yml
- I save the created .yml file in: boakboak/boakboak/apps/archive.yml
- The resulting .yml file has to look like this example: https://gitlab.com/larsmielke2/boakboak/-/tree/main/boakboak/apps

From the shell, I now call:
- boak archive -c 'my_archive_comment'


## How it works

boakboak will use the parameters from apps/packageAlias.yml, to run your project/package
- It takes appPath and finds your project/package (returns the first dir with .venv in it)
- It uses .venv file/folder or project name (if Pipfile is found), to identify the executable
- It uses a subprocess call, to run your cmds using identified python.exe



# License
