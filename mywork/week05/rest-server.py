# flask server that links to a DAO


from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

@app.route('/books', methods=['GET'])
def get_all():
    return "get all"

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

@app.route('/books', methods=['POST'])
def create():
    jsonstring = request.json

    return f"create {id} {jsonstring}"


@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    jsonstring = request.json
    return f"delete {id} {jsonstring}"




if __name__ == "__main__":
    app.run(debug = True)