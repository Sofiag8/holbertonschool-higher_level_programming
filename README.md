<<<<<<< HEAD
<h1 class="gap">Project 0x07. Python - Test-driven development</h1>

 <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif" alt="" style="" /></p>

<h2>Background Context</h2>
<ul>
<li>Based on the requirements of each task, <strong> I should always write the documentation (module(s) + function(s)) anad tests first</strong>, before actually coding anything </li>
<li>As students, we have been strongly encourage to work together on thest cases, so we don&rsquo;t miss any edge case, but not in the implementation of them!</strong></li>
<li><strong>Don&rsquo;t trust the user</strong>, always think about all possible edge cases</li>
</ul>

<h2>Learning Objectives</h2>

<p> At the end of this project I am expected to be able to explain to anyone the following:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>What&rsquo;s an interactive test</li>
<li>Why tests are important</li>
<li>How to write Docstrings to create tests</li>
<li>How to write documentation for each module and function</li>
<li>What are the basic option flags to create tests</li>
<li>How to find edge cases</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.*)</li>
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
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Integers addition
</h4>
<p>Write a function that adds 2 integers.</p>

<ul>
<li>Prototype: <code>def add_integer(a, b=98):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    1. Divide a matrix
</h4>
<p>Write a function that divides all elements of a matrix.</p>

<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&rsquo;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    2. Say my name
</h4>
 <p>Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>

<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    3. Print square
  </h4>
<p>Write a function that prints a square with the character <code>#</code>.</p>

<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    4. Text indentation
  </h4>
<p>Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>

<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    5. Max integer - Unittest
 </h4>
  <p>Since the beginning you have been creating &ldquo;Interactive tests&rdquo;. For this exercise, you will add Unittests.</p>

<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>

<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" title="unittest module" target="_blank">unittest module</a> </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
<li>All tests you make must be passable by the function below</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

  <h4 class="task">
    Advance tasks
 </h4>
<p> Advanced tasks are optional and designed to challenge students and contribute to their competitiveness as developers </p>
=======
<h1 class="gap"> Hello PYTHON and High level programming</h1>

<p><img src="https://ourcodeworld.com/public-media/articles/articleocw-5c65fbda1ea05.jpg" alt="" style="" /></p>

<h2>Authors disclaimer</h2>

<pre><code>Welcome to the Python world!

After 3 months of C, you will start Python today.
The first projects are more &quot;C-oriented&quot; - no tricks, no funky syntax - simple!
If you&#39;ve already played with Python, don&#39;t worry, fun things will come.
You&#39;ll soon find that with Python (and the majority of higher level languages), 
there are ten different ways to do the same thing. Some tasks will expect only one implementation, 
while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. 
At Holberton, we won&#39;t start off with using PyCode, because it&#39;s much more strict compared to PEP8. 
Don&#39;t worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume, CTO at Holberton
</code></pre>

<h2>More Info</h2>

<h3>Zen</h3>

<pre><code>The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren&#39;t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you&#39;re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it&#39;s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let&#39;s do more of those!
</code></pre>

<h3>Install PEP8</h3>

<p><code>Pycodestyle</code> is now the <a href="https://github.com/PyCQA/pycodestyle/issues/466" title="new standard of Python style code" target="_blank">new standard of Python style code</a>, but at school we will use <code>PEP8</code>, <code>version 1.7.*</code>
Don&rsquo;t worry, <code>pycodestyle</code> is based on <code>pep8</code>.
The hardest part now is to install it for Python 3:</p>

<h4>Regular Ubuntu 14.04 install</h4>

<pre><code>$ sudo apt-get install python3-pep8
</code></pre>

<h4>Using Pip3</h4>

<h5>Install Pip3</h5>

<pre><code>$ sudo apt-get install python3-pip
</code></pre>

<h4>Install Pep8</h4>

<pre><code>$ pip3 install pep8
</code></pre>

<h4>Make sure you have the right version</h4>

<pre><code>$ pep8 --version
1.7
$
</code></pre>
>>>>>>> 02ac645e362e30de0b74ee69d42491090b4da15e
