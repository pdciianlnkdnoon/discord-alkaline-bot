from .alkalineplugin import AlkalinePlugin
import discord, random, asyncio, re

class gaydar(AlkalinePlugin):

	def __init__(self, client):
		self.client = client

		self.name = 'gaydar'
		self.version = '69'
		self.author = 'Connor McLinden'

	async def on_command(self, message: discord.Message, command : str, args : str):
		if command.lower() == 'gaydar':
			subject = args.split(' ')[0]
			if '&' in subject:
				return

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
			

			
			if str(subject.id) == '182411730435964928' :
				await message.channel.send('<@' + str(subject.id) + '> is not gay.')
			
			elif str(subject.id) == '181227668241383425' :
				await message.channel.send('<@' + str(subject.id) + '> is so gay they stuck a 20 up there, but they got a thank you note back.')
			else :
				# determine gayness
				gayness = random.randint(1,100)
				
				if 0<=gayness<25:
					await message.channel.send('<@' + str(subject.id) + '> is not gay.')
				elif 25<=gayness<45:
					await message.channel.send('<@' + str(subject.id) + '> is a little bit curious.')
				elif 45<=gayness<65:
					await message.channel.send('<@' + str(subject.id) + '> bats for both teams.')
				elif 65<=gayness<75:
					await message.channel.send('<@' + str(subject.id) + '> can\'t deny their vile obsession.')
				elif 75<=gayness<85:
					await message.channel.send('<@' + str(subject.id) + '> can\'t hold back their intense desire.')
				elif 85<=gayness<99:
					await message.channel.send('<@' + str(subject.id) + '> is so gay, they can\'t pray the gay away.')
				elif 99<=gayness<100:
					await message.channel.send('<@' + str(subject.id) + '> is gayer than your paster from spirit camp.')
	
	
		
plugins = [gaydar]
commands = {
	'gaydar': {
		'usage':'[me|@user] is [%gay]',
		'example': 'User is very gay.'
	}
}
