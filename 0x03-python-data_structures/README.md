<h1 class="gap">Project 0x03. Python - Data Structures: Lists, Tuples</h1>

<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/2012/04/feynman-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>What are lists and how to use them</li>
<li>What are the differences and similarities between strings and lists</li>
<li>What are the most common methods of lists and how to use them</li>
<li>How to use lists as stacks and queues</li>
<li>What are list comprehensions and how to use them</li>
<li>What are tuples and how to use them</li>
<li>When to use tuples versus lists</li>
<li>What is a sequence</li>
<li>What is tuple packing</li>
<li>What is sequence unpacking</li>
<li>What is the <code>del</code> statement and how to use it</li>
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

<h3>C</h3>
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
    0. Print a list of integers
  </h4>
<p>Write a function that prints all integers of a list.</p>

<ul>
<li>Prototype: <code>def print_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>


<h4 class="task">
    1. Secure access to an element in a list
</h4>
<p>Write a function that retrieves an element from a list like in C.</p>

<ul>
<li>Prototype: <code>def element_at(my_list, idx):</code></li>
<li>If <code>idx</code> is negative, the function should return <code>None</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return <code>None</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<h4 class="task">
    2. Replace element
 </h4>
<p>Write a function that replaces an element of a list at a specific position (like in C).</p>

<ul>
<li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should not modify anything, and returns the original list</li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should not modify anything, and returns the original list</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<h4 class="task">
    3. Print a list of integers... in reverse!
</h4>
<p>Write a function that prints all integers of a list, in reverse order.</p>

<ul>
<li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<h4 class="task">
    4. Replace in a copy
  </h4>
<p>Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).</p>

<ul>
<li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should return a copy of the original <code>list</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return a copy of the original <code>list</code></li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<h4 class="task">
    5. Can you C me now?
 </h4>
<p>Write a function that removes all characters <code>c</code> and <code>C</code> from a string.</p>

<ul>
<li>Prototype: <code>def no_c(my_string):</code></li>
<li>The function should return the new string</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.replace()</code></li>
</ul>

<h4 class="task">
    6. Lists of lists = Matrix
</h4>
 <p>Write a function that prints a matrix of integers.</p>

<ul>
<li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
<li>Format: see example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<h4 class="task">
    7. Tuples addition
</h4>
<p>Write a function that adds 2 tuples.</p>

<ul>
<li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
<li>Returns a tuple with 2 integers:

<ul>
<li>The first element should be the addition of the first element of each argument</li>
<li>The second element should be the addition of the second element of each argument</li>
</ul></li>
<li>You are not allowed to import any module</li>
<li>You can assume that the two tuples will only contain integers</li>
<li>If a tuple is smaller than 2, use the value <code>0</code> for each missing integer</li>
<li>If a tuple is bigger than 2, use only the first 2 integers</li>
</ul>


<h4 class="task">
    8. More returns!
 </h4>
  <p>Write a function that returns a tuple with the length of a string and its first character.</p>


 <h4 class="task">
    9. Find the max
</h4>
<p>Write a function that finds the biggest integer of a list. </p>

<ul>
<li>Prototype: <code>def max_integer(my_list=[]):</code></li>
<li>If the list is empty, return <code>None</code></li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use the builtin <code>max()</code></li>
</ul>


<h4 class="task">
    10. Only by 2
</h4>
<p>Write a function that finds all multiples of 2 in a list.</p>

<ul>
<li>Prototype: <code>def divisible_by_2(my_list=[]):</code></li>
<li>Return a new list with <code>True</code> or <code>False</code>, depending on whether the integer at the same position in the original list is a multiple of 2</li>
<li>The new list should have the same size as the original list</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    11. Delete at
</h4>
 <p>Write a function that deletes the item at a specific position in a list.</p>

<ul>
<li>Prototype: <code>def delete_at(my_list=[], idx=0):</code></li>
<li>If <code>idx</code> is negative or out of range, nothing change (returns the same list)</li>
<li>You are not allowed to use <code>pop()</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    12. Switch
</h4>
<p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py" title="here" target="_blank">here</a></li>
<li>Your code should be inserted where the comment is (line 4)</li>
<li>Your program should be exactly 5 lines long</li>
</ul>


<h4 class="task">
    13. Linked list palindrome
</h4>
 <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Write a function in C that checks if a singly linked list is a palindrome.</p>

<ul>
<li>Prototype: <code>int is_palindrome(listint_t **head);</code></li>
<li>Return: <code>0</code> if it is not a palindrome, <code>1</code> if it is a palindrome</li>
<li>An empty list is considered a palindrome</li>
</ul>