**********************
Virtualenv Update Path
**********************

#######################
Description
#######################


This modulke provides a cli interface to use for adding extra folders to the ``PATH`` environment variable associated with the targeted environment variable. This has the effect of extending the list of folder included upon environment activation, and enables virtualenvironments to be used as limited user profiles.

The module functions by appending a path override to the init scripts associated with the environment in question. 

#######################
Installation
#######################
This module is pip installable::

    pip install virtualenv-update-path

#######################
Usage
#######################


For updating all supported update paths::
    
    virtualenv-update-path "<the path to virtualenv Script folder>" "<folder to include in path>"


For updating a bat file::
    
    virtualenv-update-path "<path to virtualenv Script folder>/activate.bat" "<folder to include in path>"

For updating the base file::
    
    virtualenv-update-path "<path to virtualenv Script folder>/activate" "<folder to include in path>"
