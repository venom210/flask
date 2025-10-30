from flask import Flask, request
from ex.my_csv_parse import filter_data_by_gender
import json

app = Flask(_name_)

#find by route that the parameter is insert by an user
@app.route("/")
def show():
    gender = request.args.get('genre')

    if gender :
        result = filter_data_by_gender(gender)

    return json.dumps(result)

#find with route that have parameter
@app.route("/<gender>")
def show_gender(gender):

    if gender :
        result = filter_data_by_gender(gender)

    return json.dumps(result)
    




app.run(debug=True, host='0.0.0.0', port=8080)