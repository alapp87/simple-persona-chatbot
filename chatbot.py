import argparse
import openai
from dotenv import dotenv_values


def main():
    config = dotenv_values(".env")
    openai.api_key = config["OPENAI_API_KEY"]

    parser = argparse.ArgumentParser(
        description="Simple command line chat bot using GPT-3.5"
    )
    parser.add_argument(
        "-p|--personality",
        type=str,
        dest="personality",
        help="A brief summary of the chatbot's personality",
        default="Friendly and helpful",
    )
    args = parser.parse_args()

    messages = []

    if args.personality:
        print(f"Assistant will have the given personality: {args.personality}")
        messages.append(
            {
                "role": "system",
                "content": f"You are a conversational chatbot. Your personality is: {args.personality}",
            }
        )

    while True:
        try:
            user_input = input(bold(blue("You: ")))

            messages.append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

            assistant_resp = response["choices"][0]["message"]
            text_to_user = assistant_resp["content"]

            print(bold(red("Assitant: ")) + text_to_user)

            messages.append(assistant_resp)
        except KeyboardInterrupt:
            print("Exiting...")
            break


def bold(text):
    s = "\033[1m"
    e = "\033[0m"
    return s + text + e


def blue(text):
    s = "\033[34m"
    e = "\033[0m"
    return s + text + e


def red(text):
    s = "\033[31m"
    e = "\033[0m"
    return s + text + e


if __name__ == "__main__":
    main()
