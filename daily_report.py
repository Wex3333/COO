import os

print("SMV BOT STARTED")

slack_token = os.getenv("SLACK_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")
channel = os.getenv("REPORT_CHANNEL")

print("Slack token exists:", bool(slack_token))
print("OpenAI key exists:", bool(openai_key))
print("Channel:", channel)
