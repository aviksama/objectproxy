# ObjectProxy #
**A minimalistic yet powerful object proxying utility**

This readme attempts to explain the general use of this library.

### Installation ###
* Install from repository
```
pip install git+https://github.com/aviksama/objectproxy.git
```
* Install from pypi
```
pip install object-proxy
```
### Example ###

Object proxy basically creates a proxy for any python object:

```python
class MyClass(object):

    def __init__(self, array=None):
        self.array = array or []

    def get_array_element(self, index):
        try:
            return self.array[index]
        except IndexError:
            return


def create_dictionary_of_objects(*args):
    mydict = dict()
    for index, arg in enumerate(args):
        mydict[index] = arg

```
Now lets create proxies for the objects above in random fashion

```python
>>> from objectproxy import ProxyElement, eval_proxy

>>> class_proxy = ProxyElement(MyClass, args=[[1,2,3],], kwargs={})
>>> function_proxy = ProxyElement(create_dictionary_of_objects, args=[class_proxy], kwargs={})
>>> class_proxy_ref = function_proxy.values()[0]
>>> class_proxy_array_element = class_proxy_ref.get_array_element(0)
>>> eval_proxy(class_proxy_array_element)
1
``` 
until `eval_proxy` is called on the proxy object, It doesn't call the parent methods. Hence all the parent methods and attributes are lazily evaluated. 

### Contribution guidelines ###

We appreciate your effort in contributing to this project. You can contribute in any of the following.
* Writing tests
* Code review
* Other guidelines
* Submit issues

In order to contribute please fork the repository, And make a GitHub pull request to `dev` branch.

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact


        