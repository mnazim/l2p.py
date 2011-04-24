Introduction
============

Computers have changed the way we get our work done these days.
Computers can be seen everywhere. Baaah! You probably know that
already, so I am not going to waste your time with gibberish. Let's
get to the point.

Computers are dumb. No, really! They are. They cannot do anything
on their own. Computers need to be told repeatedly what to do. Not
only that, they even need to be told how to do that stuff. How do
we do that? We write programs.

Programs are a sequence of precise instructions to accomplish a
job/task at hand, which are fed to the computer for it to execute
in the precise order. The programs are also known as software. Your
web browsers like Firefox, Google Chrome, etc., are programs, your
office productivity suites like OpenOffice, MS Office, etc., are
programs. Your operating systems like Ubuntu, Windows, etc., are a
set of programs. Even the
the whole Internet is a set of programs working together.

Now how do we create these programs. We need Programming Languages
for that. Programming languages are similar to normal human
languages like English, Arabic, Spanish, etc. Just like we have
many languages to communicate with our fellow humans, there are
many languages to communicate with computers. The only difference
between human languages and programming languages is that languages
used for programming are variants of English(mostly), dumbed down
to a level computers can understand(remember, computers are dumb).
Well, there are more differences, but let's not worry about those,
for the time being, at least.

The method of writing the programs using programming languages is
called programming and that's what we are going to learn here. We
will learn to write programs with a simple and elegant language
called Python.

***Fun fact: A programming languages is also program(or a set of programs)***

Before we start.
----------------

We need to download the Python programming language and a decent
text editor(No, notepad and wordpad are not decent text editors).
We will use GEdit as our text editor. To get them, go to
`learn2program.globekashmir.com/download <http://learn2program.globekashmir.com/download>`_
You should see links to download Python and GEdit for your
operating systems. Download and install both Python and GEdit
specific to your operating system. You will need a working internet
connection to download these.

If you are running Linux or Mac OS X, chances are you already have
python and a decent text editor installed. You should still install
python from the the link provided to ensure that you have proper
versions of Python and GEdit.

*Note: Python can also be downloaded from the official Python website `http://python.org <http://python.org/download>`_.*

Starting Python From Terminal
-----------------------------

Now, that we have python downloaded and installed, let's write our
first program.

Open the terminal application provided by your operating system(on
Windows press |Windows Key| + ``R``. Windows "Run Command" dialog
will appear; type ``cmd`` in it and press ``Enter``), type
``python`` at the command prompt and press ``Enter``. You should
see some text appearing in the terminal which should look something
like:

.. code-block:: python

    Python 2.6.6 (r266:84292, Sep 15 2010, 16:22:56) 
    [GCC 4.4.5] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

The above output might differ slightly on different operating
systems, but basically what we need is ``>>>``. This is called
*The Python Prompt*. If you see *The Python Prompt*, it means that
python is installed properly. If you do not see
*The Python Prompt*, go back a bit and ensure you did not miss any
step.

From now onwards, whenever you see ``>>>`` or you are told to go to
python prompt, it means:


-  open the terminal application
-  type ``python`` at the command prompt and press ``Enter``.

Your First Program
------------------

Now let's write our first program. Go to the python prompt and
enter the text exactly as you see below.

.. code-block:: python

    >>>print "Hello World"

Do not type ``>>>`` , type ``print "Hello World"`` where ``>>>`` appears

As soon as you press ``Enter``, your terminal should look like:

.. code-block:: python

    >>>print "Hello World"
    Hello World
    >>>

NOTE: It is important that you do not type anything between ``>>>`` and ``print``, not even a space. Why? Let's worry about it later.

What happened here? Remember, earlier in this article we learnt
that computers are dumb and we need to provide precise instructions
for the job/task at hand. That's exactly what we did here. We asked
the computer to print **Hello World** on the terminal. So ``print``
is the command and ``"Hello World"`` is the data on which the
command should act. There! You wrote your first program, wasn't
difficult at all. Was it? But why do we need to put ``"``(called
*double quotes*) around the Hello World. Which brings us to our
next section.

Exercise
~~~~~~~~


-  Enter ``>>> print Hello World`` (Hello World without the double
   quotes) and see what happens.
-  Instead of ``"Hello World"``, try numbers after ``print``
   command.
-  Try typing random things after ``print``. Try numbers,
   alphabets, combinations of alphabets and numbers.
-  Now finally, try all of the above again but without ``print`` in
   front of them.

Note down what you see and what you understand from this exercise.
I mean it! Get your notebook and a pencil right now and note it
down.

Literals
--------

A literal is a fixed value. It can be a number, it can be a
sequence of alphabets, it can be a collection of values. Type the
following in the python prompt and see what happens.

::

    >>>"Hello World"
    >>>22
    >>>3.14

Literals(or values) also have a type. In the above example. First
one is a **String**. Second and third are **Numbers**.

Any literal enclosed inside ``"``(*double quotes*) or
``'``(*single quotes*) are treated as strings. For example:
``"Hello"`` is a ``string``, ``"12"``, ``'33'``, ``'4.5'`` are
``strings``, not ``numbers``.

There are other types of values as well, but for now we will only
work with numbers and strings.

You can perform mathematical calculations with these values. For
example, try the following and note the results:

::

    >>>22 + 31
    >>>3.14 + 2.9
    >>>"Hello" + "World"

Now let's try some subtraction:

::

    >>>22 - 11
    >>>3.14 - 2.9
    >>>"Hello" - "World"

You must have noticed that numbers can be subtracted, but
subtraction on strings results in something different. You should
see something like:

::

    >>> "Hello" - "World"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for -: 'str' and 'str'
    >>>

This is an error: Python is trying to tell you that something went
wrong. In other words, we tried to do something that is not
possible or python does not accept this operation. But what went
wrong? We tried to subtract two strings. Not all mathematical
operations can be performed on all types. In other words, strings
can be added to each other, but we cannot subtract one string from
the other. Think about it, while ``"5 - 2"`` makes sense,
``"Hello" - "World"`` does not.

When we perform a mathematical operation on literals, they result
in new values, which are literals of the same type as the ones we
performed the operation on. That means adding/subtracting two
numbers will result in a new number and adding two strings will
result in a new string. Addition of two strings cannot result in a
number or vice versa.

Similarly you can divide values

::

    >>>5 / 2
    >>>10 / 5
    >>>22 / 11

Multiply values

::

    >>>5 * 2
    >>>6 * 88
    >>>33 * 4

Now let's combine all that we have understood so far and try out a
few things.

::

    >>>print "Hello World!"
    >>>print "My name is Mir Nazim"
    >>>print "I am ", 27, " years old"
    >>>print "I started programming at the age of ", 10 + 9
    >>>print "After 3 years I will be ", 27 + 3, " years old"
    >>>print 3, " years back, I was ", 27 - 3, " years old"

Exercise
~~~~~~~~


-  There is something different in the above examples. Try to find
   out what it is.
-  Try different combinations of printing number and strings
   together.
-  Try out all mathematical operations with both numbers and
   strings in various combinations.
-  There is one more mathematical operation performed with
   '%'(example: ``5 % 2``). Try to find out how is it different from
   division '/'

Exercise
~~~~~~~~

First, calculate the result of the following examples with a
calculator or by hand, and then try them at the python prompt:

::

    >>>10 - 2 * 33
    >>>33 * 2 - 10
    >>>33 * 2 - 10 / 10
    >>>10 / 2 * 40 / 8 * 100 / 20
    >>>10 + 2 / 2 + 66 * 2 / 66

If the results on the python prompt are different from what you got
with the calculator, try to find out the reason for the different
answers.(Hint: Both the results from the calculator and the ones on
the python prompt are correct; try to find out why they are
different)

Variables
~~~~~~~~~

A variable is a name given to a literal or a value, so that we can
use that name instead of the value in our programs. For example:

::

    >>>myname = "Mir Nazim"
    >>>myage = 27

In the above example we put ``"Mir Nazim"`` into a variable called
``myname`` and ``27`` in a variable called ``myage``. Now let's
repeat the last example, but with variables.

::

    >>>print "My name is", myname
    >>>print "I am ", myage, " years old"
    >>>print "After 3 years I will be ", myage + 3, " years old"
    >>>print 3, " years back, I was ", myage - 3, " years old"
    >>>print "I started programming at the age of ", myage - 10

From the above example, we understand that we can use the variables
inside mathematical operations. But why use variables?

Exercise
~~~~~~~~


-  Compare both examples(with and without variables) and list the
   differences.
-  Try to think of reasons whether using variables instead of
   literals is good or bad. (Hint: Try changing my name and age to
   your own name and age in both examples.)

Running Programs From A File
----------------------------

So far we have been writing programs on the python prompt. We can
also write the programs inside files and run those files instead.
Before we do so, lets create a folder to hold all our programs.
(Following instructions are specific to MS Windows, if you are on
Mac OS X or Linux I am confident you can adapt these instructions
to equivalent ones on your operating system). Go to the
terminal(but not the python prompt) and type these commands one by
one.

::

    cd C:\
    mkdir learn2program
    cd learn2program

Remember we downloaded and installed GEdit editor and Python
earlier in this tutorial. Now open the GEdit editor and type the
following example

::

    myname = "Mir Nazim"
    myage = 27
    print "Hello World!"
    print "My name is ", myname
    print "I am ", myage, " years old"

Now save this file inside ``C:\learn2program`` and name it as
``helloword.py``. Remember to give it extension ``.py``. From now
onwards, save all your files in ``learn2program`` folder.

Now go the terminal and type the following commands in order:

::

    cd C:\learn2program
    python helloword.py

You should see the following output:

::

    My name is  Mir Nazim
    I am  27  years old

If you see a different output, you missed some steps. Go back and
make sure that you followed the instructions properly.

What we did here is we asked ``python`` to run the program written
in the file called ``helloword.py``. Simple. Isn't it. From now
onwards we will write all our programs inside files.

***Note:** Do not type '>>>' in front of lines. There should not be any spaces before the first character in the files also, or python will throw ``IndentationError``, for example:*

.. code-block: python

    File "<stdin>", line 1
      print "Hello World"
      ^
    IndentationError: unexpected indent

``IndentationError`` always means that there is a space character
before some line of code.

Exercise
~~~~~~~~


-  Convert all previous examples to files and run them from
   terminal.

Interacting With The World
--------------------------

What good are computer programs if they cannot interact with
humans. Human Computer Interaction can be seen every where. When we
use ATM to get money quickly, we are interacting with computers. It
asks us to enter our PIN number, then asks us how much money we
want etc. etc. Now whatever the ATM shows on the screen is called
**Output** and whatever we enter with the keypad is called
**Input**. Every computer in the world is capable of doing only 3
things.

::

    Take Input --> PROCESS --> Give Output
        |             |               |
        |             |               |
    Commands    Calculations         Result
        &            &
      Data       Operations

Now we will write a program that take input from the user. Let's
create a new file and call it ``greet.py``. Enter following lines
in it:

::

    print "What is your name?"
    name = raw_input()
    print "What is your age?"
    age = raw_input()
    print "Hello ", name, ", you are ", age, " years old"

Now go to terminal and run following command:

::

    python greet.py

You should see following output.

::

    What is your name?
    Mir Nazim
    What is your age?
    27
    Hello  Mir Nazim , you are  27  years old

``raw_input()`` is a command which tells python to take whatever
the user enters and put it in the variable before the ``=``. There
are two ``raw_input()`` commands in ``greet.py``, one takes the
text entered by you and puts it inside the ``name`` variable and
other one puts the text entered into age variable. The rest is the
same. These variables are in no way different from the ones we used
earlier, just that the value is now coming from a different
source.

Exercise
~~~~~~~~

Just play with whatever you learned today. Write different
programs, combine variables with literals, combine numbers and
strings, print them out and see what happens.

Just have fun, because programming is about having fun all the
time.

Road Ahead
----------

In the next article in this series, we will continue to learn more
about numbers and strings. We will also learn how to make decisions
inside code and to execute things repeatedly. Till then, happy
programming.

About The Author
----------------

Mir Nazim is co-founder and Chief Architect at iKraft Software (P)
Ltd. He has been developing large scale web application with
Python, Ruby, PHP and related technologies, for 8 years. He is a
Free and Open Source Software evangelist. He can be reached at
mir.nazim@ikraftsoft.com.


.. |Windows Key| image:: /_static/windowskey.jpg
