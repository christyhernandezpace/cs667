## **Class Objects**
#### Questions and Answers for Comprehension
____________________________________________________________

* **What is a class object in Python?**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A class object in Python is a group or collection of functions that work together to achieve a common goal. It allows for better organization and categorization of code/functions.


* **What is a docstring?**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A docstring is a multi-line string used to describe what a function, class, or module does. It is typically the first statement inside a function or class and is enclosed in triple quotes like these: `""" """`. Docstrings help with code documentation and therefore organization.


* **How to define `__init__` in a class object?** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In a class object, you usually start with the `__init__` function. Here, you are able to define variables that will be local and relevant to your class object, such as models and API keys. In other words, the `__init__` function allows you to initialize the variables in your class object, and the variables defined in it can only be accessed within the class object. The way to define it within the class object is `def __init__(self):`


* **What is a method?** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A method is a function that lives within a class object.


* **How do you let functions fail gracefully?**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To allow a function to fail gracefully, you can add `try` and `except` statements within your function. You could also add a string/failure message to your exception statement. This way, when your code fails, it does not fail the entire script and instead notifies you nicely about the issue that occurred.


* **What's a standard practice of a return statement?** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In standard practice, a return statement in a function typically only returns the result of that function, so that the result(s)/variable(s) can be released from that function and then be accessed in other areas of the program instead of only the function it/they came from. It is typical for a class object as a whole to return data in JSON format, which is a structured format that is denoted by curly brackets such as these: `{ }`. JSON is similar to a Python dictionary in that both use key-value pairs and curly brackets, but they are not the same, as a dictionary is a Python-specific data structure and JSON is a text format that can exchange data between systems.