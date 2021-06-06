<h1 align="center">
  <img src="https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/32/film.png"/>
  CineManagerDB
</h1>

<h5 align="center">A comprehensive theatre management and ticket booking system</h5>
<h6 align="center">Written during my 5th semester BE for a course specified mini project in Database Management Systems (DBMS).</h6>

## 

<p align="center">
The system follows a 3-tier architecture, with a web based front end, Python + Flask as the HTTP server and router, and MySQL server for the database. JavaScript is used to build AJAX requests from the front end, which are served by a Python server running Flask as the application framework. MySQL's Python connector is used to query the MySQL server, which executes the queries on a relational database in 3rd Normal Form.
</p>
<p align="center">
The system is built to serve as an onsite booking and management system for a theatre (franchise). Two actors are considered, one being the cashier at the booking kiosk, who books tickets in exchange for payment, and the other being the manager who views statistics, alters pricing structures, schedules showings of movies, and adds new movies that are to be premiered.
</p>
<p align="center">
All HTTP requests to Flask are made via encrypted POST messages. The system is designed to be secure, robust and flexible. The requirements mandated the use of a stored procedure and a trigger in MySQL. An ER to schema mapping was to be performed and the schema was required to be normalised to 3NF.
</p>

## 

<img src="/art/1.gif?raw=true"/>
<img src="/art/2.gif?raw=true"/>
<img src="/art/3.gif?raw=true"/>

## Documentation

 ####  [Project report and manual](https://docs.google.com/document/d/1FM910xSRuvSdctJPRQz1x_DkcXHST_NvCTRobD6exUI/edit?usp=sharing)

<br />

## Entity Relationship Diagram
 <a href="https://imgur.com/FqtbNFe"><img src="https://i.imgur.com/FqtbNFe.png" title="source: imgur.com" /></a>
 
<br />

## Database Schema
 <a href="https://imgur.com/Ldlxg5Y"><img src="https://i.imgur.com/Ldlxg5Y.png" title="source: imgur.com" /></a>
 
<br />

## Functional Dependencies
 <a href="https://imgur.com/DtWk0Va"><img src="https://i.imgur.com/DtWk0Va.png" title="source: imgur.com" /></a>
 
<br />

##

<a href="https://imgur.com/E76mfpY"><img src="https://i.imgur.com/E76mfpY.png" title="source: imgur.com" /></a>

<br />

## Dependencies
 <p> <strong>Flask</strong> Python HTTP router</p>
 <p> <strong>MySQL</strong> Database server</p>
 
 <br />

## External Libraries
 <p> <strong>Bootstrap</strong> CSS structure</p>
 <p> <strong>JQuery</strong> AJAX requests, and general JS functionality</p>
 <p> <strong>pickadate.js</strong> Date and time picker</p>
 <br />

## 

```
# MySQL server must have an account with username ‘root’ and password ‘root123’ 
# (changeable within the runQuery function in app.py)
# This account needs read/write access to all tables in the db_theatre database (or root privileges)

# Initialise MySQL:

source /path/to/CineManagerDB/initialise.sql

# Use pip to install mysql-connector and flask, use python 3.6 to run app.py 
# Visit the website by vising http://localhost:5000 

Login as "manager" (password "manager"), to add new movies, schedule shows, alter ticket prices, and view bookings.
Login as "cashier (password "cashier"), to book seats for scheduled shows.

Usernames and passwords can be changed in app.py

```
<br />

##
*Please do not plagiarise.*
