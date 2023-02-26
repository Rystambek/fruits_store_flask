from flask import Flask, request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    fruits = db.all()
    html = '<html>'
    html += '<head><title>Fruit</title><style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: left;}</style></head>'
    html += '<body>'
    html += '<h1>Fruits</h1>'
    html += '<table>'
    html += '<tr><th>name</th> <th>quantity</th> <th>price</th> <th>type</th></tr>'
    for fruit in fruits:
        html += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
    html += '</table>'
    html += '</body>'
    html += "</html>"
    return html


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    fruit = request.get_json(force=True)
    fruits = db.add(fruit)
    return fruits


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    fruits = db.get_by_type(type)
    if fruits :
        html = """<html>
        <head>
        <title>Fruit</title>
        <style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: left;}</style>
        </head>
        <body>
        <h1>Fruits type</h1>
        <table>
        <tr><th>name</th> <th>quantity</th> <th>price</th> <th>type</th></tr>
        """
        for fruit in fruits:
            html += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
        html += """
        </table>
        </body>
        </html>
        """

    else:
        html = """<html>
        <head><title>ERROR</title></head>
        <body><h1> ERROR </h1></body>
        </html>
        """
    return html

# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    fruits = db.get_by_name(name)
    if fruits :
        html = """
        <html>
        <head>
        <title>Fruit</title>
        <style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: left;}</style>
        </head>
        <body>
        <h1>Fruits name</h1>
        <table>
        <tr><th>name</th> <th>quantity</th> <th>price</th> <th>type</th></tr>
        """
        for fruit in fruits:
            html += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
        html += """</table>
        </body>
        </html>
        """

    else:
        html = """<html>
        <head><title>ERROR</title></head>
        <body><h1> ERROR </h1></body>
        </html>
        """
    return html


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    fruits = db.get_by_price(price)
    if fruits :
        html = """
        <html>
        <head>
        <title>Fruit</title>
        <style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: left;}</style>
        </head>
        <body>
        <h1>Fruits price</h1>
        <table>
        <tr><th>name</th> <th>quantity</th> <th>price</th> <th>type</th></tr>
        """
        for fruit in fruits:
            html += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
        html += """</table>
        </body>
        </html>
        """

    else:
        html = """<html>
        <head><title>ERROR</title></head>
        <body><h1> ERROR </h1></body>
        </html>
        """
    return html



if __name__ == '__main__':
    app.run(debug=True)