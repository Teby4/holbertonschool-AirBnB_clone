![65f4a1dd9c51265f49d0](https://github.com/Teby4/holbertonschool-AirBnB_clone/assets/135641220/588fe399-9c03-4b32-bed2-ec41a5d1ac18)

## AirBnB clone - The console

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration


This project handles the basic file structure for the AirBnB clone. Object loading and storing is taken care by the engine module, and the console module manages interaction with this and the rest of the modules.

## The Command Interpreter

To start the console:
`$./console.py` or `$python3 console.py`

The available console commands are:
- **help**: displays a help page, gives info on other commands
- **quit**: exits the console
- **create**: creates a new object of a specific class and saves it
- **show**: display a specific instance
- **destroy**: removes an instance
- **all**: shows all instanes of a specific class, or of all classes
- **update**: modifies an attribute of an instance

After closing the console, all created instances are saved to a file, and restored when the next session is started.

### Console Command Examples

```
(hbnb) create BaseModel
b38d67bc-7ab6-4f27-a3ce-fc619d13a4d9
(hbnb) 
```
Created a BaseModel instance, and printed its unique id

```
(hbnb) destroy BaseModel b38d67bc-7ab6-4f27-a3ce-fc619d13a4d9
(hbnb) 
```
Destroyed the newly created instance

```
(hbnb) update BaseModel b38d67bc-7ab6-4f27-a3ce-fc619d13a4d9 age 27
(hbnb) show BaseModel b38d67bc-7ab6-4f27-a3ce-fc619d13a4d9
[BaseModel] (b38d67bc-7ab6-4f27-a3ce-fc619d13a4d9) {'id': 'b38d67bc-7ab6-4f27-a3ce-fc619d13a4d9', 'created_at': datetime.datetime(2024, 3, 3, 7, 38, 39, 322098), 'updated_at': datetime.datetime(2024, 3, 3, 7, 38, 39, 322111), 'age': '27'}
(hbnb) 
```
Added the attribute 'age' with a value of 27 to the created instance of BaseModel


## Authors

* Felipe Olivera <a href="https://github.com/Teby4" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a> 
* Bruno Bugani <a href="https://github.com/Mazionach" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
