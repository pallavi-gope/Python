#Virtual Environment : An environment which is same as the system interpreter but is isolated from the other python environment on the system.
#Installation:
'''
To use virtual environment, we create

    # pip install virtualenv  ----> install the package

we create a new environment using:

    # virtual myprojectenv ----> create a new venv

The next step after creating the virtual environment is to activate it.

    # .\myprojectenv\Scripts\activate.ps1

    Note: in case of error use this command : Set-ExecutionPolicy Unrestricted -Scope Process

we can now use this irtual environment as a separate python installation.

    # deactivate : to deactivate the virtual environment
'''

import flask
import pandas as pd