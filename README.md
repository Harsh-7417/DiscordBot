# DiscordBot (Ninja Bot)
A basic discord bot build in Python with MongoDB database

**Prerequisite:**
1) Install python 3.7
2) Install pip
3) Cretate virtual env
4) Install all dependencies : pip install -r requirements.txt
5) Update all required tokens/info in .env file

**How to run:**

python3 main.py


**Code info:**

#main.py :  Having Bot async methods to respond/react to client events.

#botUtilities.py : module having all custom API's

#configure.py : module maintaining DB connection(s) and env specific info


**Bot Usage:**
1) !google "text to search" --> Will display top 5 hyperlinks related to "<text to search>"
2) !recent "text to lookup" --> will display history of user related to "<text to lookup>". History is saved in mongoDB.
  

  #todo:
  Implement logging
