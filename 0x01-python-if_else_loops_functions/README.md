<h1 class="gap">Project 0x01. Python - About if/else, loops, functions</h1>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png" alt="" style="" /></p>

<h2>Learning objectives of this project</h2>
<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/2012/04/feynman-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>Why indentation is so important in Python</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use the <code>while</code> and <code>for</code> loops</li>
<li>How is Python&rsquo;s <code>for</code> different from <code>C</code>&lsquo;s?</li>
<li>How to use the <code>break</code> and <code>continues</code> statements</li>
<li>How to use <code>else</code> clauses on loops</li>
<li>What does the <code>pass</code> statement do, and when to use it</li>
<li>How to use <code>range</code></li>
<li>What is a function and how do you use functions</li>
<li>What does return a function that does not use any <code>return</code> statement</li>
<li>Scope of variables</li>
<li>What&rsquo;s a traceback</li>
<li>What are the arithmetic operators and how to use them</li>
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
 0. Positive anything is better than negative nothing
  </h4>
<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.</p>
<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py" title="here" target="_blank">here</a></li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random. randint</code> do. Please do not touch this code</li>
<li>The output of the program should be:

<ul>
<li>The number, followed by

<ul>
<li>if the number is greater than 0: <code>is positive</code></li>
<li>if the number is 0: <code>is zero</code></li>
<li>if the number is less than 0: <code>is negative</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>

 <h4 class="task">
    1. The last digit
  </h4>
<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py" title="here" target="_blank">here</a></li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random.randint</code> do. <strong>Please do not touch this code</strong>. This line should not change: <code>number = random.randint(-10000, 10000)</code></li>
<li>The output of the program should be:

<ul>
<li>The string <code>Last digit of</code>, followed by</li>
<li>the number, followed by</li>
<li>the string <code>is</code>, followed by the last digit of <code>number</code>, followed by

<ul>
<li>if the last digit is greater than 5: the string <code>and is greater than 5</code></li>
<li>if the last digit is 0: the string <code>and is 0</code></li>
<li>if the last digit is less than 6 and not 0: the string <code>and is less than 6 and not 0</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>


 <h4 class="task">
    2. I sometimes suffer from insomnia. And when I can&#39;t fall asleep, I play what I call the alphabet game
</h4>
<p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>
<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    3. When I was having that alphabet soup, I never thought that it would pay off
  </h4>
<p>Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>

<ul>
<li>Print all the letters except <code>q</code> and <code>e</code></li>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store characters in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    4. Hexadecimal printing
  </h4>
<p>Write a program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)</p>

<ul>
<li>You can only use one <code>print</code> function with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    5. 00...99
  </h4>
<p>Write a program that prints numbers from <code>0</code> to <code>99</code>.</p>

<ul>
<li>Numbers must be separated by <code>,</code>, followed by a space</li>
<li>Numbers should be printed in ascending order, with two digits</li>
<li>The last number should be followed by a new line</li>
<li>You can only use no more than 2 <code>print</code> functions with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
  </h4>
 <p>Write a program that prints all possible different combinations of two digits.</p>

<ul>
<li>Numbers must be separated by <code>,</code>, followed by a space</li>
<li>The two digits must be different</li>
<li><code>01</code> and <code>10</code> are considered the same combination of the two digits <code>0</code> and <code>1</code></li>
<li>Print only the smallest combination of two digits</li>
<li>Numbers should be printed in ascending order, with two digits</li>
<li>The last number should be followed by a new line</li>
<li>You can only use no more than 3 <code>print</code> functions with string format</li>
<li>You can only use no more than 2 loops in your code</li>
<li>You are not allowed to store numbers or strings in a variable</li>
<li>You are not allowed to import any module</li>
</ul>


  <h4 class="task">
    7. islower
  </h4>
<p>Write a function that checks for lowercase character. </p>

<ul>
<li>Prototype: <code>def islower(c):</code></li>
<li>Returns <code>True</code> if <code>c</code> is lowercase</li>
<li>Returns <code>False</code> otherwise</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
<li><a href="https://docs.python.org/3.4/library/functions.html?highlight=ord#ord" title="Tips: ord()" target="_blank">Tips: ord()</a></li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

<h4 class="task">
    8. To uppercase
  </h4>
  <p>Write a function that prints a string in uppercase followed by a new line.</p>

<ul>
<li>Prototype: <code>def uppercase(str):</code></li>
<li>You can only use no more than 2 <code>print</code> functions with string format</li>
<li>You can only use one loop in your code</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
<li><a href="https://docs.python.org/3.4/library/functions.html?highlight=ord#ord" title="Tips: ord()" target="_blank">Tips: ord()</a></li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

 <h4 class="task">
    9. There are only 3 colors, 10 digits, and 7 notes; it&#39;s what we do with them that&#39;s important
 </h4>
 <p>Write a function that prints the last digit of a number.</p>

<ul>
<li>Prototype: <code>def print_last_digit(number):</code></li>
<li>Returns the value of the last digit</li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

 <h4 class="task">
    10. a + b
 </h4>
 <p>Write a function that adds two integers and returns the result.</p>

<ul>
<li>Prototype: <code>def add(a, b):</code></li>
<li>Returns the value of <code>a + b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

 <h4 class="task">
    11. a ^ b
  </h4>
 <p>Write a function that computes <code>a</code> to the power of <code>b</code> and return the value.</p>

<ul>
<li>Prototype: <code>def pow(a, b):</code></li>
<li>Returns the value of <code>a ^ b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>


 <h4 class="task">
    12. Fizz Buzz
  </h4>
<p>Write a function that prints the numbers from 1 to 100 separated by a space. </p>

<ul>
<li>For multiples of three print <code>Fizz</code> instead of the number and for multiples of five print <code>Buzz</code>. </li>
<li>For numbers which are multiples of both three and five print <code>FizzBuzz</code>.</li>
<li>Prototype: <code>def fizzbuzz():</code></li>
<li>Each element should be followed by a space</li>
<li>You are not allowed to import any module</li>
</ul>

<p>You don&rsquo;t need to understand <code>__import__</code></p>

 <h4 class="task">
    13. Insert in sorted linked list
  </h4>
 <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Write a function in C that inserts a number into a sorted singly linked list.</p>

<ul>
<li>Prototype: <code>listint_t *insert_node(listint_t **head, int number);</code></li>
<li>Return: the address of the new node, or <code>NULL</code> if it failed</li>
</ul>