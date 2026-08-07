# import calc //after this you have to mention calc. before calling any function from calc.py
# from calc import * //to import all the functions from calc.py

from calc import add, sub #to import specific functions from calc.py

result = add()
print(result)

# the module_package folder or directory is considered the package
# and the calc.py file is considered the module, which can be imported into other files.
