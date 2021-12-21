import pickle


class Context:
    def __init__(self):
        self.state = {}
        with open("state.pickle", "wb") as state_file:
            pickle.dump(self.state, state_file)

    def update_state(self, newState):
        self.state |= newState
        with open("state.pickle", "wb") as state_file:
            pickle.dump(self.state, state_file)

    def get_state(self):
        with open("state.pickle", "rb") as state_file:
            self.state = pickle.load(state_file)
        return self.state


context = Context()
