# FA State Class


class State:
    def __init__(self, accepting=False):
        self.accepting = accepting
        self.transitionMap = {}

    def addTransitionForSymbol(self, symbol, state):
        # Implementation goes here
        return None

    def getTransitionsForSymbol(self, symbol):
        # Implementation goes here
        return None


s1 = State(False)
s2 = State(True)
