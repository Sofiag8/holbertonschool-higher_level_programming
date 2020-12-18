<h1 class="gap">Project 0x10. Python - Network #0</h1>
<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>What a URL is</li>
<li>What HTTP is</li>
<li>How to read a URL</li>
<li>The scheme for a HTTP URL</li>
<li>What a domain name is</li>
<li>What a sub-domain is</li>
<li>How to define a port number in a URL</li>
<li>What a query string is</li>
<li>What an HTTP request is</li>
<li>What an HTTP response is</li>
<li>What HTTP headers are</li>
<li>What the HTTP message body is</li>
<li>What an HTTP request method is</li>
<li>What an HTTP response status code is</li>
<li>What an HTTP Cookie is</li>
<li>How to make a request with cURL</li>
<li>What happens when you type google.com in your browser (Application level)</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>- A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your scripts will be tested on Ubuntu 14.04 LTS</li>
<li>All your Bash scripts should be exactly 3 lines long (<code>wc -l file</code> should print 3)</li>
<li>All your files should end with a new line</li>
<li>All your files must be executable</li>
<li>The first line of all your bash files should be exactly <code>#!/bin/bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>All <code>curl</code> commands must have the option <code>-s</code> (silent mode)</li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>The first line of all your Python files should be exactly <code>#!/usr/bin/python3</code></li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7.*)</li>
<li>All your modules should be documented: <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code></li>
<li>All your classes should be documented: <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code></li>
<li>All your functions (inside and outside a class) should be documented: <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code></li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

<h4 class="task">
    1. cURL to the end
</h4>
 <p>Write a Bash script that takes in a URL, sends a <code>GET</code> request to the URL, and displays the body of the response</p>

<ul>
<li>Display only body of a <code>200</code> status code response</li>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

<h4 class="task">
    2. cURL Method
</h4>
<p>Write a Bash script that sends a <code>DELETE</code> request to the URL passed as the first argument and displays the body of the response</p>

<ul>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>


  <h4 class="task">
    3. cURL only methods
</h4>
<p>Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.</p>

<ul>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>


<h4 class="task">
    4. cURL headers
</h4>
<p>Write a Bash script that takes in a URL as an argument, sends a <code>GET</code> request to the URL, and displays the body of the response</p>

<ul>
<li>A header variable <code>X-HolbertonSchool-User-Id</code> must be sent with the value <code>98</code></li>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

 <h4 class="task">
    5. cURL POST parameters
</h4>
 <p>Write a Bash script that takes in a URL, sends a <code>POST</code> request to the passed URL, and displays the body of the response</p>

<ul>
<li>A variable <code>email</code> must be sent with the value <code>hr@holbertonschool.com</code></li>
<li>A variable <code>subject</code> must be sent with the value <code>I will always be here for PLD</code></li>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

 <h4 class="task">
    6. Find a peak
</h4>
<p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Write a function that finds <strong>a peak</strong> in a list of unsorted integers.</p>

<ul>
<li>Prototype: <code>def find_peak(list_of_integers):</code></li>
<li>You are not allowed to import any module</li>
<li>Your algorithm must have the lowest complexity (<em>hint: you don&rsquo;t need to go through all numbers to find a peak</em>)</li>
<li><code>6-peak.py</code> must contain the function</li>
<li><code>6-peak.txt</code> must contain the complexity of your algorithm: <code>O(log(n))</code>, <code>O(n)</code>, <code>O(nlog(n))</code> or <code>O(n2)</code></li>
<li><strong>Note</strong>: there may be more than one peak in the list</li>
</ul>