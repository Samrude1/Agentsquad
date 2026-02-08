#!/usr/bin/env python
import sys
import warnings
from market_scout.crew import MarketScoutCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    print("## Welcome to Market Scout AI ##")
    topic = input("Enter the company or topic you want to research: ")
    
    inputs = {
        'topic': topic
    }

    result = MarketScoutCrew().crew().kickoff(inputs=inputs)
    print("\n\n########################")
    print("## Briefing Generated ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run()
