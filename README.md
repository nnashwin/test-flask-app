# Test Flask React App
> Interactive folder metadata for a more enabled future

## Install

### Install Server Packages
Ensure that you have pip3 and python3 installed on your system. 
After you have that, go to the api directory and run the following:
```bash
$ py3 -m venv venv && source venv/bin/activate && pip3 -r requirements.txt
```

If everything worked out, you should see the required dependencies downloaded in the terminal.

### Install Client Packages

To install the client packages, we recommend you install a valid version of Javascript and the yarn dependency management tool globally if you haven't done so yet. 

```bash
$ npm i -g yarn
```

Afterwards, run the yarn install command in the root directory to install all required client side packages.

```bash
$ yarn install
```

You should see the required packages downloaded.

## Run
If you have already activated your virtual env (source venv/bin/activate), you can build the client-side application and run the flask server by using the npm script 'start'.

```bash
$ yarn start
```

If everything has been completed up until this point, you should be able to hit a running flask server with the application in your browser [here](http://localhost:5000/).
