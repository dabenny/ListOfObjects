# ListOfObjects

> Python Package to Manage List of Objects

I need to create this package to manage lists of same objects.

## Installation

```sh
pip install https://github.com/dabenny/ListOfObjects
```

## Usage example

On my work often I have a bunch of objects with properties and methods as the following:

```python
class Box:
    name = 'Baox'
    money = 23
    def test(self):
        print('I''m a Box')
```

I would like to manage these objects as a list but:

```python
from listofobj import ListOfObj
test_list = ListOfObj([Box() for n in range(1,5)])
```

now I can access properties and methods of each objects within the list:

```python
test_list.name # -> return a list of Strings
test_list.money # -> return a list of Int

# I can perfom operation on the objects properties:
sum(test_list.money) # -> total money in the Boxes

# I can call object methods on each member of the list:
test_list.test() # -> print 'I''m a Box' for each object in list

# I can Slice the list by object properties:
test_list[test_list.money > 2] # Return the filtered ListOfObj
```

## Release History

* 0.9.0

  * First Public Release

## Meta

Daniele Beninato – [@dbeninato](https://www.linkedin.com/in/dbeninato/) – db.stuff+github at outlook.it

Distributed under the GNU GENERAL PUBLIC LICENSE license. See ``LICENSE`` for more information.

[https://github.com/dabenny/](https://github.com/dabenny/)

## Contributing

1. Fork it (<https://github.com/dabenny/ListOfObjects/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
