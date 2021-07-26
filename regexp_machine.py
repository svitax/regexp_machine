from collections import defaultdict


# FA State Class
class State:
    def __init__(self, accepting=False):
        self.accepting = accepting
        self.transitionMap = defaultdict(list)

    def addTransitionForSymbol(self, symbol, state):
        self.transitionMap[symbol] += [state]

    def getTransitionsForSymbol(self, symbol):
        return {symbol: self.transitionMap[symbol]}

    def test(self, string):
        # Need to implement
        string = string
        return None


s1 = State(False)
s2 = State(True)
s3 = State(False)

s1.addTransitionForSymbol("a", s2)
s1.addTransitionForSymbol("a", s3)
print(s1.getTransitionsForSymbol("a"))  # {a: [s2, s3]}


# NFA State Class
class NFA:
    def __init__(self, inState, outState):
        self.inState = inState
        self.outState = outState

    # Tests whether this NFA matches the string.
    # Delegates to the input state
    def test(self, string):
        return self.inState.test(string)


# Factory function for a single character machinne
def char(symbol):
    inState = State()
    outState = State()

    outState.accepting = True
    inState.addTransitionForSymbol(symbol, outState)

    return NFA(inState, outState)


a = char("a")
# a.test('a') # True
# a.test('b') # False

# The "empty" string
EPSILON = "ε"


# Factory functionn for an epsilon machine
def epsilon():
    return char(EPSILON)


e = epsilon()
# e.test('') # true
# e.test('a') # false
