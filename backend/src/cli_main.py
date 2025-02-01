import questionary as qy
from core.agents.agent import Agent

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
        agent.init_app()
        print("")
        message = qy.text("what is your prompt or Exit to leave").ask()
        config = {"configurable": {"thread_id": "abc123"}}
        while message.lower() != "exit":
            response = agent.invoke_app(message,config)
            print(response["messages"][-1].content)
            message =qy.text("what is your prompt or Exit to leave").ask()
        print("")
    
    else:
        exit()
    

if __name__ == "__main__":
    main()
