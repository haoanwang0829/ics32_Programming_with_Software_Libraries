import mapquest
import mapquest_class

class MapquestError(Exception):
    pass

#this function is to run the user interface.
def run_user_interface() -> None:
    try:
        location_lst = get_location()
        output_lst = get_output()
        url = mapquest.build_search_url(location_lst)
        json_result = mapquest.get_direction_result(url)
        if json_result["info"]["statuscode"] == 0:
            output = {
                'LATLONG': mapquest_class.latlong(json_result), 
                'STEPS': mapquest_class.steps(json_result), 
                'TOTALTIME': mapquest_class.totaltime(json_result), 
                'TOTALDISTANCE': mapquest_class.totaldistance(json_result), 
                'ELEVATION': mapquest_class.elevation(json_result)
            }
            print('')
            for method in output_lst:
                output[method].print_data()
            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

        else:
            print('')
            print('NO ROUTE FOUND')
    except:
        print('')
        print('MAPQUEST ERROR')
    

    
#this function is to get the input of location number and get locations
def get_location() -> list:
    number_of_locations = input()
    location_lst = []
    try:
        if int(number_of_locations) > 1:
            for number in range(int(number_of_locations)):
                location = input()
                location_lst.append(location)
            return location_lst
        else:
            raise MapquestError
    except:
        raise MapquestError

#this function is to get the input of the number of ouputs and the info of outputs
def get_output() -> list:
    number_of_outputs = input()
    output_lst = []
    try:
        if int(number_of_outputs) > 0:
            for number in range(int(number_of_outputs)):
                output = input()
                output_lst.append(output)
            return output_lst
        else:
            raise MapquestError
    except:
        raise MapquestError



if __name__ == '__main__':
    run_user_interface()

