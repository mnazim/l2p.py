=====================================
Control Structures
=====================================

Okay, Dokey! So we are back again with the second installment of our 
*Learn To Program with Python* series. I hope you enjoyed that last one in this
series. What? You missed it! No worries. You can access it at [link to part 1 here](http://asd.com).

Configuring The Editor
======================
In this part of the series, you will be writing most of the code inside a
the text editor. Remember that we talked about downloading the GEdit editor in the first
article in the series. If you did not, I suggest you download it before
proceeding any further as we will be using it extensively. 

Here is what a GEDit main window looks like. Note that it contains the
code from ``greet.py`` from the part 1 of this series.

|GEditMainWindow|

To configure GEdit for Python, go to ``Edit » Preferences`` and
configure it as shown in following two images.

|GEditPrefs1| |GEditPrefs2|

Basically, all we need is to set *Tab Width* to *4* and enable *Insert spaces
instead of tabs*. Everything else is optional. In fact, setting *Tab Width* and 
*Insert spaces instead of tabs* is also not required but it is good practice 
and accepted convention to do it like that.

.. |GEditMainWindow| image:: /_static/02/images/gedit-main-window.png
.. |GEditPrefs1| image:: /_static/02/images/gedit-prefs-1.png
.. |GEditPrefs2| image:: /_static/02/images/gedit-prefs-2.png

A Word About Operators
======================

Remember from last part of the article, we learn to do mathematical
operations with pythons. In programming, the symbols like ``+, -, /, *`` are  
called operators. 

Mathematically speaking, an operator is a function that takes a 
value or a set of values(literals and variables in case of programming)
and transforms them into a different value. The values that an operator
takes are called *Operands* and the value that comes out is called a
*Result* (duh!).

Think of an automatic bread baking machine. We put in flour, water, some salt 
and bit of yeast, it process all these raw items and transforms them into fresh 
baked bread. Flour, water, salt and yeast are the operands and the baking machine is the
operator.

Marry Go round
==============

There are a lot tasks in programming(and in real world) that require
certain steps to be done in a repetitive fashion. For example, how would
you teach someone how to add salt to a dishes

1. Taste food.
2. Is it salty enough.
3. If no, add more salt.
4. Else stop adding salt.

Assuming, it's not an experienced chef, one would need to do these steps
in a repetitive fashion. Similarly, there are certain problems in
programming that require some way to do a task or a set of tasks in a 
repetitive fashion.

Programming language provide special constructs called loops, to accomplish such tasks.

``for`` loop
------------
``for`` is one such looping construct. Consider following example.

.. code-block:: python

   for number in range(0,10):
       print number

After running the above code example, you should see following output:

.. code-block:: python

   1
   2
   3
   4
   5
   6
   7
   8
   9

``while`` loop 
--------------

Exercise
--------

Equality and Inequality
========================
We encounter a lot of situations in life where we need to say yes or no to
things. Programing is not any different. Let's see how we can do that.

Write the following code snippets inside GEdit and save it as
``check_equality1.py``.

.. literalinclude:: _static/02/code/check_equality1.py

Now, let's dissect the code line by line.

First, we set two variables ``x`` and ``y`` to ``1`` and ``2`` respectively.
Nothing new here. Then there is something new.  ``==``. It is called the *equality operator*. 
The job of the equality operator is to check whether the two operands supplied 
on its both sides are of same value or not. The result of an equality
operator is either ``True`` or ``False``. It can never be anything else.

Run the program from command line(see :doc:`Running Programs From A File in Part 1</introduction>`).

.. code-block:: bash

    python check_equality1.py 

You should see the following output.

.. code-block:: python

    True
    True
    False

Now let's rewrite ``check_equality1.py`` as follows and save it as
``check_equality2.py``:

.. literalinclude:: _static/02/code/check_equality2.py

Run the program from the command line::

    python check_equality2.py

The output should be like following:

::

    Let x = 1 and y = 2.
    x is equal to 1:  True
    y is equal to 2:  True
    x is equal to y:  False



Like any other operator, equality operator can also be combined with
string and other operators.

Exercise
--------

``!=`` is the opposite of ``==``. It is called the *Inequality Operator*. 
in ``check_equality2.py``, replace ``==`` with ``!=``. Save it as
``check_inequality.py``. Run the program and compare the output with the output 
of ``check_equality2.py``. What differences do you see in the output?

Taking decisions
================

Now that we understand equality and inequality operators, let's put them
to some real use. 

``if`` statement 
----------------

.. code-block:: python

   if 1 == 1:
       print "1 is equal to 1"

Explain ``if`` here

``if - else`` statement
-----------------------

.. code-block:: python

   if 1 == 1:
       print "It's True"
   else:
       print "It's False"


``if - elif - else``
--------------------

.. literalinclude:: _static/02/code/guest_list.py

Exercise
--------


Road Ahead
==========
