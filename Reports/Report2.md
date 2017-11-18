# Evan
This week, I worked on setting up a basic website that lets users post items on the page. Each user can post something via an unprotected input box. This will serve as a practice site for a XSS site. 

![Screenshot](https://i.imgur.com/PkyydUj.png) 

This will allow a malicious user post some JS code, which will get run on the page of anyone else who went to the site.

For example, the following, when entered into the input would cause an alert "XSS" to appear on every other persons computer. 

``` 
Hacks<script>alert("XSS!");</script>
```

# Max 

# Trevor
