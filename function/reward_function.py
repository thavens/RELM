from dotenv import load_dotenv
import os
import openai

class RewardFunction:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        self.MIN_GRADE = 0
        self.MAX_GRADE = 10

    def get_reward(self, question: str = None, answer_good: str = None, answer_bad: str = None):

        prompt = f"""

        Pretend you are a reward function seeking concise answers in language a six-year-old can understand.
        You are going to rate the following answer on a range of {self.MIN_GRADE} to {self.MAX_GRADE},
        {self.MIN_GRADE} for an unhelpful explanation that uses language a five-year-old CAN'T understand and {self.MAX_GRADE} for a concise, helpful response that uses simple langauge a five-year-old can understand.
        I will send you multiple questions and respones pair, and you respond with an integer rating for each answer, separating each response using a new line and "=====".
        
        Grade the helpfulness level of the following question/answer pair:
        Question: \"{question}\"
        Answer: \"{answer_good}\"

        =====

        Question: \"{question}\"
        Answer: \"{answer_bad}\"

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
    
    question = "Why is the sky blue?"
    
    goodAnswer = "The sky is blue because of the sunlight. When the sun shines its light, it spreads out and fills the sky. The light has different colors, like red, orange, yellow, green, blue, and violet. But the blue light is the one that gets scattered the most by the tiny things in the air. That's why we see the sky as blue!"

    badAnswer = "Ah, the fascinating question about the color of the sky! You see, the sky's hue is the result of a complex interplay of multiple factors, including the scattering of sunlight, the composition and density of Earth's atmosphere, the molecular properties of air molecules, and the phenomenon known as Rayleigh scattering. Furthermore, the wavelengths of light and their interactions with various atmospheric constituents contribute to the observed blue coloration. To fully comprehend the intricate mechanisms at play, one must delve into the realms of physics, optics, atmospheric science, and quantum mechanics. Suffice it to say, the sky's blueness is a marvelous amalgamation of scientific intricacies that continue to captivate researchers worldwide."

    prompt = RewardFunction()

    print(prompt.get_reward(question, goodAnswer, badAnswer))
