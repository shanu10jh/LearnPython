from dotenv import load_dotenv
import os
load_dotenv()
model = os.getenv("MODEL")

print(model)