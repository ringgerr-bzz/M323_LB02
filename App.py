from functools import reduce

from flask import Flask, request, jsonify

from Multiplier import Multiplier

app = Flask(__name__)


# A1G
def calculate_discount(price, discount_rate):
    return price * (1 - discount_rate)


@app.route('/apply_discount', methods=['POST'])
def apply_discount():
    data = request.get_json()
    price = data.get('price', 0)
    discount_rate = data.get('discount_rate', 0)
    discounted_price = calculate_discount(price, discount_rate)
    return jsonify({"discounted_price": discounted_price})


# A1F
def process_immutable_values(original_data):
    return original_data + (100,)


def process_mutable_values(original_data):
    original_data.append(100)
    return original_data


@app.route('/immutable_example', methods=['GET'])
def immutable_example():
    immutable_data = (1, 2, 3)
    mutable_data = [1, 2, 3]
    processed_immutable = process_immutable_values(immutable_data)
    processed_mutable = process_mutable_values(mutable_data)
    return jsonify({
        "original_immutable": immutable_data,
        "processed_immutable": processed_immutable,
        "original_mutable": [1, 2, 3],
        "processed_mutable": processed_mutable
    })


# A1E

# Object Oriented
@app.route('/oo_multiply', methods=['GET'])
def oo_multiply():
    multiplier = Multiplier(5)
    numbers = [1, 2, 3, 4, 5]
    result = multiplier.multiply(numbers)
    return jsonify({"result": result})


# Procedural
@app.route('/procedural_multiply', methods=['GET'])
def procedural_multiply():
    factor = 5
    numbers = [1, 2, 3, 4, 5]
    result = [n * factor for n in numbers]
    return jsonify({"result": result})


def multiply_number(number, factor):
    return number * factor


# Functional
@app.route('/functional_multiply', methods=['GET'])
def functional_multiply():
    numbers = [1, 2, 3, 4, 5]
    factor = 5
    result = list(map(lambda x: multiply_number(x, factor), numbers))
    return jsonify({"result": result})


# B1G
def sort_numbers(numbers):
    return sorted(numbers)


@app.route('/sort_numbers', methods=['GET'])
def sort_numbers_route():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_numbers = sort_numbers(numbers)
    return jsonify({"sorted_numbers": sorted_numbers})


# B1F
def extract_numbers(data):
    return data.get('numbers', [])


def process_numbers(numbers, factor):
    return [multiply_number(number, factor) for number in numbers]


@app.route('/process_numbers', methods=['POST'])
def process_numbers_route():
    data = request.get_json()
    numbers = extract_numbers(data)
    factor = data.get('factor', 1)
    result = process_numbers(numbers, factor)
    return jsonify({"processed_numbers": result})


# B2G

def multiply(number, factor):
    return number * factor


multiply_function = multiply


@app.route('/multiply_via_function_variable', methods=['POST'])
def multiply_via_function_variable():
    data = request.get_json()
    number = data.get('number', 0)
    factor = data.get('factor', 1)

    result = multiply_function(number, factor)

    return jsonify({"result": result})


def apply_function_to_list(function, numbers):
    return [function(number) for number in numbers]


@app.route('/apply_function_to_numbers', methods=['POST'])
def apply_function_to_numbers():
    data = request.get_json()
    numbers = data.get('numbers', [])
    factor = data.get('factor', 1)

    result = apply_function_to_list(lambda x: multiply(x, factor), numbers)

    return jsonify({"result": result})


# B2F

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def apply_operation(x, y, operation):
    return operation(x, y)


@app.route('/apply_addition', methods=['POST'])
def apply_addition():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)

    result = apply_operation(x, y, add)

    return jsonify({"result": result})


@app.route('/apply_subtraction', methods=['POST'])
def apply_subtraction():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)

    result = apply_operation(x, y, subtract)

    return jsonify({"result": result})


@app.route('/apply_multiplication', methods=['POST'])
def apply_multiplication():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)

    result = apply_operation(x, y, multiply)

    return jsonify({"result": result})


# B2E

def create_multiplier(factor):
    def multiplier(number):
        return number * factor

    return multiplier


@app.route('/apply_closure', methods=['POST'])
def apply_closure():
    data = request.get_json()
    number = data.get('number', 1)
    factor = data.get('factor', 2)

    multiplier_function = create_multiplier(factor)

    result = multiplier_function(number)

    return jsonify({"result": result})


def create_discount_calculator(discount_rate):
    def discount(price):
        return price * (1 - discount_rate)

    return discount


@app.route('/apply_discount_closure', methods=['POST'])
def apply_discount_closure():
    data = request.get_json()
    price = data.get('price', 0)
    discount_rate = data.get('discount_rate', 0)

    discount_function = create_discount_calculator(discount_rate)

    discounted_price = discount_function(price)

    return jsonify({"discounted_price": discounted_price})


# B3G

@app.route('/square_number', methods=['POST'])
def square_number():
    data = request.get_json()
    number = data.get('number', 0)

    square = lambda x: x ** 2
    result = square(number)

    return jsonify({"result": result})


@app.route('/to_uppercase', methods=['POST'])
def to_uppercase():
    data = request.get_json()
    text = data.get('text', '')

    uppercase = lambda x: x.upper()
    result = uppercase(text)

    return jsonify({"result": result})


# B3F

@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    data = request.get_json()
    number1 = data.get('number1', 0)
    number2 = data.get('number2', 0)

    add = lambda x, y: x + y
    result = add(number1, number2)

    return jsonify({"result": result})


@app.route('/concatenate_strings', methods=['POST'])
def concatenate_strings():
    data = request.get_json()
    string1 = data.get('string1', '')
    string2 = data.get('string2', '')

    concatenate = lambda x, y: x + y
    result = concatenate(string1, string2)

    return jsonify({"result": result})


# B3E

@app.route('/sort_by_length', methods=['POST'])
def sort_by_length():
    data = request.get_json()
    strings = data.get('strings', [])

    sorted_strings = sorted(strings, key=lambda x: len(x))

    return jsonify({"sorted_strings": sorted_strings})


@app.route('/sort_by_second_value', methods=['POST'])
def sort_by_second_value():
    data = request.get_json()
    tuples = data.get('tuples', [])

    sorted_tuples = sorted(tuples, key=lambda x: x[1])

    return jsonify({"sorted_tuples": sorted_tuples})


# B4G

@app.route('/map_example', methods=['POST'])
def map_example():
    data = request.get_json()
    numbers = data.get('numbers', [])

    doubled_numbers = list(map(lambda x: x * 2, numbers))

    return jsonify({"doubled_numbers": doubled_numbers})


@app.route('/filter_example', methods=['POST'])
def filter_example():
    data = request.get_json()
    numbers = data.get('numbers', [])

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    return jsonify({"even_numbers": even_numbers})


@app.route('/reduce_example', methods=['POST'])
def reduce_example():
    data = request.get_json()
    numbers = data.get('numbers', [])

    sum_of_numbers = reduce(lambda x, y: x + y, numbers)

    return jsonify({"sum_of_numbers": sum_of_numbers})


# B4F

@app.route('/combined_map_filter_reduce', methods=['POST'])
def combined_map_filter_reduce():
    data = request.get_json()
    numbers = data.get('numbers', [])

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    doubled_numbers = list(map(lambda x: x * 2, even_numbers))

    sum_of_doubled_numbers = reduce(lambda x, y: x + y, doubled_numbers)

    return jsonify({
        "original_numbers": numbers,
        "even_numbers": even_numbers,
        "doubled_numbers": doubled_numbers,
        "sum_of_doubled_numbers": sum_of_doubled_numbers
    })



# B4E

@app.route('/complex_map_filter_reduce', methods=['POST'])
def complex_map_filter_reduce():
    data = request.get_json()
    products = data.get('products', [])

    filtered_products = list(filter(lambda p: 10 <= p['price'] <= 50, products))

    updated_products = list(map(lambda p: {**p, 'price': p['price'] * 1.2}, filtered_products))

    total_cost = reduce(lambda total, p: total + p['price'], updated_products, 0)

    return jsonify({
        "original_products": products,
        "filtered_products": filtered_products,
        "updated_products": updated_products,
        "total_cost": total_cost
    })


if __name__ == '__main__':
    app.run(debug=True)
