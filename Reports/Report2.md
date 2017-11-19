# Evan

# Max 

# Trevor

My progress for this week was focused on building a basic web-based application to take user login input
and run that through a MySQL Database.  The application is written in JavaScript using the Node.js framework,
and referencing a MySQL Database created in an Ubuntu virtual machine.  It will ask a user to enter a username 
and password, and it will send the user's input to the database for authentication.  For the purpose of 
demonstrating the potential impact of an SQL injection, the first version will have no countermeasures.
These countermeasures will be added later.

The first step for building this application was setting up Node.js on a virtual Ubuntu machine.  Next, I
had to perform some troubleshooting in order to run a basic Node app that has no connection to a database;
this first application only displays an HTML page in order demonstrate that Node was installed successfully.

Finally, earlier in the week, I had learned how to connect to and interact with a database from a Python
script.  Since I have never used the Python equivalent for Node.js, I decided it would be easier to learn
a new library for an SQL database connection.  Thus, I wrote a script to connect with the database and
interact with tables I created for this project.  I am in the process of debugging as of this writing.
