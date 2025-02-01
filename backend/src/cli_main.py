import questionary as qy
from core.agents.api_agent import api_Agent





def main():
    print("Welcome to Automated Bureaucracy via Command Line")
    print("")
    choice = qy.select( "What do you want to do",
              choices=[
                  "Chat","Exit"
                  ]
    ).ask()
    
    if choice == "Chat":
        agent = Agent()
        agent.create_agent()
        print("")
        message = ""
        while message != "Exit":
            message = qy.text("what is your prompt or exit to leave").ask()
            response = agent.chat(message)
            print(response.content)
        print("")
    
    else:
        exit()
    

if __name__ == "__main__":
    main()
    print("hello")
