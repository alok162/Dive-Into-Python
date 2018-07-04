# Project Title
**python-basics**

# Properties
  Getters and setters are methods that let us read and write the value of an instance variable of an object.And this is the way we can set and get values rather than directly exposing fields of a class.

  As per the OO Principles, one should have properties as private and changes must be allowed through the   methods only. This rule is for enforcing the guaranty that there will be no accidental change of property. 
  Getters and setters encapsulate the fields of a class by making them accessible only through its public methods and keep the values themselves private. That is considered a good OO principle. ... Getter and setter method are used to get and set the value of x which is the way to achive encapsulation


**abstract method**

A method that is declared as abstract and does not have implementation is known as abstract method.

**What is docstring?**

A DocString represents Document String that is used to Document Python Modules, Classes and Methods.


**How is the memory management process in Python?**

Like other programming environments, Python Programming Environment has Garbage Collection Techniques that manages the Memory efficiently. Moreover, the memory is managed by the Private Heap which is ultimately managed by the Python Memory Manager.


**Does Python Compiled Code contains Byte-Codes?**

No. Python is primarily an Interpreted Language. However, at first the .py file is compiled to something called as Python Byte-Code which is not a file that contains Binary digits like other Programming environments. It actually contains Python specific instructions that helps in optimizing the startup speed.

**Is Python a Compiled or an Interpreted Programming Language?**

Python programs have the extension .py. These source files are first compiled to Byte Codes (which does not contain the binary codes). These Byte Code files helps in startup speed optimization. These byte-codes are then sent to the Python Virtual Machine where lines of codes are read one after another which means that it is interpreted.

**What is PEP 8 in Python?**

PEP 8 is a set of recommendations about writing Python Code so as to make it readable and useful for other programmers. It is more of a coding convention.


**Is Python a Scripting Language or not?**

Python is a General-Purpose Programming Language or rather a Multi-Purpose Programming Language. It is also a Scripting Language as it can be used to combine it into HTML Code used for Web Development.

**Python GIL (Global Interpreter Lock)**

Global interpreter lock (GIL) is a mechanism used in computer language interpreters to synchronize the execution of threads so that only one native thread can execute at a time.

This lock is necessary mainly because CPython’s memory management is not thread-safe(Python virtual machine is not thread safe).

A global interpreter lock (GIL) is a mutual-exclusion lock held by a programming language interpreter thread to avoid sharing code that is not thread-safe with other threads. In implementations with a GIL, there is always one GIL for each interpreter process.

Applications running on implementations with a GIL can be designed to use separate processes to achieve full parallelism, as each process has its own interpreter and in turn has its own GIL.

multiple threads run in parallel on different cores
