import json

class StateLawSchema:
    def __init__(self, state, laws):
        self.state = state
        self.laws = laws

def load_state_laws():
    with open('website/data/state_laws.json') as f:
        data = json.load(f)
        state_laws = {}
        for item in data:
            state_laws[item['state']] = StateLawSchema(item['state'], item['laws'])
        return state_laws

def getLaws(state):
    stateLaws = load_state_laws()
    if state in stateLaws:
        return stateLaws[state]
    else:
        return None