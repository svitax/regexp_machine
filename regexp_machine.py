# FA State Class

from collections import defaultdict


class State:
    def __init__(self, accepting=False):
        self.accepting = accepting
        self.transitionMap = defaultdict(list)

    def addTransitionForSymbol(self, symbol, state):
        self.transitionMap[symbol] += [state]

    def getTransitionsForSymbol(self, symbol):
        return {symbol: self.transitionMap[symbol]}


s1 = State(False)
s2 = State(True)
s3 = State(False)

s1.addTransitionForSymbol('a', s2)
s1.addTransitionForSymbol('a', s3)
print(s1.getTransitionsForSymbol('a'))  # {a: [s2, s3]}
