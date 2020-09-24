import discord
import random
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready.')
	
	
@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.')
	
@client.event
async def on_member_remove(meber):
		print(f'{member} has left the server')
		
@client.command()
async def ping(ctx):
	await ctx.send(f'pong! {round(client.latency * 1000)}ms')
	
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
	responses = ['As I see it, yes.',
	 'Ask again later.',
	 'Better not tell you now.',
	 'Cannot predict now.',
	 'Concentrate and ask again.',
 	'Don’t count on it.',
	 'It is certain.',
	 'It is decidedly so.',
	 'Most likely.',
 	'My reply is no.',
	 'My sources say no.',
 	'Outlook not so good.',
	 'Outlook good.' 
 	'Reply hazy, try again.',
	 'Signs point to yes.',
	 'Very doubtful.',
 	'Without a doubt.',
	 'Yes.',
	 'Yes – definitely.',
	 'You may rely on it.'] 
	await ctx.send(f'Question:  {question}\nAnswer: {random.choice(responses)}')
	
@client.command()
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount)
 
@client.command()
async def kick(ctx, member : discord.Member, *, reason=0):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=0):
 await member.ban(reason=reason)
 
@client.command()
async def ewbot(ctx):
	await ctx.send('the fuck you say to me you little shit')
  
@client.command()
async def flash(ctx):
	await ctx.send('bang')
	
@client.command()
async def botisshit(ctx):
	await ctx.send('owner ban him')
	
@client.command()
async def servers(ctx):
	await ctx.send('here https://discord.gg/VqAxN5.,https://discord.gg/8bS7aWR.,https://discord.gg/PgwPSVm')
	
@client.command()
async def r34(ctx):
	await ctx.send('this is not prohibited dipshit')
	
@client.command()
async def bottoken(ctx):
	await ctx.send('token = this is the bot token lol get jabated')
	
@client.command()
async def creator(ctx):
	await ctx.send('the shitty creator is coolkit7 who has made me come to life while lazr keeps me on')
	
@client.command()
async def bang(ctx):
	await ctx.send('grenade out')
	
@client.command()
async def rp(ctx):
	await ctx.send('dont pirate you dipshit motherfucking asshole im talking to you laz')
 
client.run(token)
