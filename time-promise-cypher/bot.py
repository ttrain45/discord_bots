import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

@bot.command()
async def book_init(ctx):
    #TODO
@bot.command()
async def get_password(ctx):
    #TODO

@bot.command()
async def menu(ctx):
    #TODO

@bot.command()
async def retrieve_contents(ctx):
    #TODO

@bot.command()
async def dis_print(ctx):
    #TODO

@bot.command()
async def percent_example(ctx):

    await ctx.send('Enter the original price: ')
    message_response = await bot.wait_for('message', check=lambda m: m.author == ctx.author)
    print(message_response)
    original_price = float(message_response.content)

    await ctx.send('Enter how much percantage: ')
    message_response = await bot.wait_for('message', check=lambda m: m.author == ctx.author)
    input_percantage = float(message_response.content)

    # Your calculations
    discount = ( input_percantage / 100) * original_price 
    finalCost = original_price - discount

    await ctx.send(f"You saved {discount}. Your total is, {finalCost}")


bot.run('{TOKEN}')