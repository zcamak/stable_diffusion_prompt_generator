import argparse

def parse_input():
    parser = argparse.ArgumentParser(description='Stable Diffusion prompt generator helper.')

    parser.add_argument('-p', '--prompt', type=str, help='User provided prompt')
    parser.add_argument('-f', '--file', type=str, help='File used as base for prompt generation')
    parser.add_argument('-k', '--key', type=str, help='OpenAI API key for GPT')

    args = parser.parse_args()

    args.file = "prompt_scheme.json" if args.file == None else args.file

    return  args.file, args.prompt, args.key
