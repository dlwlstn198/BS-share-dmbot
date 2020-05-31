
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('노네임_DM봇')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==714784133133500428:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="제목")
                        embed.add_field(name="DM봇", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/Ez4n3xk")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzE2NjUxMjc2MDExODMxMzI2.XtO8jg.iKiWBQlrEUHQQGk4sfVhBTM9v-s')
