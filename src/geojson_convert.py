import json
import sys
import os


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python geojson_convert.py <input_file_name>")
        sys.exit(1)

input_file_name = input_file_name = sys.argv[1]

try:
    f = open(input_file_name)

    # returns JSON object as a dictionary
    data = json.load(f)

    contains = data['contains']
    # Filter out objects with type equal to "spot" and rename attributes
    filtered_spots = []
    for obj in contains:
        if obj.get('type') == 'spot':
            # Select and rename attributes
            new_obj = {
      		    "type": "Feature",
      		    "geometry": {
      		      "type": "Point",
      		      "coordinates": obj.get('location').get('coordinates')
      		    },
      		    "properties": {
      		      "title": obj.get('name')
      		    }
            }
            filtered_spots.append(new_obj)
        
    geojson = {
    	"type": "FeatureCollection",
    	"features": filtered_spots
    }
    f.close()

    output_file = os.path.splitext(input_file_name)[0] + ".geojson"
    with open(output_file, 'w') as file:
        json.dump(geojson, file, indent=4)
except FileNotFoundError:
    print("File not found. Enter filename to convert as argument.")
