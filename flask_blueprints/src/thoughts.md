# Thoughts

* error_app: an isolated blueprint, doesn't use anything outside of the error_app directory

* hello_app: really simple hello world app, uses the hello.html template inside the templates/hello_app/ directory



the general template appears to be:

./app/{blueprint app}/
./app/{blueprint app}/__init__.py 
./app/templates/
./app/templates/{blueprint app}/
./app/templates/{blueprint app}/{template}.html
./app/static/
./app/__init__.py
./app/models.py
./config.py
./app.py


miguel grinberg uses a "main" blueprint to contain the majority of logic, but I kind of like the idea that each flask blueprint should be fully named. 

I've been thinking of doing a flask-react example for awhile. I think I could have atleast two blueprints. 

1. the react blueprint, containing all of the react files and the react route.
2. an api blueprint, registered under APIs. SN has a nice pattern of "/{api path}/{namespace}/{version}/{endpoint}" I think that might be a nice way to do it.

I am wondering if all blueprints (or at least the utility blueprints) should be inside of a blueprint directory. it wouldn't block pip installing a blueprint. 