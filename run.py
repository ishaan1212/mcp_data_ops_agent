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

# This file contains the workflow. If someone wants to share the file, how to secure the file, first serialize the file, picklize it. When you picklize it then no one can crack that because contains the security protocol.
# When dimpi runs it she has to follow the protocols of your pipeline. .YAML format is used to serialize it (Yet Another Markup Language)