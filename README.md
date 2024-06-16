# A case for Julia over Python for teaching scientific computing

Back in the day, Fortran was the kind of language used in a university course teaching numerical methods in mathematics.
Later, matlab become popular for this purpose, being more "beginner friendly".
Nicely reducing the programming difficulty for students on what is meant to be a mathematics course after all.
Then Python came in as the general purpose "real world" language to use in code-related courses that were part of mathematical or scientific university courses.
Along with libraries like `numpy`, `scipy` and `pandas`, Python seems to be edging out domain specific languages like matlab and R from being taught in schools.
Now Python is more popular than ever, much much more so than the others mentioned so far.
On the face of it Python is a great beginner language, with dynamic typing, reducing the required programming knowledge overhead when needing to teach programming "just as a tool" for a scientific application.
However here is my claim:

> As soon as you through NumPy into the mix, the beginner-friendly aspects of Python go out the window.
> Even as far as being inferior in these regards compared to Julia.

- lists vs numpy arrays
    - == not being the same
- good python vs good numpy
- convoluted dtype="o" example (needs pandas)
- python is not an "industry language"
- disclaimers

## Python is easy?

Python is dynamically typed, and requires no explicit typing.
These are typically seen as good things for a beginner's programming language,
which I do not disagree with.
I also see a place for languages like Python for non-beginners too.
My recent projects have involved Rust and Python, each allowing for a style that suits their respective codebase well.
Above all, I see reducing on formalities, and easy immediate interactive coding
as the key requirements for a beginner language.
Typing is just an unnecessary formality potentially confusing a new user?

However...

> being ignorant of typing is not an option when using NumPy.

## Typing + Numpy != avoidable

## Python + Numpy == unnecessary formality

## Good Numpy != Good Python

## Python != Good jobs
