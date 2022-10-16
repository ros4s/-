from datetime import datetime
import discord, asyncio, pytz
import json

with open('token.json') as f:
    json_object = json.load(f)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("This sentense is printed on terminal")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Bot Status"))

@client.event
async def on_message(message):
    if message.content == "test" or message.content == "Test":
        await message.channel.send("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send("{} | {}, User, Hello".format(message.author, message.author.mention))
    if message.content == "embed":
        embed = discord.Embed(title="제목", description="부제목", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="임베드 라인 1- inline - false", value="라인 이름에 해당하는 값", inline=False)
        embed.add_field(name="임베드 라인 2- inline - false", value="라인 이름에 해당하는 값", inline=False)

        embed.add_field(name="임베드 라인 3- inline - true", value="라인 이름에 해당하는 값", inline=True)
        embed.add_field(name="임베드 라인 4- inline - true", value="라인 이름에 해당하는 값", inline=True)

        embed.set_footer(text="Bot Model by. ros4s", icon_url="이미지링크")
        await message.channel.send(embed=embed)

client.run(json_object['token'])