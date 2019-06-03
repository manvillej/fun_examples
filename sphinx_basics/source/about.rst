==============
How I did this
==============

1. Once I've installed sphinx I ran *sphinx-quickstart* which quickly sets up sphinx source directory. 

2. Then I can create/edit the rst files. here is the sphinx information on restructued text: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

3. Then I can run *sphinx-build -b html sourcedir builddir*


I can provide example documentation of python object very easily

.. py:function:: enumerate(sequence[, start=0])
	
	return an iterator that yields tuples of an index and an item of the *sequence*. (and so on.)

=============
autodoc
=============

I can also use autodoc to document functions, classes, and modules. here is a link to learn more about that: http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

.. automodule:: io
	:members: