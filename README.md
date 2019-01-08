# Python + Chalice AWS Trial/Kata
This is an example of a Chalice generated AWS endpoint in python. I extracted the fizzbuzz logic calculator from the react app to the python web service. 

## Python and Chalice setup
**Note**: References below to pip were actually pip3 on my machine after installing via homebrew

<a href='https://docs.python-guide.org/starting/install3/osx/#install3-osx'>Python Configuration Guide</a>

I opted to setup pipenv and virtualenv, but did not really use them. 

Once python is setup on your machine, install chalice using the pip3 install command.

<pre>pip3 install chalice</pre>

## AWS Configruation

## Project Creation
Chalice has a new project command that functions similar to yarn's create-react-app command. It will generate some boilerplate code in the app.py
. 

<pre>chalice new-project {directory}</pre>

The generated app.py will contain an example of the api endpoint annotation, otherwise it functions similar to regular python.

## Deploy Project

To deploy the project, if the AWS credientials are configured, 
