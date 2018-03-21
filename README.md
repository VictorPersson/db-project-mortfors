# Bus Database #
#### How to use and install and the Bus databse!<br>

<strong>The database is built in postgreSQL and the program is written using Python3.6</strong>

### Windows ###
-------------
1. Download and tnstall [Python3.6](https://www.python.org/downloads/)
2. During the install process make sure you tick the option to get "PIP" as well.
3. Once python3 with pip is installed, open the cmd as an administrator and type ```pip install psycopg2```.
4. Install postgreSQL by visting their website and following the instructions!
5. Open up a new psql session and type \i mortfors_fv.sql in order to initialize the database.

### Mac ###
-------------
1. Download and install [Python3.6](https://www.python.org/downloads/)
2. During the install process make sure you tick the option to get "PIP" as well.
3. Once python3 with pip is installed, open your terminal and type
```sudo pip install psycopg2```.
<br>Enter your computers password and press enter <em>(PW won't visually show in your terminal window, but it's there)</em>
5. Open up a new psql session and type \i mortfors_fv.sql in order to initialize the database.

### Linux ###
-------------
1. Open your terminal
2. Download/install Python3 with ```sudo apt-get install python3```
2. Download/install PIP through ```apt-get install python-pip```
3. Once Python3 with PIP is installed, type ```sudo pip install psycopg2``` in order to get the psycopg2 library.
4. Install postgreSQL by typing sudo apt-get install postgresql in a terminal!
5. Open up a new psql session and type \i mortfors_fv.sql in order to initialize the database.

### How to use Bus databse ###
-------------
1. Clone/download all files in the repository.
2. Fling up your terminal or cmd.
3. Open the bus.py file with your texteditor of choice and add change the database credentials to your own.
4. Back in your terminal/cmd, navigate to the directory where you downloaded the bus.py file
5. Launch the application by entering ```python bus.py```
6. You can now use our Bus database application!
<br>
<p align="center">
  Don't forget to Star our repository/ <br>
  <strong>Politweet Enterprises™</strong>
</p>
