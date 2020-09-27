<h1 class="gap">Project 0x05. Python - Exceptions</h1>

<h2>Learning Objectives</h2>
<p> At the end of this project I am expected to be able to explain: </p>

<h3> General </h3>
<ul>
<li>What&rsquo;s the difference between errors and exceptions</li>
<li>What are exceptions and how to use them</li>
<li>When do we need to use exceptions</li>
<li>How to correctly handle an exception</li>
<li>What&rsquo;s the purpose of catching exceptions</li>
<li>How to raise a builtin exception</li>
<li>When do we need to implement a clean-up action after an exception</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

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

<h2 class="gap">Tasks</h2>
<h4 class="task">
    0. Safe list printing
  </h4>
 <p>Write a function that prints <code>x</code> elements of a list.</p>

<ul>
<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

  <h4 class="task">
    1. Safe printing of an integers list
  </h4>
 <p>Write a function that prints an integer with <code>&quot;{:d}&quot;.format()</code>.</p>

<ul>
<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>

 <h4 class="task">
    2. Print and count integers
  </h4>
  <p>Write a function that prints the first <code>x</code> elements of a list and only integers.</p>

<ul>
<li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).</li>
<li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
<li><code>x</code> can be bigger than the length of <code>my_list</code> - if it&rsquo;s the case, an exception will occur</li>
<li>Returns the real number of integers printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print an integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

  <h4 class="task">
    3. Integers division with debug
  </h4>
<p>Write a function that divides 2 integers and prints the result.</p>

<ul>
<li>Prototype: <code>def safe_print_division(a, b):</code></li>
<li>You can assume that <code>a</code> and <code>b</code> are integers</li>
<li>The result of the division should print on the <code>finally:</code> section preceded by <code>Inside result:</code></li>
<li>Returns the value of the division, otherwise: <code>None</code></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You have to use <code>&quot;{}&quot;.format()</code> to print the result</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    4. Divide a list
  </h4>
  <p>Write a function that divides element by element 2 lists.</p>

<ul>
<li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
<li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
<li><code>list_length</code> can be bigger than the length of both lists</li>
<li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
<li>If 2 elements can&rsquo;t be divided, the division result should be equal to <code>0</code></li>
<li>If an element is not an integer or float:

<ul>
<li>print: <code>wrong type</code></li>
</ul></li>
<li>If the division can&rsquo;t be done (<code>/0</code>):

<ul>
<li>print: <code>division by 0</code></li>
</ul></li>
<li>If <code>my_list_1</code> or <code>my_list_2</code> is too short

<ul>
<li>print: <code>out of range</code></li>
</ul></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    5. Raise exception
  </h4>
<p>Write a function that raises a type exception.</p>

<ul>
<li>Prototype: <code>def raise_exception():</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    6. Raise a message
  </h4>
<p>Write a function that raises a name exception with a message.</p>

<ul>
<li>Prototype: <code>def raise_exception_msg(message=&quot;&quot;):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
Advances Tasks
  </h4>
<p> This are not mandatory tasks but are designed to prepare the students to more challeging tasks</p>