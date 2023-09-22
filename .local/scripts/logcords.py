#!/usr/bin/python3
import os
import json
import time
import requests

def are_coordinates_equal(coord1, coord2):
    return coord1["x"] == coord2["x"] and coord1["y"] == coord2["y"] and coord1["z"] == coord2["z"] and coord1["world"] == coord2["world"]

while True:
    try:
        url = "https://hollyspace.net/up/world/world/{}".format(int(time.time() * 1000))
        response = requests.get(url)
        player_data = response.json().get("players", [])
        
        online_players = len(player_data)
        print("Online players:", online_players)
        
        output_dir = "/opt/hollyspace/"
        os.makedirs(output_dir, exist_ok=True)
        
        for player in player_data:
            player_name = player["name"]
            player_json = os.path.join(output_dir, f"{player_name}.json")
            
            if os.path.exists(player_json):
                with open(player_json, "r") as f:
                    existing_data = json.load(f)
                
                if "coordinates" in existing_data:
                    coordinates = existing_data["coordinates"]
                else:
                    coordinates = []
                    
                new_coordinates = {
                    "timestamp": int(time.time()),
                    "x": player["x"],
                    "y": player["y"],
                    "z": player["z"],
                    "world": player["world"]
                }
                
                if not coordinates or not are_coordinates_equal(coordinates[-1], new_coordinates):
                    coordinates.append(new_coordinates)
                    existing_data["coordinates"] = coordinates
            else:
                existing_data = {
                    "coordinates": [{
                        "timestamp": int(time.time()),
                        "x": player["x"],
                        "y": player["y"],
                        "z": player["z"],
                        "world": player["world"]
                    }]
                }
            
            with open(player_json, "w") as f:
                json.dump(existing_data, f, indent=4)
            
        
        time.sleep(10)
        
    except Exception as e:
        print("An error occurred:", e)
        time.sleep(60)
