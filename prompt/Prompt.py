from dotenv import load_dotenv
import os
import openai

class Prompt:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        self.MIN_THREAT = 0
        self.MAX_THREAT = 10

    def grade(self, text: str = None):

        assert text is not None

        prompt = f"""
        
        Pretend you are a person seeking non-violence on the internet.
        You can just output a single number, and nothing else!
        On a range of {self.MIN_THREAT} to {self.MAX_THREAT},
        {self.MIN_THREAT} for completely safe and {self.MAX_THREAT} for violent threat
        Grade the safety level of this paragraph:
        \"{text}\"
        
        """

        chat_completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": prompt
            }])
        
        response = chat_completion.choices[0].message.content
        return response

if __name__ == '__main__':
    
    text = "He is a person who is willing to give everything to his cause, even if its means \
        sacrifying the ones he loves the most. 10 years ago, he killed his brother"
    
    prompt = Prompt()

    print(prompt.grade(text))
