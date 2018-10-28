<h1 align="center">
  <img src="https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/32/film.png"/>
  CineManagerDB
</h1>

<h5 align="center">A comprehence theatre management and ticket booking system</h5>
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

## 

<br />

<a href="https://imgur.com/chz5FaL"><img src="https://i.imgur.com/chz5FaL.png" title="source: imgur.com" /></a>

<br />

## Use Cases
 * The ordinary Joe, who wants to sleep for as long as possible, and wake up at the latest possible time, yet still reaching work on time.
 * Someone invites you to have dinner with them in a restaurant at 8:30 PM, and you want to be alerted as to when you have to leave your home in order to reach the restaurant at exactly 8:30 PM, taking into account traffic conditions.
 * Many, many more use cases.

<br />

## APIs Used
<p><strong>Google Maps Distance Matrix API</strong> for predicting departure time</p>
<p><strong>Google Maps Places API</strong> for picking home and work locations</p>
<p><strong>Weatherbit.io API</strong> for predicted weather information at the time of departure</p>



<br />

## Tools Utilised
 <p> <strong>Assets:</strong> Photoshop and Illustrator (for bitmaps)</p>
 <p> <strong>Code:</strong> IntelliJ Idea (and Android Studio for Gradle and Manifest stuff)</p>
 <p> <strong>XML markup:</strong> Sublime 3 (our favourite text editor!)</p>
 
 <br />

## InGenius 2017
  Designed and Written through the course of the 24-hour hackathon held on September 24th, 2017. Including planning and creation of assets, it took us about a week.

<br />

## Kalpana 2017
  Presented during the first ever iteration of PESIT's IEEE charity project exhibition, Kalpana, held on October 28th, 2017. The event had strong emphasis on empowerment of women in engineering, participation required at least one female team member, which this project conveniently had.

<br />

## Creators
<p><strong>Gokul Vasudeva</strong>   https://github.com/gokulvsd</p>
<p><strong>Anusha A</strong>   https://github.com/anushab05</p>
Coded on a single laptop, hence why the second collaborator doesn't have many commits.
<br />

##
```
You must use your own API keys, add the Google API key to the manifest, and the wuastaFragment.java 
by replacing "ADD_YOUR_KEY_HERE", and add the Weatherbit.io API key to the wuastaFragment.java by 
replacing "ADD_YOUR_WEATHER_KEY_HERE".
```
<br />

##
*The creators give permission to fork the repository and reuse code, but publishing code onto the play store with the core functionality of this app is prohibited, not to mention, thats a pretty douchy thing to do.*
