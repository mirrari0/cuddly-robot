from chalice import Chalice
import json

app = Chalice(app_name='helloworld')


@app.route('/')
def index():
    return {'team-sugar-skulls': ['tori','jared','steve','anthony','anthony']}

@app.route('/fizzbuzz/{number}')
def fizzbuzz(number):
    return { 'result' : fizzbuzzCalculator(int(number)) }

@app.route('/fizzBuzzCalc', methods=['POST'], content_types=['application/json'])
def fizzBuzzCalc():
    return { 'result' : fizzbuzzCalculator(int(app.current_request.json_body['request'])) }

def fizzbuzzCalculator(n):

    if n == 0:
        return str(n)
    elif n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
