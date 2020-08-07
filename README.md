# Test Flask React App
> Interactive folder metadata for a more enabled future

## Install

### Install Server Packages
Ensure that you have pip3 and python3 installed on your system. 
After you have that, go to the api directory and run the following:
```bash
$ py3 -m venv venv && source venv/bin/activate && pip3 -r requirements.txt
```

If everything worked out, you should see the required dependencies downloading successfully in the terminal.

### Install Client Packages

To install the client packages, we recommend you install a valid version of Javascript and the yarn dependency management tool globally if you haven't done so yet. 

```bash
$ npm i -g yarn
```

Afterwards, run the yarn install command in the root directory to install all required client side packages.

```bash
$ yarn install
```

You should see the required packages downloading in the terminal.

## Run
If you have already activated your virtual env (source venv/bin/activate), you can build the client-side application and run the flask server by using the npm script 'start'.

```bash
$ yarn start
```

If everything has been completed up until this point, you should be able to hit a running flask server with the application in your browser [here](http://localhost:5000/).

## Design

***### Server Side
For this application, I wanted a simple data store that can be updated easily yet scaled out in the future.  Have worked with some sql previously, I felt that a really simple sqlite db file
could hold the data created through the create_db script.  The cool thing about using sqlite is that we can build on the simple structure while maintaining sql syntax / table definitions. 
As we incrementally add to the application, once the data needs grow past a certain point, we can change the connection in our creation script to query an actual sql database in the future.

I chose to use Flask due to its ease of development and setup. It seems more bare bones than a lot of other frameworks out there, and it was fun to work with and I was able to get off the ground quickly.

### Client Side
The client side is a basic create-react-app that builds into static files the server can serve from route. With hooks and other react features built in, I only needed to add a couple libraries (react-hook-form and immutability-helper) to aid development
and readability of code.

## Future Improvements
1. Adding some type of versioning / saving mechanism to the data folders on the server.
   - It would be nice to allow users to maintain their changes to folders with some type of persistance.  Even if it was something as simple as a save button, users could create and persist folders.

   - If we created a files table that had a many-to-one relationship with a record in a users table, we could allow each version to be saved into a database while incrementing the number. By adding a current version field in the users table, we could save, roll back, and even allow users to explore other previous versions of the folders and files they have created before.

2. Adding Drag and Drop.
   - This seems like a great project to use drag and drop.  I started down that path for a bit, but I think that it would be too much of a lift for the current scope of the project.  It would be nice to allow users to interact with the app in a more dynamic way.

3. Finding a standard, solid python trie library to use in the creation script.
    - Once I realized this problem was well solved with a trie, I did a quick search of the top python trie libraries out there with the correct apis I needed.  I didn't find ones with simple enough apis that met the needs of the project, and I felt I could write a small one up faster than it would take with the 3-5 hour deadline.  However, I am sure there is a solid open-source library out there that works out of the box.