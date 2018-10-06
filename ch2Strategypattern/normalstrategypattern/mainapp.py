from ch2Strategypattern.normalstrategypattern.context import *
from ch2Strategypattern.normalstrategypattern.stratege import *

if __name__=="__main__":
    context=None
    context=Context(ConreteStrategyA())
    context.ContextInterface()
    context=Context(ConreteStrategyB())
    context.ContextInterface()
    context=Context(ConreteStrategyC())
    context.ContextInterface()