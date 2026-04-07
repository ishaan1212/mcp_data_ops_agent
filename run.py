from src.mcp_agent.agent import MCPAgent
import sys


def main():
    agent = MCPAgent()

    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input("Enter your request: ")

    response = agent.handle_request(user_input)

    print("\nResponse:")
    print(response)


if __name__ == "__main__":
    main()