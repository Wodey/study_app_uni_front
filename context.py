import pickle


class Context:
    def __init__(self):
        self.state = {
            "username": None,
            "uid": None,
            "score": 0,
            "current_task": None
        }
        with open("state.pickle", "wb") as state_file:
            pickle.dump(self.state, state_file)

    def update_state(self, newState):
        self.state |= newState
        with open("state.pickle", "wb") as state_file:
            pickle.dump(self.state, state_file)

    def get_state(self):
        with open("state.pickle", "rb") as state_file:
            self.state = pickle.load(state_file)
        print(f"context is {self.state}")
        return self.state


context = Context()
print(context.get_state()['username'])