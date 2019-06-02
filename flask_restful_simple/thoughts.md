
flask-restful is pretty cool. It seems pretty nice to center APIs around resources which can be parallel to models. 

I should look into the marshal_with & marshal functionality. It seems pretty cool: https://flask-restful.readthedocs.io/en/latest/fields.html


I am wondering if I can find something that can generate resource classes by passing in a data model. So I can set up a resource-model quickly with a bunch of functionality. I want to examine the differences between a metaclass generator model & a class inheritance model. 

I think with a class inheritance model allows for more custom behavior as I can override base behaviors & add custom behaviors

The metaclass model allows for more quickly standing up a resource-model as I just have to add it to a list to pass into the generator.

If the generator & the inheritance models share the same base class, then either method would have the same functionalities.


Also should look into better app layouts in the intermediate docs: https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html

also to look at: https://marshmallow.readthedocs.io/en/3.0/
