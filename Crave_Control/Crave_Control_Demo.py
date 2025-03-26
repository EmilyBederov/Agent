from Agents.AgentImports import *
from TheLLMChain.LLMChainImports import *
from User.UserImports import *
from TheLLMChain.Run import Run
from Display import Display
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

class Crave_Control_Demo:

    def __init__(self):
        self.system_prompt = """
        Hi there! I'm CraveControl, your friendly meal-finding assistant.
    
        I'm here to help you discover the perfect meal that matches your ideal calorie needs and taste preferences.
        
        To get started, could you share a bit about yourself and your current cravings?
        
        Let me know details like your age, weight, height, workout habits, any dietary preferences or restrictions,
        and even what ingredients you have on hand. Your input will help me tailor the best, healthiest meal options just for you!
        """

        self.user_input = input(self.system_prompt)

        self.Run = Run()
        self.Display = Display()

        #### Start the Process ####
        self.process()

    def process(self):
        records = Run.run(self.user_input)
        self.Display.display_recipes_ranked(records)


def __main__():
    crave_agent = Crave_Control_Demo()


