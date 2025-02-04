import questionary as qy
from backend.src.core.agents.chat.chat_agent import Agent

def main():
    print("Welcome to Automated Bureaucracy via Command Line")
    print("")
    choice = qy.select( "What do you want to do",
              choices=[
                  "Chat","Simulate","Exit"
                  ]
    ).ask()

    if choice == "Chat":
        agent = Agent()
        agent.create_agent()
        print("")
        message = qy.text("what is your prompt or Exit to leave").ask()
        config = {"configurable": {"thread_id": "abc123"}}
        while message.lower() != "exit":
            response = agent.invoke_agent(message,config)
            print(response)
            message =qy.text("what is your prompt or Exit to leave").ask()
        print("")
    elif choice == "Simulate":
        print("simulaate temp")
    
    else:
        exit()

if __name__ == "__main__":
    main()
