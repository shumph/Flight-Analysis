'''

Samuel Humphrey

sjh2014@rogers.com

This code creates a series of functions that analyze a csv file containing flight data, and outputs the result of this analysis

'''


def parse_flight_data(data_file_name): #a function that sorts a csv file into a "dictionary within a dictionary"

    flight_information ={}

    try :

        data_file = open(data_file_name, 'r')

        data_file.readline()

        for line in data_file:

            current_list = []

            line = line.lower()

            line = line.strip()

            if line  != '':

                data_dict = {} #this willbe our 'dictionary within a dictionary'

                current_list = line.split(',')           

                for i in range(1, len(current_list)): #since our .csv is formatted we know which piece of data will be at which index of i, so I can set my values accordingly, I skip index 0 as this is our flight number

                    if i == 1:

                        data_dict['DepartureAirport'] = current_list[i]

                    elif  i == 2:

                        data_dict['ArrivalAirport'] = current_list[i]

                    elif i == 3:

                        data_dict['DepartureTime'] = current_list[i]

                    elif i == 4:

                        data_dict['ArrivalTime'] = current_list[i]

                    elif i == 5:

                        data_dict['Airline'] = current_list[i]

                    elif i == 6:                                               #this elif gate must split the time value into hours and minutes, and convert to minutes

                        flight_duration_split = current_list[i].split(':')     # the list produced by this method is of form ('HH', 'MM', 'SS')

                        flightMinutes = 0

                        for i in range(len(flight_duration_split)):

                            if i == 0:

                                flightMinutes += int(flight_duration_split[i]) * 60 

                            elif i == 1:

                                flightMinutes += int(flight_duration_split[i])   

                        data_dict['FlightDuration'] = flightMinutes

                    elif i == 7:

                        data_dict['AvgTicketPrice'] = int(current_list[i])

                    elif i == 8:

                        data_dict['Aircraft'] = current_list[i]

                    elif i == 9:

                        data_dict['PassengerCount'] = int(current_list[i])

                        

                flight_information[current_list[0]] = data_dict

        return flight_information

    except IOError: #here to catch file errors

        return(-1)



def calculate_average_ticket_price(all_flights, airline): #a function that finds the avg tix price for an airline

    try: 

        price_sum = 0            

        num_additions = 0

        for key in all_flights: #loops over all flight numbers

            current_dict = all_flights[key]  

            if current_dict['Airline'] == airline.lower(): #checks to see if the airline for this flight number is the same as our parameter airline if so add our avg price and increase our total number of flights for this airline by 1

                price_sum += current_dict['AvgTicketPrice'] 

                num_additions += 1

        if num_additions == 0: #catches error where we have no flights

            return 0

        average_price = price_sum / num_additions #averages our average

        return average_price

    except: #catches all other errors

        return -1


def get_total_passengers_by_airline(all_flights): #a function that returns the total number of passengers an airline has processed

    try: 

        total_passengers_by_airline = {}            

        for key in all_flights:

            current_dict = all_flights[key]

            if current_dict['Airline'] not in total_passengers_by_airline:          

                total_passengers_by_airline[current_dict['Airline']] = current_dict['PassengerCount']

            else:

                total_passengers_by_airline[current_dict['Airline']] += current_dict['PassengerCount']

        return total_passengers_by_airline

    except:

        return {}



def get_overnight_flights(all_flights): #returns a list of all overnight flights

    overnight_flights = []

    def get_day(time_info):   #creates a function that extracts the day from our ArrivalTime/DepartureTime

        split_one = time_info.split(' ')         #makes a list that looks like ('YYYY-MM-DD', 'HH:MM:SS')

        split_two = split_one[0].split('-')      #makes a list that looks like ('YYYY', 'MM', 'DD') (note:our day is at the second index of our list)

        day = int(split_two[2])

        return day

    for key in all_flights:

        current_dict = all_flights[key]

        depart_day = get_day(current_dict['DepartureTime'])  #turns our departure time and arrival time into a day (DD)

        arrival_day = get_day(current_dict['ArrivalTime'])

        if depart_day != arrival_day:                       #if the values arent equal, it is definitionally an overnight flight, so add our flight number to our list

            overnight_flights.append(key)

    return overnight_flights


def get_top_n_aircraft(all_flights, n=3): #a function that sorts the number 

    aircraft_count = {}

    def sort_sum_dict(sum_dict): #a function to sort our dictionairy

        index = 1

        return sorted(sum_dict.items(), key=lambda x: x[index], reverse=True)

        

    for key in all_flights:                

        current_dict = all_flights[key]          

        if current_dict['Aircraft'] not in aircraft_count:            #if key is not found in our dictionairy, add it and set it svalue = 1

            aircraft_count[current_dict['Aircraft']] = 1

        else:                                                         #if it does already exist increment its value by one

            aircraft_count[current_dict['Aircraft']] += 1        

    if len(aircraft_count) < n:                               #checks to make sure the length of our dictionary is not less than n

        raise ValueError("Invalid n value!")                      

    

    sorted_list = sort_sum_dict(aircraft_count)         #applies our sorting function, creates a sorted list

    

    top_n_aircraft = []

    for i in range(n):                           #creates a list of the first n aircraft in our list

        current_element = sorted_list[i]           

        top_n_aircraft.append(current_element[0])

        

    return top_n_aircraft



def get_total_duration(all_flights, airports): #a ffunction that returns the total number of minutes flown into and out of an list of airports

    airline_durations = {}  

    for key in all_flights: #loop over all flight numbers

        current_dict = all_flights[key]  

        for k in airports:                    #loop over or parameter airports

            if current_dict['ArrivalAirport'] == k.lower():

                for j in airports:                 #loop over parameter airports again

                    if current_dict['DepartureAirport'] == j.lower():

                        if current_dict['Airline'] not in airline_durations:

                            airline_durations[current_dict['Airline']] = current_dict['FlightDuration']

                    

                        else:

                            airline_durations[current_dict['Airline']] += current_dict['FlightDuration']

        if current_dict['Airline'] not in airline_durations:                             #makesa a key and value for airlines not previously covered (when flight duration = 0)

                airline_durations[current_dict['Airline']] = 0

                

                

    return airline_durations



