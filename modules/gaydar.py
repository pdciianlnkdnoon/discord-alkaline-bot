from .alkalineplugin import AlkalinePlugin
import discord, random, asyncio, re

class gaydar(AlkalinePlugin):

	def __init__(self, client):
		self.client = client

		self.name = 'GayDAR'
		self.version = '69'
		self.author = 'Connor McLinden'

	async def on_command(self, message: discord.Message, command : str, args : str):
		if command == 'GayDAR'.lower():
			subject = args.split(' ')[0]
			

			# determine subject:
			if subject.lower() == 'me':
				subject = message.author
			else:
				mat = re.match('<@.[0-9]+>', subject)

				if mat:
					subject = discord.utils.get(message.guild.members, id=int(subject[2:-1].replace('!','')))
				else:
					subject = discord.utils.find(lambda m: subject.lower() in m.name.lower() or subject.lower() in m.display_name.lower(), message.guild.members)

			if type(subject) == str:
				await message.channel.send('I don\'t know who that is...')
				return
			
	gayness = random.randint(1,100)
	if 0<=gayness<25:
		message.channel.send(subject + ' is not gay.')
	elif 25<=gayness<45:
		message.channel.send(subject + ' is a little bit curious.')
	elif 45<=gayness<65:
		message.channel.send(subject + ' bats for both teams.')
	elif 65<=gayness<75:
		message.channel.send(subject + ' can\'t deny their interests.')
	elif 75<=gayness<85:
		message.channel.send(subject + ' can\t hold back their intense desire.')
	elif 85<=gayness<99:
		message.channel.send(subject + ' is so gay, they can\'t pray the gay away.')
	else 99<=gayness<100:
		message.channel.send(subject + ' is gayer than your paster from spirit camp.')
	
	
		
plugins = [gaydar]
commands = {
	'GayDAR': {
		'usage':'[me|@user] is [%gay]',
		'example': 'User is very gay.'
	}
}

