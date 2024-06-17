# A case for Julia over Python for teaching scientific computing

Back in the day, Fortran was the kind of language used in a university course teaching numerical methods in mathematics.
Later, matlab become popular for this purpose, being more "beginner friendly".
Nicely reducing the programming difficulty for students on what is meant to be a mathematics course after all.
Then Python came in as the general purpose "real world" language to use in code-related courses that were part of mathematical or scientific university courses.
Along with libraries like `numpy`, `scipy` and `pandas`, Python seems to be edging out domain specific languages like matlab and R from being taught in schools.
Now Python is more popular than ever, much much more so than the others mentioned so far.
On the face of it Python is a great beginner language, with dynamic typing, reducing the required programming knowledge overhead when needing to teach programming "just as a tool" for a scientific application.
However here is my claim:

> As soon as you throw NumPy into the mix, the beginner-friendly aspects of Python go out the window.
> Even as far as being inferior in these regards compared to Julia.

### Disclaimer

I have been a tutor/demonstrator for Python related courses at university, never for Julia though.
This is mainly my thoughts on the downsides of Python in the context of teaching scientific computing to beginners based on my experience.
I have no real proven reason to believe it's easier with Julia.
But my experience with Julia so far seemingly eliminates the potential struggles that I have seen in students in the past.

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

Lists in Python can contain objects of any type, and any mix of types

```python
a = [2, "eu", {1: "val"}] # totally fine
```

However Numpy arrays are homogeneous, only containing elements of the same type, giving great performance benefits when used correctly.
Any attempt to mutate it after it's creation (and its `dtype` is set) will result in a conversions to that type:

```python
x = numpy.array([2])
x[0] = 0.5 # float is converted to Int value 0
x[0] = True # converts to 1
x[0] = "l" # ValueError: could not convert string to integer: 'l'
```

Typical `dtypes` include boolean, integer, float64,... And also the "O" dtype referring to generic Python objects.
I didn't know about that last `dtype="O"` possibility until I graded a student submission achieving it, performing manipulations with a numpy array of `dtype=int`, and eventually creating a numpy array of mostly integers, but also a couple `None` objects.

Students learning to use NumPy can easily get stung by ignoring types, and at the very least need to understand that NumPy arrays and Python lists are different types of objects.

To hammer this point, here's a classic error for students:

```python
if x == x:
    print("x is x")
```

Surely no issue here right? Almost any value of `x` would make the code above
do what we expect? Not with NumPy:

```
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```

This is because if `x` is a numpy array containing more than 1 entry, `x==x` evaluates pointwise to an array of booleans, not a single bool.
This along with many other numpy ruins any kind of duck typing: you either write code specifically to work with Numpy arrays and objects, or you write code to use anything else.

```python
len(x) # length of python list
x.shape[0] # length of numpy array
reversed(x) # take elements of list in reverse order (wrap list() aronud to get a list)
numpy.flip(x) # reverse elements in a numpy array
```

For reference, in Julia, you use standard inbuilt arrays for both generic use, and numerical computing. Less of a need to be careful about types.
Furthermore, in relation to the above example with equality checking, you can do either simply and explicitly:

```julia
x = [0, 1]
x == x # normal equality, evaluates to true
x .== x # pointwise equality, evaluates to [true, true]
```


## Python + Numpy == unnecessary formality

## Good Numpy != Good Python
