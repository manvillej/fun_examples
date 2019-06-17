# google_fire

It took me awhile to figure out the whole entry_points, but I think I am going to experiment with that more. I have a project where it could be useful. It was really cool to be able to create CLIs with their name really quickly. I don't have to focus on arg parsing at all and I can just quickly throw a CLI together. 

The class model is very useful, you can handle your initial/environment variables in the __init__, plus the method chaining seems promising. I like the idea of building a CLI set of games like Joshua from Wargames

## install:
> conda env create -f environment.yml
> conda activate google_fire
> python setup.py develop

## commands:
### hello
* hello {name}

### calc:
* calc add {x} {y}
* calc mutiply {x} {y}

### counter:
* counter countup
* counter countdown
