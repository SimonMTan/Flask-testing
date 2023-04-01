from flask import Flask, request,jsonify

app = Flask(__name__)

data = [{'name': 'alice',
        'email': 'alice@outlook.com'}]

@app.route('/')
def hello_world():
    return jsonify(data)

@app.route('/',methods=['PUT'])
def create_world():
    newworld = json.loads(request.data)
    data.append(newworld)
    return jsonify(data)

@app.route('/',methods=['POST'])
def update_page():
    updateworld = json.loads(request.data)
    for each in data:
        if each['name'] === updateworld['name']
            each['email'] = updateworld['email']
        else:
            continue
    return jsonify(data)

@app.route('/',methods=['Delete'])
def delete_page():
    deleteworld = json.loads(request.data)
    newdata = []
    for idx in range(len(data)):
        each = data[idx]
        if each['name'] != deleteworld['name']:
            newdata.append(each)
        else:
            continue
    data = newdata
    return jsonify(data)
