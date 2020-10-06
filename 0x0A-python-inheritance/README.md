<h1 class="gap">Project 0x0A. Python - Inheritance</h1>

<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>Why Python programming is awesome </li>
<li>What is a superclass, baseclass or parentclass</li>
<li>What is a subclass</li>
<li>How to list all attributes and methods of a class or instance</li>
<li>When can an instance have new attributes</li>
<li>How to inherit class from another</li>
<li>How to define a class with multiple base classes </li>
<li>What is the default class every class inherit from</li>
<li>How to override a method or attribute inherited from the base class</li>
<li>Which attributes or methods are available by heritage to subclasses</li>
<li>What is the purpose of inheritance</li>
<li>What are, when and how to use <code>isinstance</code>, <code>issubclass</code>, <code>type</code> and <code>super</code> built-in functions</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version <code>1.7.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Python Test Cases</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>All your test files should be text files (extension: <code>.txt</code>)</li>
<li>All your tests should be executed by using this command: <code>python3 -m doctest ./tests/*</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Lookup
  </h4>
<p>Write a function that returns the list of available attributes and methods of an object:</p>

<ul>
<li>Prototype: <code>def lookup(obj):</code></li>
<li>Returns a <code>list</code> object</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    1. My list
  </h4>
 <p>Write a class <code>MyList</code> that inherits from <code>list</code>:</p>

<ul>
<li>Public instance method: <code>def print_sorted(self):</code> that prints the list, but sorted (ascending sort)</li>
<li>You can assume that all the elements of the list will be of type <code>int</code></li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    2. Exact same object
  </h4>
<p>Write a function that returns <code>True</code> if the object is <em>exactly</em> an instance of the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def is_same_class(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    3. Same class or inherit from
  </h4>
 <p>Write a function that returns <code>True</code> if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def is_kind_of_class(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    4. Only sub class of
  </h4>
<p>Write a function that returns <code>True</code> if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def inherits_from(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    5. Geometry module
  </h4>
 <p>Write an empty class <code>BaseGeometry</code>.</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    6. Improve Geometry
  </h4>
<p>Write a class <code>BaseGeometry</code> (based on <code>5-base_geometry.py</code>).</p>

<ul>
<li>Public instance method: <code>def area(self):</code> that raises an <code>Exception</code> with the message <code>area() is not implemented</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    7. Integer validator
  </h4>
<p>Write a class <code>BaseGeometry</code> (based on <code>6-base_geometry.py</code>).</p>

<ul>
<li>Public instance method: <code>def area(self):</code> that raises an <code>Exception</code> with the message <code>area() is not implemented</code></li>
<li>Public instance method: <code>def integer_validator(self, name, value):</code> that validates <code>value</code>:

<ul>
<li>you can assume <code>name</code> is always a string</li>
<li>if <code>value</code> is not an integer: raise a <code>TypeError</code> exception, with the message <code>&lt;name&gt; must be an integer</code></li>
<li>if <code>value</code> is less or equal to 0: raise a <code>ValueError</code> exception with the message <code>&lt;name&gt; must be greater than 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    8. Rectangle
</h4>
<p>Write a class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).</p>

<ul>
<li>Instantiation with <code>width</code> and <code>height</code>: <code>def __init__(self, width, height):</code>

<ul>
<li><code>width</code> and <code>height</code> must be private. No getter or setter</li>
<li><code>width</code> and <code>height</code> must be positive integers, validated by <code>integer_validator</code></li>
</ul></li>
</ul>

<h4 class="task">
    9. Full rectangle
 </h4>
<p>Write a class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
(task based on <code>8-rectangle.py</code>)</p>

<ul>
<li>Instantiation with <code>width</code> and <code>height</code>: <code>def __init__(self, width, height):</code>:

<ul>
<li><code>width</code> and <code>height</code> must be private. No getter or setter</li>
<li><code>width</code> and <code>height</code> must be positive integers validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
<li><code>print()</code> should print, and <code>str()</code> should return, the following rectangle description: <code>[Rectangle] &lt;width&gt;/&lt;height&gt;</code></li>
</ul>

 <h4 class="task">
    10. Square #1
  </h4>
<p>Write a class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>):</p>

<ul>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size):</code>:

<ul>
<li><code>size</code> must be private. No getter or setter</li>
<li><code>size</code> must be a positive integer, validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
</ul>

  <h4 class="task">
    11. Square #2
  </h4>
<p>Write a class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>).
(task based on <code>10-square.py</code>).</p>

<ul>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size):</code>:

<ul>
<li><code>size</code> must be private. No getter or setter</li>
<li><code>size</code> must be a positive integer, validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
<li><code>print()</code> should print, and <code>str()</code> should return, the square description: <code>[Square] &lt;width&gt;/&lt;height&gt;</code></li>
</ul>