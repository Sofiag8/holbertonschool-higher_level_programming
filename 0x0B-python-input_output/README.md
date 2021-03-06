<h1 class="gap">Project 0x0B. Python - Input/Output</h1>

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to open a file</li>
<li>How to write text in a file</li>
<li>How to read the full content of a file </li>
<li>How to read a file line by line</li>
<li>How to move the cursor in a file</li>
<li>How to make sure a file is closed after using it</li>
<li>What is and how to use the <code>with</code> statement</li>
<li>What is <code>JSON</code></li>
<li>What is serialization</li>
<li>What is deserialization</li>
<li>How to convert a Python data structure to a JSON string </li>
<li>How to convert a JSON string to a Python data structure</li>
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
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Read file
  </h4>
 <p>Write a function that reads a text file (<code>UTF8</code>) and prints it to stdout:</p>

<ul>
<li>Prototype: <code>def read_file(filename=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage <code>file permission</code> or <code>file doesn&#39;t exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    1. Number of lines
  </h4>
 <p>Write a function that returns the number of lines of a text file:</p>

<ul>
<li>Prototype: <code>def number_of_lines(filename=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage <code>file permission</code> or <code>file doesn&#39;t exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    2. Read n lines
  </h4>
<p>Write a function that reads <code>n</code> lines of a text file (<code>UTF8</code>) and prints it to stdout:</p>

<ul>
<li>Prototype: <code>def read_lines(filename=&quot;&quot;, nb_lines=0):</code></li>
<li>Read the entire file if <code>nb_lines</code> is lower or equal to <code>0</code> OR greater or equal to the total number of lines of the file</li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage <code>file permission</code> or <code>file doesn&#39;t exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    3. Write to a file
  </h4>
<p>Write a function that writes a string to a text file (<code>UTF8</code>) and returns the number of characters written:</p>

<ul>
<li>Prototype: <code>def write_file(filename=&quot;&quot;, text=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage file permission exceptions.</li>
<li>Your function should create the file if doesn&rsquo;t exist.</li>
<li>Your function should overwrite the content of the file if it already exists.</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    4. Append to a file
  </h4>
<p>Write a function that appends a string at the end of a text file (<code>UTF8</code>) and returns the number of characters added:</p>

<ul>
<li>Prototype: <code>def append_write(filename=&quot;&quot;, text=&quot;&quot;):</code></li>
<li>If the file doesn&rsquo;t exist, it should be created</li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage <code>file permission</code> or <code>file doesn&#39;t exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    5. To JSON string
  </h4>
<p>Write a function that returns the JSON representation of an object (string):</p>

<ul>
<li>Prototype: <code>def to_json_string(my_obj):</code></li>
<li>You don&rsquo;t need to manage exceptions if the object can&rsquo;t be serialized.</li>
</ul>

 <h4 class="task">
    6. From JSON string to Object
  </h4>
<p>Write a function that returns an object (Python data structure) represented by a JSON string:</p>

<ul>
<li>Prototype: <code>def from_json_string(my_str):</code></li>
<li>You don&rsquo;t need to manage exceptions if the JSON string doesn&rsquo;t represent an object.</li>
</ul>

<h4 class="task">
    7. Save Object to a file
  </h4>
 <p>Write a function that writes an Object to a text file, using a JSON representation:</p>

<ul>
<li>Prototype: <code>def save_to_json_file(my_obj, filename):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage exceptions if the object can&rsquo;t be serialized.</li>
<li>You don&rsquo;t need to manage file permission exceptions.</li>
</ul>

<h4 class="task">
    8. Create object from a JSON file
  </h4>
  <p>Write a function that creates an Object from a &ldquo;JSON file&rdquo;:</p>

<ul>
<li>Prototype: <code>def load_from_json_file(filename):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&rsquo;t need to manage exceptions if the JSON string doesn&rsquo;t represent an object.</li>
<li>You don&rsquo;t need to manage file permissions / exceptions.</li>
</ul>

<h4 class="task">
    9. Load, add, save
  </h4>
  <p>Write a script that adds all arguments to a Python list, and then save them to a file:</p>

<ul>
<li>You must use your function <code>save_to_json_file</code> from <code>7-save_to_json_file.py</code></li>
<li>You must use your function <code>load_from_json_file</code> from <code>8-load_from_json_file.py</code></li>
<li>The list must be saved as a JSON representation in a file named <code>add_item.json</code></li>
<li>If the file doesn&rsquo;t exist, it should be created</li>
<li>You don&rsquo;t need to manage file permissions / exceptions.</li>
</ul>

 <h4 class="task">
    10. Class to JSON
  </h4>
 <p>Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:</p>

<ul>
<li>Prototype: <code>def class_to_json(obj):</code></li>
<li><code>obj</code> is an instance of a Class</li>
<li>All attributes of the <code>obj</code> Class are serializable: list, dictionary, string, integer and boolean</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    11. Student to JSON
  </h4>
 <p>Write a class <code>Student</code> that defines a student by:</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>10-class_to_json.py</code>)</li>
<li>You are not allowed to import any module</li>
</ul>

 <h4 class="task">
    12. Student to JSON with filter
</h4>
<p>Write a class <code>Student</code> that defines a student by: (based on <code>11-student.py</code>)</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>10-class_to_json.py</code>):

<ul>
<li>If <code>attrs</code> is a list of strings, only attribute names contained in this list must be retrieved. </li>
<li>Otherwise, all attributes must be retrieved</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<h4 class="task">
    13. Student to disk and reload
 </h4>
<p>Write a class <code>Student</code> that defines a student by: (based on <code>12-student.py</code>)</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>10-class_to_json.py</code>):

<ul>
<li>If <code>attrs</code> is a list of strings, only attributes name contain in this list must be retrieved. </li>
<li>Otherwise, all attributes must be retrieved</li>
</ul></li>
<li>Public method <code>def reload_from_json(self, json):</code> that replaces all attributes of the <code>Student</code> instance:

<ul>
<li>You can assume <code>json</code> will always be a dictionary</li>
<li>A dictionary key will be the public attribute name</li>
<li>A dictionary value will be the value of the public attribute</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<p>Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)</p>

<h4 class="task">
    14. Pascal&#39;s Triangle
</h4>
 <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Create a function <code>def pascal_triangle(n):</code> that returns a list of lists of integers representing the Pascal&rsquo;s triangle of <code>n</code>:</p>

<ul>
<li>Returns an empty list if <code>n &lt;= 0</code></li>
<li>You can assume <code>n</code> will be always an integer</li>
</ul>