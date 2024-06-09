from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

app = Flask (__name__)

CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

@app.route('/add', methods =['GET'])
@cross_origin(origins='*')
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothunhai'))
    sum = a+b
    return 'add function ' + str(sum)

if __name__ == '__main__':
    app.run(host= '127.0.0.1', port= '6868')