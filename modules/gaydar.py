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
				
			await message.channel.send('Please wait, I\'ll do a quick scan.')	
			await asyncio.sleep(0.5)
			await message.channel.send('`beep beep`')
			await asyncio.sleep(1)
			if str(subject.id) == '408521026239070218' :
				await message.channel.send('<@' + str(subject.id) + '> not sure maybe we could find out over coffee sometime? ( ͡° ͜ʖ ͡°)')
			
			else :
				# determine gayness
				gayness = random.randint(1,100)
				
				if 1<=gayness<35:
					await message.channel.send('<@' + str(subject.id) + '> is definitely not gay.')
				elif 35<=gayness<40:
					await message.channel.send('<@' + str(subject.id) + '> is a little bit curious.')
				elif 40<=gayness<45:
					await message.channel.send('<@' + str(subject.id) + '> is so gay they stuck a 20 up there, and got a thank you note back.')
				elif 45<=gayness<50:
					await message.channel.send('<@' + str(subject.id) + '> swings both ways due to their desperate loneliness.')
				elif 50<=gayness<55:
					await message.channel.send('<@' + str(subject.id) + '> is as straight as a sickle.')
				elif 55<=gayness<65:
					await message.channel.send('<@' + str(subject.id) + '> bats for both teams.')
				elif 65<=gayness<75:
					await message.channel.send('<@' + str(subject.id) + '> can\'t deny their vile obsession.')
				elif 75<=gayness<80:
					await message.channel.send('<@' + str(subject.id) + '> can\'t hold back their intense desire for the dick.')
				elif 80<=gayness<90:
					await message.channel.send('<@' + str(subject.id) + '> is so gay, they can\'t pray the gay away.')
				elif 90<=gayness<91:
					await message.channel.send('<@' + str(subject.id) + '> is gayer than your paster from spirit camp.')
				elif 91<=gayness<92:
					await message.channel.send('<@' + str(subject.id) + '> isn\'t gay, but you\'re gay though.')
				elif 92<=gayness<93:
					await message.channel.send('<@' + str(subject.id) + '> isn\'t gay, but is a weeb so... same thing I guess.')
				elif 93<=gayness<94:
					await message.channel.send('<@' + str(subject.id) + '> is your paster from spirit camp. monkaS')
				elif 94<=gayness<95:
					await message.channel.send('<@' + str(subject.id) + '> is gay due to being baguetted by their family.')
					await message.channel.send('f in chat to pay respects to' + '<@' + str(subject.id) + '>')
				elif 95<=gayness<100:
					await message.channel.send('<@' + str(subject.id) + '> is gay, and secretly a tiktok trap.')
plugins = [gaydar]
commands = {
	'gaydar': {
		'usage':'[me|@user] is [%gay]',
		'example': 'User is very gay.'
	}
}
