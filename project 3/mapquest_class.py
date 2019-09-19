import mapquest

#each class is for eachoutput
#each class contains get_data and print_data functions
#one is to get the data from dictionaries and the another one is to print it out.
class latlong:
    def __init__(self, json_result: dict) -> None:
        self.json_result = json_result

    def get_data(self) -> list:
        latlong_lst = []
        for location in self.json_result["route"]["locations"]:
            lat = location["latLng"]["lat"]
            lng = location["latLng"]["lng"]
            if lat < 0:
                lat_adjust = "%0.2f" % abs(lat) + 'S'
            else:
                lat_adjust = "%0.2f" % lat + 'N'
            if lng < 0:
                lng_adjust = "%0.2f" % abs(lng) + 'W'
            else:
                lng_adjust = "%0.2f" % lng + 'E'

            latlong_lst.append([lat_adjust + ' ' + lng_adjust])
        return latlong_lst

    def print_data(self) -> None:
        print("LATLONGS")
        for latlong in self.get_data():
            print(latlong[0])
        print('')

class steps:

    def __init__(self, json_result: dict) -> None:
        self.json_result = json_result

    def get_data(self) -> list:
        step_lst = []
        for leg in self.json_result["route"]["legs"]:
            for narrative in leg["maneuvers"]:
                step = narrative["narrative"]
                step_lst.append(step)
        return step_lst

    def print_data(self) -> None:
        print("DIRECTIONS")
        for step in self.get_data():
            print(step)
        print('')



class totaltime:

    def __init__(self, json_result: dict) -> None:
        self.json_result = json_result

    def get_data(self) -> int:
        time = self.json_result["route"]["time"]
        return time

    def print_data(self) -> None:
        print("TOTAL TIME: {} minutes".format(round(self.get_data()/60)))
        print('')


class totaldistance:
    
    def __init__(self, json_result: dict) -> None:
        self.json_result = json_result

    def get_data(self) -> int:
        distance = self.json_result["route"]["distance"]
        return distance

    def print_data(self) -> None:
        print("TOTAL DISTANCE: {} miles".format(round(self.get_data())))
        print('')

class elevation:
    
    def __init__(self, json_result: dict) -> None:
        self.json_result = json_result

    def get_data(self) -> list:
        latlong_lst = []
        elevation_lst = []
        for location in self.json_result["route"]["locations"]:
            latlong_lst.append((str(location["latLng"]["lat"]),str(location["latLng"]["lng"])))
        for latlong in latlong_lst:
            elevation_url = mapquest.build_elevation_url(latlong)
            json_elevation_result = mapquest.get_elevation_result(elevation_url)
            for elevation in json_elevation_result["elevationProfile"]:
                elevation_lst.append(round(elevation["height"]))
        return elevation_lst

    def print_data(self) -> None:
        print("ELEVATIONS")
        for elevation in self.get_data():
            print(elevation)
        print('')






