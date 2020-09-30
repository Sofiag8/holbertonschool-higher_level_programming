<div align="center">
<h1 class="gap">Project 0x09. Python - Everything is object</h1>
</div>

<div align="center">
 <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg" alt="" style="" /><br /></p>
</div>

<h2>Background Context</h2>
<p> Now that I have a little bit knowledge in python, this project is about working with different types of objects. </p>


<p>This project is a little bit different than the usual projects. The first part is only questions about Python&rsquo;s specificity like &ldquo;What would be the result of&hellip;&rdquo;. 
You should <strong>read all documentation first (as usual :))</strong>, then take the time to <strong>think and brainstorm with your peers</strong> about what you think and why. <strong>Try to do this without coding anything for a few hours</strong>.</p>

<p>Trying examples in the Python interpreter will give you most of the answers without having to think about it. <strong>Don&rsquo;t go this route</strong>. First read, then think, then brainstorm together. Only then you can test in the interpreter.</p>

<p>It&rsquo;s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.
The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.</p>


<p>All answers should be only one line in a file. No space before or after the answer.</p>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (<code>version 1.7.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3><code>.txt</code> Answer Files</h3>

<ul>
<li>Only one line</li>
<li>No Shebang</li>
<li>All your files should end with a new line</li>
</ul>


<h2 class="gap">Tasks</h2>

  <h4 class="task">
    0. Who am I?
  </h4>
<p>What function would you use to print the type of an object?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

<h4 class="task">
    1. Where are you?
  </h4>
<p>How do you get the variable identifier (which is the memory address in the CPython implementation)?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

 <h4 class="task">
    2. Right count
 </h4>

<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 100
</code></pre>

 <h4 class="task">
    3. Right count =
  </h4>
  <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 89
</code></pre>

 <h4 class="task">
    4. Right count =
  </h4>
 <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a
</code></pre>

<h4 class="task">
    5. Right count =+
  </h4>
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a + 1
</code></pre>

<h4 class="task">
    6. Is equal
  </h4>
 <p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

 <h4 class="task">
    7. Is the same
</h4>
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

<h4 class="task">
    8. Is really equal
</h4>
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = &quot;Holberton&quot;
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

<h4 class="task">
    9. Is really the same
</h4>
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = &quot;Holberton&quot;
&gt;&gt;&gt; print(s1 is s2)
</code></pre>


  <h4 class="task">
    10. And with a list, is it equal
 </h4>
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3]
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

<h4 class="task">
    11. And with a list, is it the same
</h4>
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3]
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

<h4 class="task">
    12. And with a list, is it really equal
</h4>
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

 <h4 class="task">
    13. And with a list, is it really the same
</h4>
  <p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

<h4 class="task">
    14. List append
</h4>
<p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
</code></pre>

<h4 class="task">
    15. List add
</h4>
<p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
</code></pre>

 <h4 class="task">
    16. Integer incrementation
</h4>
 <p>What does this script print?</p>

<pre><code>def increment(n):
    n += 1

a = 1
increment(a)
print(a)
</code></pre>

<h4 class="task">
    17. List incrementation
</h4>
<p>What does this script print?</p>

<pre><code>def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
</code></pre>

<h4 class="task">
    18. List assignation
</h4>
<p>What does this script print?</p>

<pre><code>def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
</code></pre>

 <h4 class="task">
    19. Copy a list object
</h4>
  <p>Write a function <code>def copy_list(l):</code> that returns a <strong>copy</strong> of a list.</p>

<ul>
<li>The input list can contain any type of objects</li>
<li>Your file should be maximum 3-line long (no documentation needed)</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    20. Tuple or not?
</h4>
 <pre><code>a = ()
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

  <h4 class="task">
    21. Tuple or not?
</h4>
  <pre><code>a = (1, 2)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

 <h4 class="task">
    22. Tuple or not?
</h4>
  <pre><code>a = (1)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

<h4 class="task">
    23. Tuple or not?
</h4>
  <pre><code>a = (1, )
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

 <h4 class="task">
    24. Richard Sim&#39;s special #0
</h4>
<p>What does this script print?</p>

<pre><code>a = (1)
b = (1)
a is b
</code></pre>

  <h4 class="task">
    25. Richard Sim&#39;s special #1
</h4>
 <p>What does this script print?</p>

<pre><code>a = (1, 2)
b = (1, 2)
a is b
</code></pre>

 <h4 class="task">
    26. Richard Sim&#39;s special #2
</h4>
 <p>What does this script print?</p>

<pre><code>a = ()
b = ()
a is b
</code></pre>


<h4 class="task">
    27. Richard Sim&#39;s special #3
</h4>
 <pre><code>&gt;&gt;&gt; id(a)
139926795932424
&gt;&gt;&gt; a
[1, 2, 3, 4]
&gt;&gt;&gt; a = a + [5]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

  <h4 class="task">
    28. Richard Sim&#39;s special #4
</h4>
 <pre><code>&gt;&gt;&gt; a
[1, 2, 3]
&gt;&gt;&gt; id (a)
139926795932424
&gt;&gt;&gt; a += [4]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

 <h4 class="task">
    29. Python3: Mutable, Immutable... everything is object!
</h4>
<p>Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):</p>

<ul>
<li>introduction</li>
<li>id and type</li>
<li>mutable objects</li>
<li>immutable objects</li>
<li>why does it matter and how differently does Python treat mutable and immutable objects</li>
<li>how arguments are passed to functions and what does that imply for mutable and immutable objects</li>
</ul>

<p><em>If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.</em></p>

<p>Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top.
Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.</p>

<p>When done, please add all urls below (blog post, LinkedIn post, etc.)</p>

<p>Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.</p>



 <h4 class="task">
    35. Clear strings
</h4>
 <pre><code>guillaume@ubuntu:/python3$ cat string.py
a = &quot;HBTN&quot;
b = &quot;HBTN&quot;
del a
del b
c = &quot;HBTN&quot;
guillaume@ubuntu:/python3$
</code></pre>

<p>Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don&rsquo;t spell out the word):</p>

<ul>
<li>How many string objects are created by the execution of the first line of the script? (<code>106-line1.txt</code>)</li>
<li>How many string objects are created by the execution of the second line of the script (<code>106-line2.txt</code>)</li>
<li>After the execution of line 3, is the string object pointed by <code>a</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>106-line3.txt</code>)</li>
<li>After the execution of line 4, is the string object pointed by <code>b</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>106-line4.txt</code>)</li>
<li>How many string objects are created by the execution of the last line of the script (<code>106-line5.txt</code>)</li>
</ul>
