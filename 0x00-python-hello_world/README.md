<h1 class="gap"> Project 0x00. Python - Hello, World</h1>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg" alt="" style="" /></p>

<h2>For this project I had the following resources</h2>

<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="https://docs.python.org/3.4/tutorial/index.html" title="The Python tutorial" target="_blank">The Python tutorial</a> (<em>Read the first three chapters</em>)</li>
<li><a href="https://docs.python.org/3.4/tutorial/appetite.html" title="Whetting Your Appetite" target="_blank">Whetting Your Appetite</a> </li>
<li><a href="https://docs.python.org/3.4/tutorial/interpreter.html" title="Using the Python Interpreter" target="_blank">Using the Python Interpreter</a> </li>
<li><a href="https://docs.python.org/3.4/tutorial/introduction.html" title="An Informal Introduction to Python" target="_blank">An Informal Introduction to Python</a> (<em>Read up until &ldquo;3.1.2. Strings&rdquo; included</em>)</li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="https://www.python.org/dev/peps/pep-0008/" title="PEP 8 -- Style Guide for Python Code" target="_blank">PEP 8 &ndash; Style Guide for Python Code</a> </li>
</ul>

<h2>The learning objectives are the following:</h2>
<p>At the end of this project, you are expected to be able to <a href="/rltoken/fBqNUTa-ZywgkDpUYfAzAQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>Who created Python</li>
<li>Who is Guido van Rossum</li>
<li>Where does the name &lsquo;Python&rsquo; come from</li>
<li>What is the Zen of Python</li>
<li>How to use the Python interpreter</li>
<li>How to print text and variables using <code>print</code></li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Holberton Python coding style and how to check your code with <code>PEP 8</code></li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file at the root of the <code>holbertonschool-higher_level_programming</code> repo, containing a description of the repository</li>
<li>A <code>README.md</code> file, at the root of the folder of <em>this</em> project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version <code>1.7.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Shell Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 14.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>wc -l file</code> should print 2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>All your files must be executable</li>
</ul>

<h3>C Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> <code>and -pedantic</code></li>
<li>All your files should end with a new line</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Dont forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>


<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Run Python file
  </h4>

  <p>Write a Shell script that runs a Python script.</p>

<p>The Python file name will be saved in the environment variable <code>$PYFILE</code></p>

<h4 class="task">
    1. Run inline
  </h4>
<p>Write a Shell script that runs Python code.</p>

<p>The Python code will be saved in the environment variable <code>$PYCODE</code></p>

 <h4 class="task">
    2. Hello, print
  </h4>
  <p>Write a Python script that prints exactly <code>&quot;Programming is like building a multilingual puzzle</code>, followed by a new line.</p>

<ul>
<li>Use the function <code>print</code></li>
</ul>

<h4 class="task">
    3. Print integer
  </h4>
<p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" title="source code" target="_blank">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" title="here" target="_blank">here</a></li>
<li>The output of the script should be:

<ul>
<li>the number, followed by <code>Battery street</code>,</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast the variable <code>number</code> into a string</li>
<li>Your code must be 3 lines long</li>
<li>You have to use the new print numbers <a href="https://pyformat.info/#number" title="tips" target="_blank">tips</a> (with <code>.format(...)</code>)</li>
</ul>


  <h4 class="task">
    4. Print float
  </h4>
 <p>Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.</p>
<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py" 
title="here" target="_blank">here</a></li>
<li>The output of the program should be:

<ul>
<li><code>Float:</code>, followed by the float with only 2 digits</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast <code>number</code> to string</li>
<li>You have to use the new print formatting <a href="https://pyformat.info/#number_padding" title="tips" target="_blank">tips</a>  (with <code>.format(...)</code>)</li>
</ul>

<h4 class="task">
    5. Print string
  </h4>
<p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" title="source code" target="_blank">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" title="here" target="_blank">here</a></li>
<li>The output of the program should be:

<ul>
<li>3 times the value of <code>str</code></li>
<li>followed by a new line</li>
<li>followed by the 9 first characters of <code>str</code></li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to use any loops or conditional statement</li>
<li>Your program should be maximum 5 lines long</li>
</ul>


  <h4 class="task">
    6. Play with strings
  </h4>
 <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py" title="source code" target="_blank">source code</a> to print <code>Welcome to Holberton School!</code></p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements.</li>
<li>You have to use the variables <code>str1</code> and <code>str2</code> in your new line of code</li>
<li>Your program should be exactly 5 lines long</li>
</ul>

<h4 class="task">
    7. Copy - Cut - Paste
  </h4>
<p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py" title="source code" target="_blank">source code</a></p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 8 lines long</li>
<li><code>word_first_3</code> should contain the first 3 letters of the variable <code>word</code></li>
<li><code>word_last_2</code> should contain the last 2 letters of the variable <code>word</code></li>
<li><code>middle_word</code> should contain the value of the variable <code>word</code> without the first and last letters</li>
</ul>

 <h4 class="task">
    8. Create a new sentence
  </h4>
 <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" title="source code" target="_blank">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.</p>
<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 5 lines long</li>
<li>You are not allowed to create new variables</li>
<li>You are not allowed to use string literals</li>
</ul>

  <h4 class="task">
    9. Easter Egg
  </h4>
<p>Write a Python script that prints &ldquo;The Zen of Python&rdquo;, by TimPeters, followed by a new line.</p>

<ul>
<li>Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py</code>)</li>
</ul>


 <h4 class="task">
    10. Linked list cycle
  </h4>
  <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
<li>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution&rsquo;s runtime fast enough, does your solution require extra memory usage / mallocs, etc.</li>
</ul>

<p>Write a function in C that checks if a singly linked list has a cycle in it.</p>

<ul>
<li>Prototype: <code>int check_cycle(listint_t *list);</code></li>
<li>Return: <code>0</code> if there is no cycle, <code>1</code> if there is a cycle</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Only these functions are allowed: <code>write</code>, <code>printf</code>, <code>putchar</code>, <code>puts</code>, <code>malloc</code>, <code>free</code></li>
</ul>




<blockquote>
<p>Solving a problem is already a big win! but finding the best and optimal way to solve it, it&rsquo;s way better! Think about the most optimal / fastest way to do it.</p>
</blockquote>