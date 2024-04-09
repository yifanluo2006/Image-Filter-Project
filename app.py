from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask!'


@app.route('/test/<message>')
def test_method(message):
  print(message)
  return jsonify(message)


@app.route('/name/<name>')
def say_hi(name):
  print("hello, my name is " + name)
  return jsonify("success")


# {"num1": int, "num2": int}
@app.route('/addnums', methods=['POST'])
def add_two():
  try:
    data = request.json
    if data is not None:
      answer = data['num1'] + data['num2']
      return jsonify({"answer": answer})
    else:
      return jsonify({"msg": "invalid json"})
  except Exception as e:
    return jsonify({"error": e})


# Write an API that takes {"name":<string>,"age":<int>} as input, and returns "Hello, my name is <name>, and I am <age> years old." if the name is less than 8 charachters in length. If <name> is more than or equal to 8 charachters, return "Name too long!"


@app.route('/nameage', methods=['POST'])
def retrun_nameage():
  try:
    data = request.json
    if data is not None:
      name = str(data['name'])
      age = int(data['age'])
      return jsonify("Hello, my name is " + name + ", and I am " + str(age) +
                     " years old.")
    else:
      return jsonify({"msg": "invalid json"})
  except Exception as e:
    return jsonify({"error": e})

@app.route('/test', methods=['POST'])
def test():
  return jsonify({"name": "Yifan"})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000)
