<h1 class="gap">Project 0x14. Javascript - Web scraping</h1>

<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>Why Javascript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="/rltoken/c82PxNOgt77URzBvKDVcqg" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/GEBmmrmMUnGd20y4k6_4OA" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/B5xrtt_3vxQFbcCpW5rVsw" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>


<h4 class="task">
    0. Readme
</h4>
<p>Write a script that reads and prints the content of a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The content of the file must be read in <code>utf-8</code></li>
<li>If an error occurred during the reading, print the error object</li>
</ul>


<h4 class="task">
    1. Write me
</h4>
<p>Write a script that writes a string to a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The second argument is the string to write</li>
<li>The content of the file must be written in <code>utf-8</code></li>
<li>If an error occurred during while writing, print the error object</li>
</ul>

<h4 class="task">
    2. Status code
</h4>
 <p>Write a script that display the status code of a <code>GET</code> request.</p>

<ul>
<li>The first argument is the URL to request (<code>GET</code>)</li>
<li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
<li>You must use the module <code>request</code></li>
</ul>

<h4 class="task">
    3. Star wars movie title
</h4>
<p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p>

<ul>
<li>The first argument is the movie ID</li>
<li>You must use the <a href="https://swapi-api.hbtn.io/" title="Star wars API" target="_blank">Star wars API</a> with the endpoint <code>https://swapi-api.hbtn.io/api/films/:id</code></li>
<li>You must use the module <code>request</code></li>
</ul>

<h4 class="task">
    4. Star wars Wedge Antilles
</h4>
 <p>Write a script that prints the number of movies where the character &ldquo;Wedge Antilles&rdquo; is present.</p>

<ul>
<li>The first argument is the API URL of the <a href="https://swapi-api.hbtn.io/" title="Star wars API" target="_blank">Star wars API</a>: <code>https://swapi-api.hbtn.io/api/films/</code></li>
<li>Wedge Antilles is character ID <code>18</code> - your script <strong>must</strong> use this ID for filtering the result of the API</li>
<li>You must use the module <code>request</code></li>
</ul>

<h4 class="task">
    5. Loripsum
</h4>
 <p>Write a script that gets the contents of a webpage and stores it in a file.</p>

<ul>
<li>The first argument is the URL to request</li>
<li>The second argument the file path to store the body response</li>
<li>The file must be UTF-8 encoded</li>
<li>You must use the module <code>request</code></li>
</ul>

<h4 class="task">
    6. How many completed?
</h4>
<p>Write a script that computes the number of tasks completed by user id.</p>

<ul>
<li>The first argument is the API URL: <code>https://jsonplaceholder.typicode.com/todos</code></li>
<li>Only print users with completed task</li>
<li>You must use the module <code>request</code></li>
</ul>