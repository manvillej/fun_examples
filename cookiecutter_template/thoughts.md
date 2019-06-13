

To build from the local template, run:
> cookiecutter "<path to repo>\fun_examples\cookiecutter_template\templates\basic"

Then just fill in fields at the prompts. 

It worked interestingly, I am wondering if I could use it to not just whole project setups, but subparts as well. a submodule would probably be cool. I am wondering if I can extend it to provide an CLI interfact in front of it. So it can have multiple phases of creation. For a submodule, provide a name for it, number of .py files, request input for the configuration for each pi file. 



to build from a non local template:

> cookiecutter gh:audreyr/cookiecutter-pypackage

the "gh:" is just short hand for github. It could also be

> cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git