from flask import Flask, request
from operations import add, sub, mult, div 

app = Flask(__name__)


@app.route("/add")
def add_nums():
  """Adds a and b from query"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = add(a,b)
  return f"<h1>{result} </h1>"

@app.route("/sub")
def sub_nums():
  """Subtracts a and b  from query"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = sub(a,b)
  return f"<h1>{result} </h1>"

@app.route("/mult")
def mult_nums():
  """Multiplies a and b from query"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = mult(a,b)
  return f"<h1>{result} </h1>"

@app.route("/div")
def div_nums():
  """Divides a and b from query"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = div(a,b)
  return f"<h1>{result} </h1>"

@app.route("/<operator>")
def operate_nums(operator):
  """Adds, subtracts, multiplies, or divides a and b from query string based on given operator"""
  operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = operators[operator](a,b)
  return f"<h1>{result} </h1>"

  