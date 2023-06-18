from dotenv import load_dotenv
import os
import openai
import json

MIN_THREAT = 0
MAX_THREAT = 10

if __name__ == '__main__':

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # content = []

    with open('data.txt', mode='a') as file:
        while True:
            try:
                next_input = input("Enter text: ")
                
                prompt = f"""

                Pretend you are person seeking non-violence on the internet.
                You can just output a single number, and nothing else!
                On a range of {MIN_THREAT} to {MAX_THREAT},
                {MIN_THREAT} for completely safe and {MAX_THREAT} for violent threat
                Grade the safety level of this paragraph:
                \"{next_input}\"

                """

                chat_completion = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }])
                
                response = chat_completion.choices[0].message.content
                print(f'\nGPT-4 rating: {response}\n')

                file.write(f'{next_input} \n\t rating {response} \n')
                
                # content.append({'user': next_input})
                # content.append({'assistant': response})
            except KeyboardInterrupt:
                break

        file.close()
    # print(content)