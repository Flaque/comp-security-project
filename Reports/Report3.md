# Trevor

I have successfully tested a basic Node app to be vulnerable to SQL injections.  In addition, I have looked into various methods of preventing SQL injections.  Among these is a setting in NodeJS that allows multiple SQL queries to be sent over a connection to the database, which is disabled by default.  Thus, entering into the username field 'Trevor"; INSERT INTO Users VALUES (...)' will result in an error.  However, this leaves the vulnerability to gaining authentication with the line 'Trevor" OR 1=1'.  This can be dealt with via a string parser, or with a carefully designed authentication algorithm in the back end of the application.

Some SQL injections that will be demonstrated with this basic app include authenticating with a valid password but no valid username, altering a database, and removing tables created specifically for this demonstration.  

In addition to testing, I conducted research on when the SQL injection attack has been used before.  According to an article by Sean Michael Kerner (https://www.esecurityplanet.com/network-security/how-was-sql-injection-discovered.html), Jeff Foristal wrote the first public discussion of SQL injections in 1998.  At the time, he was writing on how to hack Windows NT servers.  To this day, SQL injections are among the most common attacks.  

As recently as early October 2017, researcher Anthony Ferrara discovered a bug in WordPress that allowed an for website takeover (http://www.thewhir.com/web-hosting-news/wordpress-issues-emergency-patch-for-sql-injection-vulnerability).  According to another article by Thomas Fox-Brewster at Forbes, SQL injections were used for the cyberattacks that led to the leak of Game of Thrones episodes (https://www.forbes.com/sites/thomasbrewster/2017/11/21/basic-hacker-or-elite-cyber-spy-feds-say-this-iranian-tried-to-extort-hbo-for-6bn/#1d39affd2255).

# Max

This project has proven to be quite complicated to make secret...There are so many ways to push back hackers, but also so many vulnerbilities. After creating a python script to change the clipboard, I was able to convert this into an executable. Which seemed all fine and dandy until the executable could only be ran inside of the folder with all of its dependentcies. 

Most of my time has been spent on making a script to ensure that the the executable gets ran. So, when the microsoft word file is opened, it goes to the internet to download a powershell script that I wrote (I all had to learn how to use powershell scripts). However, .ps1 files are banned from being ran on one computers. So, I had to find a bypass for this. With a couple of bypassing flags, I found a way to run the powershell scripts. This powershell script downloads the malicious clipboard folder from the internet, unzips it, then executes it, inside of the windows folder. Doing this from a powershell script was not the easiet thing to do in the world; took a ton of time to understand how all of it works. At the end of the run, it will change the item on the clipboard whenever the value "11" is on it.

I have found out that this hacking sort of thing takes committment! It's not nearly as simple as I thought it was; there are very few rules to work off of, books to read and videos to watch. It is an art of perservance that most people do not understand. The stuff I wrote above is what worked! I tried a ton of shell scripting, putting the code all in microsoft word, downloading links differently...and this is just the tip of the iceberg for what I did for this project that did not work out. Perservance is key!

#Evan

