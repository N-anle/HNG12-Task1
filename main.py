from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import requests

app = Flask(__name__)
app.json.sort_keys = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False 


CORS(app)

def is_prime(number):

    number = int(number)

    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3,(int(math.sqrt(number))) + 1,2):
        if number % i == 0:
            return False
        
    return True

def is_perfect(number):

    number = int(number)

    if number <= 1:
        return False
    
    divisors = []

    for i in range(1 ,number // 2 + 1):
        if number % i == 0:
            divisors.append(i)
        else:
            continue
        
    divisors_sum = sum(divisors)

    if divisors_sum == number:
        return True
    else:
        return False
    

def digit_sum(number):

    digit_sum = 0
    number_int = int(number)

    
    if number_int != 0:
        number_int = abs(number_int)
        while number_int > 0:
            digit = number_int % 10
            digit_sum += digit
            number_int //= 10

    
    if int(number) < 0:
       digit_sum = digit_sum

    return digit_sum
    

def number_properties(number):
    original_number = int(number)

    

    properties_list = []

    if 2 <= original_number <= 9:
        properties_list.append("armstrong")

    #check for armstrong number
    if original_number > 0:
        temp_number = original_number
        digits = []
        cubed = []
        cubed_sum = 0

        while temp_number > 0:
            digit = temp_number % 10
            digits.append(digit) 
            temp_number //= 10
            
        for digit in digits:
            cubed.append((digit ** 3))

        cubed_sum = sum(cubed)
        
        if cubed_sum == original_number:
            properties_list.append("armstrong")

    #check for even and odd
    if original_number < 0:
        original_number = abs(original_number)
    

    if original_number % 2 == 0:
        properties_list.append("even")
    else:
        properties_list.append("odd")

    return properties_list

        

def get_fun_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math", timeout=20)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException:
        return "Fun fact unavailable"




@app.route("/api/classify-number")

def home():
    
    number = request.args.get("number")

    if number is None:
        null_error = {
            "number" : "null",
            "error" : "true"
        }

        return jsonify (null_error), 400

    try:
        int(number)

        
        digit_sum_result = digit_sum(number)
        property_list = number_properties(number)
        fun_fact = get_fun_fact(number)
        prime_number = is_prime(number)
        perfect_number = is_perfect(number)
            
            
        
       
        response = {
            "number" : number,
            "is_prime" : prime_number,
            "is_perfect": perfect_number,
            "digit_sum" : digit_sum_result,
            "properties" : property_list,
            "fun_fact" : fun_fact
        }

        return jsonify(response), 200

    except ValueError:
        val_error = {
            "number" : "alphabet",
            "error" : True
        }

        return jsonify(val_error), 400
    

if __name__ == "__main__":
    app.run(debug=True)