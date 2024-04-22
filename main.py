from analysis import *
import pprint

def main():
    
    filename = r'C:\Users\Samuella\CS1026Projects\CS1026 Proj 3\Uflights.csv'  
    all_flights = parse_flight_data(filename)

    pp = pprint.PrettyPrinter(indent=2)
   



    
    airline_to_check = 'Delta Airlines'
    average_price = calculate_average_ticket_price(all_flights, airline_to_check)
    print(f"Average ticket price for {airline_to_check}: ${average_price:.2f}")

    airline_to_check = 'air canada'
    average_price = calculate_average_ticket_price(all_flights, airline_to_check)
    print(f"Average ticket price for {airline_to_check}: ${average_price:.2f}")

    airline_to_check = 'rOYAl jordanIAN'
    average_price = calculate_average_ticket_price(all_flights, airline_to_check)
    print(f"Average ticket price for {airline_to_check}: ${average_price:.2f}")





    passengers_by_airline = get_total_passengers_by_airline(all_flights)
    print('Total passengers per airline:\n')
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(passengers_by_airline)





    overnight_flights = get_overnight_flights(all_flights)
    print('The list of overnight flights:\n')
    print(overnight_flights)




    n=4
    top_n_aircraft = get_top_n_aircraft(all_flights,n)
    print(f'Top {n} aircrafts:')
    print(top_n_aircraft)    

    top_n_aircraft = get_top_n_aircraft(all_flights)
    print(f'\nTop 3 aircrafts:')
    print(top_n_aircraft)



    airports= ['JFK', 'LAX', 'SFO']
    total_durations=get_total_duration(all_flights, airports)
    print(f'Total duration for all airlines for flights between any of {airports}:')
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(total_durations)

    airports= ['YxU', 'YyZ', 'YUL','yow']
    total_durations=get_total_duration(all_flights, airports)
    print(f'\nTotal duration for all airlines for flights between any of {airports}:')
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(total_durations)
main()


