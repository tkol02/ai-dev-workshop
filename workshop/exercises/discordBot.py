import random
import discord
from botCode import code as botcode
from discord.ext import commands

intents = discord.Intents.all()  # Enable all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}! I am the game bot :D. To get help type "!howto!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Goodbye {ctx.author.mention}. Have a nice day.')

@bot.command()
async def howto(ctx):
    await ctx.send(f'To play rps type "!rps [rock, paper, scissors]"')

@bot.command()
async def rps(ctx, choice: str):
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    choice = choice.lower()

    if choice in choices:
        result = determine_winner(choice, bot_choice)
        await ctx.send(f'You chose {choice}, I chose {bot_choice}. {result}')
    else:
        await ctx.send("Invalid choice. Choose 'rock', 'paper', or 'scissors'.")

def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
         (player_choice == 'paper' and bot_choice == 'rock') or \
         (player_choice == 'scissors' and bot_choice == 'paper'):
        return "You win!"
    else:
        return "I win!"

bot.run(botcode)  # Replace with your bot's token
