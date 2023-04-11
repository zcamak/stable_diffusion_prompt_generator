import argparse

def parse_input():
    prompt = ""
    file   = "prompt_scheme.json"

    parser = argparse.ArgumentParser(description='Stable Diffusion prompt generator helper.')

    parser.add_argument('-p', '--prompt', type=str, help='User provided prompt')
    parser.add_argument('-f', '--file', type=str, help='File used as base for prompt generation')
    parser.add_argument('-a', '--api', type=str, help='OpenAI API key for GPT')

    args = parser.parse_args()

    return args.prompt, args.file, args.api
