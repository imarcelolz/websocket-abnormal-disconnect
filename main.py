import argparse
from websocket import create_connection

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect to an endpoint")
    parser.add_argument("endpoint", help="The endpoint to connect to")

    args = parser.parse_args()

    print(f"Connecting to {args.endpoint}!")

    create_connection(args.endpoint)