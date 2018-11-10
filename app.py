from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from Chart import Chart

# Define a bunch of astronova API pseudofunctions for pure testing, 
# and to inform later updating of existing program

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/query', methods=['POST'])
@cross_origin(origin='*')
def query():
    data = request.get_json(force=True)
    if data == None:
        print("Didn't receive data.")
        return jsonify("No data!")
    else:
        location = data['inputLocation']
        location = location.strip()
        location = location.lower()

        birthDate = data['inputDate']
        birthDate = birthDate.strip()
        splitBirthDate = birthDate.split('/')
        month, day, year = (int(x) for x in splitBirthDate)
        
        birthTime = data['inputTime']
        splitBirthTime = birthTime.split(':')
        hour, minute = (int(x) for x in splitBirthTime)

        return jsonify([month, day, year, hour, minute, location])