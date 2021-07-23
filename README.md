# KIvyGetPyModuleDeps

This simple script helps you to know all the hidden and sub requirement of python packages used on your code. This gives you the info of requirements
to add to your `buildozer.spec` file and also what packages you have that are not included on the `python-for-android` receipe

## Code Example of How To get all dependences

```python
from get_buildozer_py_deps import get_dependencies, check_non_existing_recipe

print(get_dependencies(["requests", "pyrebase4"]) # you can add as many package as possible
print(check_non_existing_recipe(["requests", "pyrebase4"]) # you can add as many package as possible, but your internet access must be on
```

you can also run the file directly with this command
```
python3.8 __init__.py pyrebase4 kivy kivymd
```
