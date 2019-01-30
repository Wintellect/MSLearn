import csv

def split_strip(value, split_value = ','):
    return tuple([ x.strip() for x in value.split(split_value) ])

class State:

    def __init__(self, state_data):

        state_abbr, state_name_data = state_data
        country =  'United States'

        state_name_parts = split_strip(state_name_data)
        state_name = state_name_parts[0]

        if (len(state_name_parts) == 2):
            country = state_name_parts[1]
            state_label = 'province'
        else:
            state_label = 'state'

        self.code = state_abbr
        self.name = state_name
        self.label = state_label
        self.country = country

def load_states(states_csv_file_name):

    states = {}

    with open(states_csv_file_name, 'r') as states_csv_file:
        states_csv_file_reader = csv.reader(states_csv_file, delimiter=',')
        for state_line_number, state_data in enumerate(states_csv_file_reader):
            if state_line_number == 0: continue
            state = State(state_data)
            states[state.code] = state

    return states

class Airport:

    def __init__(self, airport, states):

        code = airport[0]
        name = ''
        city = ''
        state_label = ''
        state_name = ''
        country = ''

        desc_parts = split_strip(airport[1], ':')

        if len(desc_parts) == 2:

            location, name = desc_parts
            location_parts = split_strip(location)

            if len(location_parts) == 2:
                city = location_parts[0]
                state_code = location_parts[1]

                if state_code in states:
                    state = states[state_code]
                    state_name = state.name
                    state_label = state.label
                    country = state.country
                else:
                    country = state_code

        else:
            name = desc_parts[0]

        self.code = code
        self.name = name
        self.city = city
        self.state_name = state_name
        self.state_label = state_label
        self.country = country

def load_airports(airport_csv_file_name, states):

    airports = {}

    with open(airport_csv_file_name, 'r') as airports_csv_file:
        airports_csv_file_reader = csv.reader(airports_csv_file, delimiter=',')
        for airport_line_number, airport_data in enumerate(airports_csv_file_reader):
            if airport_line_number == 0: continue
            airport = Airport(airport_data, states)
            airports[airport.code] = airport
      
    return airports