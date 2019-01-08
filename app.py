from chalice import Chalice
import json

app = Chalice(app_name='fizzbuzzcalculator')


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

