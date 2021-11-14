#  First project 0x00. AirBnB clone - The console 👾

 | ![Alt text](https://static.dw.com/image/56218728_303.jpg "Title") |
 | ----------------------------------------------------------------- |


In this project we are going to clone a web application step by step of AirBnB, we will use tools built by ourselves throughout the project such as HTML / CSS templates, database storage, API, front-end integration which will also serve us for later projects.

## Content ✍️
Each part of the project is intertwined and will help us to:
* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* Create a simple flow of serialization/deserialization:   Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine


## Instructions 🦾
The first thing we must do is create our own shell limited to a specific use case, in this case we want to be able to manage the objects of our project and we will do it as follows:
1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

## Installation 🚀
To download the program and run it first
they should follow these steps:
1. Have vagrant, wsl, visual studio code or a virtual machine.

```
sudo apt-get install vagrant
```

2. Install a text editor like emacs, vi or sublime text.

```
sudo apt-get install emacs
```

3. Install python3

```
sudo apt-get install python3.6
```

4. Clone the repository.
```
git clone https://github.com/ChristianMartinezTech/AirBnB_clone.git
```

5. All files should use the pycodestyle (version 2.7.*)
```
pip install pycodestyle
```

<h3> FOLDERS <h3> 

| FOLDERS | DESCRIPTION |
| ----- | ------------ |
| models |   |
| engine |   |
| tests |   |
| AUTHORS |   |
| README.md |   |

<h3> FILES <h3> 

| FILES | DESCRIPTION |
| ----- | ------------ |
| base_model.py |   |
| __init__.py |   |
| file_storage.py |   |
| console.py |   |
| user.py |   |
| state.py |   |
| city.py |   |
| amenity.py |   |
| place.py |   |
| review.py |   |


<h3> COMMANDS <h3> 

| COMMANDS | DESCRIPTION |
| ----- | ------------ |
|  |   |
|  |   |
|  |   |
|  |   |
|  |   |
|  |   |





## Authors 👩‍💻

<p> Christian Felipe Martinez 2388@holbertonschool.com </p>
<p> Jessica Julieth Sanabria 3497@holbertonschool.com </p>

