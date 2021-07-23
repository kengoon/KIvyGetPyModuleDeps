# KIvyGetPyModuleDeps

This simple script helps you to know all the hidden and sub requirement of python packages used on your code. This gives you the info of requirements
to add to your `buildozer.spec` file and also what packages you have that are not included on the `python-for-android` receipe

## Code Example of How To get all dependences

```python
from get_buildozer_py_deps import get_dependencies, check_non_existing_recipe

print(get_dependencies(["kivy", "pyrebase4"]) # you can add as many package as possible
print(check_non_existing_recipe(["kivy", "pyrebase4"]) # you can add as many package as possible, but your internet access must be on
```

you can also run the file directly with this command
```
python3.8 __init__.py pyrebase4 kivy kivymd
```

### Output of `get_dependencies` looks like this
```javascript
{
  'kivy': ['pygments', 'kivy-garden', 'docutils'], 'pyrebase4': ['requests-toolbelt', 'gcloud', 'oauth2client', 'python-jwt', 'pycryptodome', 'requests'], 
  'kivy-garden': ['requests'], 
  'requests-toolbelt': ['requests'], 
  'gcloud': ['googleapis-common-protos', 'protobuf', 'oauth2client', 'six', 'httplib2'],     
  'oauth2client': ['pyasn1-modules', 'rsa', 'six', 'httplib2', 'pyasn1'], 
  'python-jwt': ['jwcrypto'], 
  'requests': ['chardet', 'urllib3', 'idna', 'certifi'], 
  'googleapis-common-protos': ['protobuf'], 'pyasn1-modules': ['pyasn1'], 
  'rsa': ['pyasn1'], 
  'jwcrypto': ['six', 'deprecated', 'cryptography'], 
  'cryptography': ['cffi']
}
```
it returns a dictionary of packages as `keys` and requirements as `values`


### Output of `check_non_existing_recipe` looks like this
```javascript
['pyrebase']
```
it returns a list of packages that is not yet present on `python-for-android`
