import discord, random
from wit import Wit

#POSSIBLE RESPONSES, im planning on linking it to a database of responses but i'm too lazy to do that
#Notes: you can obviously modify them to your will
greets = ['Hi!', 'Yo!', 'Howdyyy ho!', 'Hello there!', 'Good to see you again', 'Holas amigos!', 'R.I.P Rick May']
byes = ['Bye!', 'See ya :(', 'Cya!']

#DECLARE VARIABLES
BOT_CHANNEL_ID = 0 #channel id here, it's an int btw
WIT_TOKEN = 'Z2HRFYADTY3OPUFWTKWZ2C6UJFVES4H7' #You can replace this token, but by doing that my bot won't be able to learn
DISCORD_TOKEN = 'DISCORD BOT TOKEN HERE'

#CREATE BOT INSTANCES
bot = discord.Client()
client = Wit(WIT_TOKEN)

#THIS WILL ONLY WORK ON PYTHON 3.6+, sorry
def get_bot_response(response):
	try:
		entity_response = next(iter(response['entities']))
	except StopIteration:
		return "I yet don't know how to respond, but by sending messages you help me learn! Thanks for contributing!"

	if entity_response == "greetings":
		return random.choice(greets)
	if entity_response == "bye":
		return random.choice(byes)

@bot.event
async def on_ready():
	print("Ready")

@bot.event
async def on_message(message):
	if message.author != bot.user and message.channel.id == BOT_CHANNEL_ID:
		resp = client.message(message.content)
		await message.channel.send(get_bot_response(resp))

bot.run(DISCORD_TOKEN)
