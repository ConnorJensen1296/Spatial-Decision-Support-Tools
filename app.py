from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

class DataStore():
    place_id = None

data = DataStore()


@app.route("/",)
def home():
    return render_template("home.html")

@app.route('/origin_data', methods = ['POST', 'GET'])
def get_origin():
    # Getting the user inputted origin
    data.place_id = request.args.get('origin')
    return render_template("tmp.html")

@app.route("/destination", methods=['POST', 'GET'])
def destination():
    centroid = pd.read_csv('data\centroids.csv')
    # Applying the Distance API call to every centroid
    def calc_dist(lat,lng):
        base_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=place_id:{}&destinations={},{}&key=AIzaSyCzH9RgLeGoCU8uGYf90-fLlG9LZX8X_Bg"
        url = base_url.format(data.place_id, lat, lng)
        r = requests.get(url)
        json = r.json()
        return json['rows'][0]['elements'][0]['duration']['value']

    centroid['distance'] = centroid.apply(lambda row: calc_dist(row['Latitude'], row['Longitude']), axis=1)
    centroid = centroid.sort_values(by='distance', ascending=True)
    return jsonify(lng=centroid['Longitude'].iloc[0],
                  lat=centroid['Latitude'].iloc[0])

if __name__ == '__main__':
    app.run(debug=True, port=5000 )
