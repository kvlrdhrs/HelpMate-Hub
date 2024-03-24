<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Help_MatchMaker_0"></a>Help_MatchMaker</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">This program, “Help_MatchMaker,” is a simple matchmaking system designed to connect volunteers with volunteering opportunities. It’s built using Python and utilizes a PostgreSQL database via the psycopg2 library for managing data.</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Prerequisites_4"></a>Prerequisites</h2>
<ul>
<li class="has-line-data" data-line-start="5" data-line-end="6">Python 3.x</li>
<li class="has-line-data" data-line-start="6" data-line-end="8">PostgreSQL</li>
</ul>
<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="Installation_8"></a>Installation</h2>
<ol>
<li class="has-line-data" data-line-start="9" data-line-end="10">Clone this repository to your local machine.</li>
<li class="has-line-data" data-line-start="10" data-line-end="14">Install the required dependencies:<pre><code class="has-line-data" data-line-start="12" data-line-end="14" class="language-bash">pip install psycopg2
</code></pre>
</li>
<li class="has-line-data" data-line-start="14" data-line-end="16">Set up your PostgreSQL database and ensure that the credentials match with the ones specified in the code.</li>
</ol>
<h2 class="code-line" data-line-start=16 data-line-end=17 ><a id="Usage_16"></a>Usage</h2>
<p class="has-line-data" data-line-start="17" data-line-end="18">To run the program, execute the following command in your terminal:</p>
<pre><code class="has-line-data" data-line-start="19" data-line-end="21" class="language-bash">python <span class="hljs-built_in">help</span>_matchmaker.py
</code></pre>
<p class="has-line-data" data-line-start="22" data-line-end="23">Upon execution, the program will present a menu with options to help as a volunteer, search for a volunteer, or exit the program. Depending on the choice, users can add themselves as volunteers, search for volunteering opportunities, or exit the program.</p>
<h2 class="code-line" data-line-start=24 data-line-end=25 ><a id="Features_24"></a>Features</h2>
<ul>
<li class="has-line-data" data-line-start="25" data-line-end="26"><strong>Volunteer Registration</strong>: Users can register themselves as volunteers by providing their name, email, phone number, city, age, and the type of work they are interested in.</li>
<li class="has-line-data" data-line-start="26" data-line-end="27"><strong>Volunteer Search</strong>: Users can search for volunteering opportunities based on city, keyword, or both.</li>
<li class="has-line-data" data-line-start="27" data-line-end="29"><strong>Simple Navigation</strong>: The program offers a straightforward menu-based navigation system for ease of use.</li>
</ul>
<h2 class="code-line" data-line-start=29 data-line-end=30 ><a id="Structure_29"></a>Structure</h2>
<ul>
<li class="has-line-data" data-line-start="30" data-line-end="31"><strong>Menu Class</strong>: Defines functionalities to insert, delete, and update data in the PostgreSQL database.</li>
<li class="has-line-data" data-line-start="31" data-line-end="32"><strong>User Menus</strong>: Functions to display different menus based on user choices.</li>
<li class="has-line-data" data-line-start="32" data-line-end="34"><strong>Main Function</strong>: The entry point of the program, where users interact with the menus and functionalities.</li>
</ul>
<h2 class="code-line" data-line-start=34 data-line-end=35 ><a id="Contributing_34"></a>Contributing</h2>
<p class="has-line-data" data-line-start="35" data-line-end="36">Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.</p>
<h2 class="code-line" data-line-start=37 data-line-end=38 ><a id="License_37"></a>License</h2>
<p class="has-line-data" data-line-start="38" data-line-end="39">This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
