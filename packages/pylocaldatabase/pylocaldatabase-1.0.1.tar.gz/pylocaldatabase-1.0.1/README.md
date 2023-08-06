# Python Local Database

A python package made to simplify the use of json as a mean to organize and store data in python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python Local Database.

```bash
pip install pylocaldatabase
```

Release history and file downloads can be found [on the project's pypi page](https://pypi.org/project/pylocaldatabase/).

## Usage

```python
from pylocaldatabase import pylocaldatabase
# define database file and assign databasecontroller instance to var dbcontroll
dbcontroll = pylocaldatabase.databasecontroller(path="file.json")

# load data from file
dbcontroll.load()

# create database file 'file.json'
dbcontroll.makeDatabase()

# create document 
dbcontroll.insertDocument({}, "documentName")

# assign the document we created
document = dbcontroll.getDocument("documentName")

# insert Item to the document
document.insertItem("ItemName", {"Property":"Property Value"})

# read Item data
itemData = document.getItem("ItemName").get()

# save data 
dbcontroll.save()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
