import pickle
import os
from dotenv import load_dotenv

class Context:
    def __init__(self):
        self.state = {
            "username": None,
            "uid": None,
            "score": 0,
            "current_task": None,
            "tid": None
        }
        self.subscribers = []

        with open("state.pickle", "wb") as state_file:
            pickle.dump(self.state, state_file)

    def update_state(self, newState):
        self.state |= newState
        with open("state.pickle", "wb") as state_file:
            pickle.dump(self.state, state_file)
        self.notify()

    def get_state(self):
        with open("state.pickle", "rb") as state_file:
            self.state = pickle.load(state_file)
        return self.state

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self):
        for i in self.subscribers:
            i.rerender()

context = Context()