import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

#== Create our Assistant ==
personal_trainer = client.beta.assistants.create(
    name = "Personal Trainer",
    instructions = """You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles.

You've trained high-caliber athletes and movie stars.""",
    model = model
)
personal_trainer_id = personal_trainer.id
print(personal_trainer_id)

#== Thread ==
thread = client.beta.threads.create(
    messages = [
        {
            "role": "user",
            "content": "I want to build lean muscles. Can you help me?"
        }
    ]
)
thread_id = thread.id
print(thread_id)