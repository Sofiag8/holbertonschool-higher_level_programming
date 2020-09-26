<h1 class="gap"> Project 0x04. Python - More Data Structures: Set, Dictionary</h1>

<p><img src="https://i1.faceprep.in/Companies-1/python-lambda-functions-new.png" alt="" style=""/></p>


<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/2012/04/feynman-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>What are set and how to use them</li>
<li>What are the most common methods of set and how to use them</li>
<li>When to use sets versus lists</li>
<li>How to iterate into a set</li>
<li>What are dictionary and how to use them</li>
<li>When to use dictionaries versus lists or sets</li>
<li>What is a key in a dictionary</li>
<li>How to iterate into a dictionary</li>
<li>What is a lambda function</li>
<li>What is map, reduce and map functions</li>
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
    0. Squared simple
 </h4>
<p>Write a function that computes the square value of all integers of a matrix.</p>

<ul>
<li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:

<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You are allowed to use regular loops, <code>map</code>, etc.</li>
</ul>

<h4 class="task">
    1. Search and replace
</h4>
 <p>Write a function that replaces all occurrences of an element by another in a new list.</p>

<ul>
<li>Prototype: <code>def search_replace(my_list, search, replace):</code></li>
<li><code>my_list</code> is the initial list</li>
<li><code>search</code> is the element to replace in the list</li>
<li><code>replace</code> is the new element</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    2. Unique addition
</h4>
 <p>Write a function that adds all unique integers in a list (only once for each integer).</p>

<ul>
<li>Prototype: <code>def uniq_add(my_list=[]):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    3. Present in both
</h4>
 <p>Write a function that returns a set of common elements in two sets.</p>

<ul>
<li>Prototype: <code>def common_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    4. Only differents
</h4>
<p>Write a function that returns a set of all elements present in only one set.</p>

<ul>
<li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    5. Number of keys
  </h4>
<p>Write a function that returns the number of keys in a dictionary.</p>

<ul>
<li>Prototype: <code>def number_keys(a_dictionary):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    6. Print sorted dictionary
 </h4>
<p>Write a function that prints a dictionary by ordered keys.</p>

<ul>
<li>Prototype: <code>def print_sorted_dictionary(a_dictionary):</code></li>
<li>You can assume that all keys are strings</li>
<li>Keys should be sorted by alphabetic order</li>
<li>Only sort keys of the first level (don&rsquo;t sort keys of a dictionary inside the main dictionary)</li>
<li>Dictionary values can have any type</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    7. Update dictionary
  </h4>
 <p>Write a function that replaces or adds key/value in a dictionary.</p>

<ul>
<li>Prototype: <code>def update_dictionary(a_dictionary, key, value):</code></li>
<li><code>key</code> argument will be always a string</li>
<li><code>value</code> argument will be any type</li>
<li>If a key exists in the dictionary, the value will be replaced</li>
<li>If a key doesn&rsquo;t exist in the dictionary, it will be created</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    8. Simple delete by key
 </h4>
<p>Write a function that deletes a key in a dictionary.</p>

<ul>
<li>Prototype: <code>def simple_delete(a_dictionary, key=&quot;&quot;):</code></li>
<li><code>key</code> argument will be always a string</li>
<li>If a key doesn&rsquo;t exist, the dictionary won&rsquo;t change</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    9. Multiply by 2
  </h4>
<p>Write a function that returns a new dictionary with all values multiplied by 2</p>

<ul>
<li>Prototype: <code>def multiply_by_2(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>Returns a new dictionary</li>
<li>You are not allowed to import any module</li>
</ul>


<h4 class="task">
    10. Best score
  </h4>
  <p>Write a function that returns a key with the biggest integer value.</p>

<ul>
<li>Prototype: <code>def best_score(a_dictionary):</code></li>
<li>You can assume that all values are only integers</li>
<li>If no score found, return <code>None</code></li>
<li>You can assume all students have a different score</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    11. Multiply by using map
  </h4>
 <p>Write a function that returns a list with all values multiplied by a number without using any loops.</p>

<ul>
<li>Prototype: <code>def multiply_list_map(my_list=[], number=0):</code></li>
<li>Returns a new list:

<ul>
<li>Same length as <code>my_list</code></li>
<li>Each value should be multiplied by <code>number</code></li>
</ul></li>
<li>Initial list should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>Your file should be max 3 lines</li>
</ul>

<h4 class="task">
    12. Roman to Integer
 </h4>
<p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Create a function <code>def roman_to_int(roman_string):</code> that converts a <a href="https://en.wikipedia.org/wiki/Roman_numerals" title="Roman numeral" target="_blank">Roman numeral</a> to an integer.</p>

<ul>
<li>You can assume the number will be between 1 to 3999.</li>
<li><code>def roman_to_int(roman_string)</code> must return an integer</li>
<li>If the <code>roman_string</code> is not a string or <code>None</code>, return 0</li>
</ul>
