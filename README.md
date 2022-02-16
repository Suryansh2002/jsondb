# jsonsh
=======

This sucks and i know it !

Installing
----------

```sh
pip install jsonsh
```

What is this !
-----------
This is a silly package , that uses pydantic to store data in different json files

Data Fetched is in pydantic Model , which can be converted to dict using dict()


Usage
------

### Base Example

```py
from jsonsh import Template,Instance

instance = Instance("Data") #this is your data folder

@instance.register
class Test(Template)
    id:int
    age:int
    name:str

async def main():
    idk = Test(id = 10,age = 13,name = "hello")
    await idk.save() #this saves the file in your current working directory
```

### Finding Data

There are no advanced queries yet but you can find by id or particular value


```py
from jsonsh import Template,Instance

instance = Instance("Data")

@instance.register
class Test(Template)
    id:int
    age:int
    name:str

async def main():
    data = await Test.find_one(id = 10)
    print(data) #prints the data

```

### Finding Multiple Data


```py
from jsonsh import Template,Instance

instance = Instance("Data")

@instance.register
class Test(Template)
    id:int
    age:int
    name:str

async def main():
    data = await Test.find_many(age = 10) #finding all dict with age as 1
    print(data) #prints the lists of multiple dicts

```

#### Simple Caching 

```py

from jsonsh import Template,Instance

instance = Instance("Data",cache_state = True,capacity = 100) #this helps you to avoid reading files in finds

```
