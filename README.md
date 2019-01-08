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
To deploy the project, if the AWS credientials are configured, is pretty simple. 
<pre>chalice deploy</pre>

The response information will contain the lamda ARN and the rest API url. The rest API url is, well, a rest endpoint that can be accessed using rest calls. 

## This Example
Again, the examples in this repo are two endpoints that can be used to access the FizzBuzz Calcujlator logic. 
### Fizzbuzz Rules
<pre>
Any number that is a multiple of three shall return "fizz"
Any number that is a multiple of five shall return "buzz"
Any number that is a multiple of three AND five shall return "fizzbuzz"
Otherwise, return the original number. 
</pre>

I created two examples of endpoints. The first extracts the number out of the endpoint as an endpoint variable and passes it to the rules engine. 
<pre>

curl https://sf5oz1x80a.execute-api.us-west-1.amazonaws.com/api/fizzbuzz/{number}

</pre>
It grabs the number out of the endpoint and parses it into an int object, applies the rules, and returns the results json. 

The second example I included a few endpoint properties in the endpoint annotation such that one could only perform a POST on it and that it would expect application-content/json in the header. This also allowed the call to pass the request in as additional data in the json format 
<pre>

curl -X POST -H "Application/json" -H "Content-type: application/json" https://sf5oz1x80a.execute-api.us-west-1.amazonaws.com/api/fizzBuzzCalc/ -d '{ "request" : "6" }'

</pre>
