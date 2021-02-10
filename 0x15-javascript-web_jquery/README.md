# Project: 0x15. Javascript - Web JQuery

## Learning objectives

#### General 

* Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* How to select HTML elements in Javascript
* How to select HTML elements with jQuery
* What are differences between <code>ID</code>, <code>class</code> and <code>tag name</code> selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a <code>GET</code> request with jQuery Ajax
* How to make a <code>POST</code> request with jQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events


#### Import jQuery 
<pre><code>&lt;head&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
&lt;/head&gt;
</code></pre>


<hr class="gap">
<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. No jQuery
</h4>

Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):
* You must use <code>document.querySelector</code> to select the HTML tag</li>
* You can&rsquo;t use the jQuery API

<h4 class="task">
    1. With jQuery
</h4>

Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):

* You must use <code>document.querySelector</code> to select the HTML tag</li>
* You must use the jQuery API

<h4 class="task">
    2. Click and turn red
</h4>

Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:

* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API

<h4 class="task">
    3. Add `.red` class
</h4>
Write a Javascript script that adds the class <code>red</code> to the HTML tag <code>HEADER</code> when the user clicks on the tag <code>DIV#red_header</code>

* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API

<h4 class="task">
    4. Toggle classes
</h4>
Write a Javascript script that toggles the class of the HTML tag <code>HEADER</code> when the user clicks on the tag <code>DIV#toggle_header</code>:

* The <code>HEADER</code> tag must always have one class: <code>red</code> or <code>green</code>, never both in the same time, never empty.
* If the current class is <code>red</code>, when the user click on <code>DIV#toggle_header</code>, the class must be updated to <code>green</code> ; and the reverse.
* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API

<h4 class="task">
    5. List of elements
</h4>

Write a Javascript script that adds a <code>LI</code> element to a list when the user clicks on the tag <code>DIV#add_item</code>:
* The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code>
* The new element must be added to <code>UL.my_list</code>
* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API

<h4 class="task">
    6. Change the text
</h4>

Write a Javascript script that updates the text of the HTML tag <code>HEADER</code> to &ldquo;New Header!!!&rdquo; when the user clicks on <code>DIV#update_header</code>

* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API

<h4 class="task">
    7. Star wars character
</h4>

Write a Javascript script that fetches the <code>name</code> from this URL: <code>https://swapi-api.hbtn.io/api/people/5/?format=json</code>
* The name must be displayed in the HTML tag <code>DIV#character</code>
* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API

<h4 class="task">
    8. Star Wars movies
</h4>

Write a Javascript script that fetches and lists the <code>title</code> for all movies by using this URL: <code>https://swapi-api.hbtn.io/api/films/?format=json</code>
* All movie titles must be list in the HTML tag <code>UL#list_movies</code>
* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use jQuery API

<h4 class="task">
    9. Say Hello!
</h4>

Write a Javascript script that fetches from <code>https://fourtonfish.com/hellosalut/?lang=fr</code> and displays the value of <code>hello</code> from that fetch in the HTML&rsquo;s tag <code>DIV#hello</code>.

* The translation of &ldquo;hello&rdquo; must be displayed in the HTML tag <code>DIV#hello</code>
* You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag
* You must use the jQuery API
* Your script must work when it is imported from the <code>HEAD</code> tag

