# Project Euler

![](https://projecteuler.net/profile/tabenmalik.png)

Welcome to my Project Euler solutions! [Project Euler](https://projecteuler.net/)
is a catalog of math problems designed to improve math, programming, and
problem solving skills. Only solutions to the first 100 problems are documented
here, per Project Euler's guidelines. All of my solutions past problem 100 are
in a private repo, though they still use this python package as the core
framework and register additional solutions via the `pe.problems` entry point.
It's pretty nifty.

This is a return to Project Euler for me. My original solutions were written
in *Java* back in *2010*, so I decided to restart my solutions in Python and
publish them here.

## Self-imposed Constraints

On top of the Project Euler guidelines, I imposed additional constraints on
my development in this project. These constraints are designed to keep my
problem solving consistent, focused, and documented.

#### Must be written in Python/CPython

Python is a very readable open source, high level, language with a rich
standard library. As I am already familiar with Python, this constraint allows
me to focus more on the problem sets than learning additional languages.

Pure Python can be slow for certain kinds of problems, which means I need to
be flexible in my thinking. CPython, the most popular implementation of Python,
is written in C and provides a framework for extending Python with C. With
CPython, I can write C extensions in the CPython ecosystem without breaking my
Python-only constraint. This allows more efficient solutions and gives me a
deeper knowledge of the whole Python ecosystem!

#### No third-party library dependencies for final solutions

Third-party libraries can be useful for investigating or demonstrating aspects
of a problem. For example, using matplotlib to plot the trend of a sequence can
give useful insight to a problem. My final solutions, however, must use only
the Python standard library and my own developed framework.

Using third party libraries such as numpy, sympy, etc, may make solutions
easier to solve and provide faster runtimes, but could cause me to miss out on
crucial understanding. My intention is to learn and deeply understand each
problem, not just get the answer.

#### Solutions must be documented in sphinx

Each problem, and my core library, should be documented using sphinx and
reStructured text. Sphinx is a popular option for documentation generation
of Python packages. This constraint ensures consistency in how I publish
explanations to my first 100 solutions, to help others learn.

Enjoy!
