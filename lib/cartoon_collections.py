cheeses = ["cheddar", "gouda", "camebert"]

def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f'{i}. {dwarf}')
        i += 1

def summon_captain_planet(planeteer_calls):
    return [f'{planeteer_call.title()}!' for planeteer_call in planeteer_calls]

def long_planeteer_calls(calls_list):
    for call in calls_list:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods_list):
    for food in foods_list:
        if food in cheeses:
            return food
    return None
