# Trevor (SQL Injection)

For the first week of the project, Trevor spent time using Google to 
understand what an SQL injection is, and how to perform one.  An SQL
injection is a web-based attack wherein the attacker might gain access
to a system by using SQL syntax in a form text entry field.  

In a Login form, the backend program might utilize code that takes the
user's entry and stores it in a variable called userIDEntry.  Then, the
JavaScript code would look like this code from 
https://www.w3schools.com/sql/sql_injection.asp:

``` JavaScript
txtUserId = getRequestString("UserId");
txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;
```

To view information about the system, the attacker might provide the
entry:

```
105 OR 1 = 1
```

The resultant SQL entry would then be

```
SELECT * FROM Users WHERE UserId = 105 OR 1 = 1;
```

This would return the Users table for the attacker to see.  If the
Users table also contains passwords, then the attacker has attained
a complete list of usernames and passwords for the site.  Similar code
can also be used to gain unauthorized access to a system.

# Evan (XSS in Javascript)

## Cross-Site Scripting 
XSS is a class of attacks that involve injecting client side scripts through the website which then renders to other users. 

A famous example is the self retweeting heart;  

``` html
<script class="xss">$('.xss').parents().eq(1).find('a').eq(1).click();$('[data-action=retweet]').click();alert('XSS in Tweetdeck')</script>♥
```

This attack took advantage of the fact that TweetDeck, a 3rd party Twitter client didn't have any filtering for javascript inside of tweets. In general, it was assumed that the Twitter backend handled this, but unfortunately they did not either.

Let's break down each part of this tweet to see what's up. 

The first `<script class="xss">` defines a special HTML element that allows the execution of javascript code on the page. It also defines a "class" which serves as a label that we can point back to in a moment. 

Then, we'll take advantage of jquery to find "ourselves" (or the script tag) with `$('.xss')`. Then we'll grab the first parent element with `.parents().eq(1)`. This then lets us look for a link, or "anchor" with `.find('a').eq(1)`. 

This link happens to be the "retweet" button. So we'll click it: `.click()`. We can then confirm the action with `$('[data-action=retweet]').click()`. 

Since the original creator was not malicious and simply trying to expose a vulnerability, he pops up an alert: `alert('XSS in Tweetdeck')`. 

Then finally, we close the script and add a heart for flair: `</script>♥`.

## Preventing these attacks

The general strategy with dealing with these sorts of attacks is to avoid putting untrusted data in unallowed locations. 

According to the owasp wiki: 

Never put untrusted data in script tags.
``` html
<script> DONT PUT IT HERE </script>
```

Never put untrusted data inside of an html comment.
``` html
<!-- NOT IN HERE EITHER -->
```

Never put untrusted data in an html attribute
``` html
<div "DONT PUT BAD STUFF BYE THERE"=test>
```

Never put untrusted data in a tag name
``` html
<NOTAGNAMEHEREEITHER />
```

Never put untrusted data in CSS 
``` html
<style> NOTHING IN HERE </style>
```

# Max 
In the first week I decided to look up how to alter the clipboard on a windows machine from an application that was always running. 
SetClipboardData is an API that allows the user to alter the clipboard. Currently, this is my number one idea on how to do this. I would run
a process in the background, constantly searching if a particular input from the clipboard had happened yet.
Being an APT(advanced persistent threat), I was curious how we could get this on the person's computer. So, I have been messing around with 
downloading Microsoft Word files from the internet, then having them execute a command to open powershell. From there, someone could 
easily run a command to run the malware to change the application. 

So far, this has been a very fun project, I am looking forward to fully implementing this!
