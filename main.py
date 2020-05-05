import discord, random, json
from wit import Wit

with open("responses.json") as json_file:
	responses = json.load(json_file)

#DECLARE VARIABLES
BOT_CHANNEL_ID = 0 #channel id here, it's an int btw
WIT_TOKEN = 'Z2HRFYADTY3OPUFWTKWZ2C6UJFVES4H7' #You can replace this token, but by doing that my bot won't be able to learn
DISCORD_TOKEN = 'discord token here'

#CREATE BOT INSTANCES
bot = discord.Client()
client = Wit(WIT_TOKEN)

#THIS WILL ONLY WORK ON PYTHON 3.6+, sorry
def get_bot_response(response):
	error_message = "I yet don't know how to respond, but by sending messages you help me learn! Thanks for contributing!"
	global responses

	try:
		entity_response = next(iter(response['entities']))
		if responses[str(entity_response)]:
			return random.choice(responses[entity_response])
	except:
		return error_message

	return error_message

@bot.event
async def on_ready():
	print("Ready")

@bot.event
async def on_message(message):
	if message.author != bot.user and message.channel.id == BOT_CHANNEL_ID:
		resp = client.message(message.content)
		await message.channel.send(get_bot_response(resp))

bot.run(DISCORD_TOKEN)
