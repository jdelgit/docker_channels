# docker_channels
Django channels used in docker environment with nginx, redis, and daphne



Important channels files:

* routing.py  -- similar to urls.py but for websockets
* consumers.py -- can think of them as views kinda
* settings.py
* asgi.py

Within the consumer you define the functions to want to run/call. For example in my other project once a message is received I call the parse and return the resulting success/failure message via a return channel.

Important signals files:

* signals.py
* app.py
* \_\_init\_\_.py

Additionally if you're running django-channels on windows (if you decide not to use the docker file for example), you'll need to install : 

* Redis-server  (alternative is RabbitMQ)
* pywin32 and pypiwin32 (through pip)


Some things to note:

* The value entered in the form is irrelevant the output will always be the value hard-coded in de signals.py, I added the form in order to incorporate triggering the event after saving the form. (Didn't feel like making it too fancy).



**How to use it?**

Assuming you have docker-compose installed


```
docker-compose build
docker-compose up
```

I added a script that does the migration, it runs after 2 seconds.
The connect to the app at http://192.168.99.100 , 
otherwise check your docker ip .

```
docker-machine ip
```

Once connected there are 2 ways to observe the functionality.

1. Via browser terminal

 * open browser-console type ```document.ws.send(10)```
 * the output can be observed on your working terminal (docker)

2. Using the form link

* Submit the form, and it prints in the terminal

For method one, there's an inline JS that allows this. If you choose to implement this setup or something similar, be sere to **remove**
the line  ```document.ws = socket;``` in the template. as this allows you to do the action described above.



 
 
