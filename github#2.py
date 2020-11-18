import discord
import random
import subprocess
print('stage0')
import asyncio 
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
async def r34(ctx):
	await ctx.send('this is not prohibited dipshit')
	
@client.command()
async def bottoken(ctx):
	await ctx.send('token = this is the bot token lol get jabated')
	
@client.command()
async def creator(ctx):
	await ctx.send('the shitty creator is coolkit7 who has made me come to life')
	
@client.command()
async def bang(ctx):
	await ctx.send('grenade out')
	
@client.command()
async def rp(ctx):
	await ctx.send('dont pirate you dipshit motherfucking asshole')

@client.command()		
async def gender(ctx, *, question):
	responses = ['female.',
	'male.']
	await ctx.send(f'Question:  {question}\nAnswer: {random.choice(responses)}')
	
@client.command()		
async def stupid(ctx):
	await ctx.send('YOU ARE SO FUCKING STUPID I WANT TO DROWN YOUR ASS IN BOILING WATER!!!!')
	
@client.command()
async def bed(ctx):
	await ctx.send('bed whats a bed')
	
@client.command()
async def lol(ctx):
	await ctx.send('(sarcasm)that was so fucking funny woo')
	
@client.command()		
async def pregtest(ctx, *, question):
	responses = ['yes... oi i said no .r34.',
	'no you are gonna be a virgin for life.']
	await ctx.send(f'Question:  {question}\nAnswer: {random.choice(responses)}')
	
@client.command()
async def ohshit(ctx):
 	await ctx.send('(panic)oh shit oh fuck what the fuck is going on fuuuuuck')
 	
@client.command()
async def phew(ctx):
 	await ctx.send('(relieved)phew that was a close one')
 	
@client.command()
async def ewbit(ctx):
	await ctx.send('learn how to spell bot you fucking idiot')
	
@client.command(aliases=['stupod', 'dupid','stypid','stulid'])
async def stupif(ctx):
	await ctx.send('quit calling people stupid if you dont even know how to spell fuck you dipshit')
	
@client.command()
async def ydoiluvthisbot(ctx):
	await ctx.send('thx for loving this bot if you want you can download it yourself just say .githubcoolkit7 remember you need your own bot token and if there are any bug plz do tell me i test this bot out my self and I do really like it')

    
@client.command(aliases=['?'])  
async def wha(ctx):
	await ctx.send('wtf did i do i was in admin')

	
@client.command()
async def lolf(ctx):
	await ctx.send('that was so FUCKING HILARIOUS LOL!')
	
@client.command()
async def day(ctx, *, question):
	responses = ['it is gonna be trash.',
	'woah bro i have never seen a worser day.'
	'this is gonna be the best day of your life.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.',
	'today is just gonna be normal.']
	await ctx.send(f'Question:  {question}\nAnswer: {random.choice(responses)}')
	
@client.command()
async def english(ctx):
	await ctx.send('english is such a stulid class that i dont even understand why i have to take it even though its my first language')

 
client.run('token')