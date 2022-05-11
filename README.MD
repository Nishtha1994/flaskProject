How it works:
Please run the main.py
Click on local host
Type in /ping after local host - it will return okay
Delete the file from temp folder and type in /ping again you will see 503 
service error
/img will show a gif image and the request details are printed only for the /img

Further improvements:
I want to implement a before_request() to redirect the user to the /login page
if they are not logged yet.
Also, use SQLALchemy (more pythonic way of SQL) to create users and allow authorization so that logging is more efficient
If there are lot of requests coming in we can handle them by using memcache and enabling cache_on_arguments