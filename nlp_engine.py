from chatbot.metro_logic import get_fare, get_timing, get_all_stations

def process_query(query):
    query = query.lower()
    stations = [s.lower() for s in get_all_stations()]
    found = [s.capitalize() for s in stations if s in query]

    if "fare" in query:
        if len(found) == 2:
            fare = get_fare(found[0], found[1])
            return f"The fare from {found[0]} to {found[1]} is ₹{fare}" if fare else "Fare not found."
        else:
            return "Please specify both start and end stations to know the fare."

    elif "time" in query or "timing" in query:
        if len(found) == 2:
            timing = get_timing(found[0], found[1])
            return f"Metro from {found[0]} to {found[1]} runs {timing}." if timing else "Timing not found."
        else:
            return "Please provide both stations to check timing."

    elif "route" in query or "how to go" in query:
        if len(found) == 2:
            return f"You can take a direct metro from {found[0]} to {found[1]}."
        else:
            return "Please provide start and end stations to check the route."

    else:
        return "I can help you with metro fare, timings, and routes. Try asking like 'fare from Central to Guindy'."
