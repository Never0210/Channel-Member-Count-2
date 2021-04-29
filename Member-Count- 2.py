async def user():
    while True:
              channel = bot.get_channel(HIER DEINE CHANNEL ID) # Channel ID
              guild = bot.get_guild(HIER DEINE SERVER ID) # Server ID
              member = sum(discord.member and not member.bot for member in guild.members)
              await channel.edit(name=f"┗ Mitglieder: {member}")
              await asyncio.sleep(300) # Zeit der Aktualisierung [Nicht unter 5 min]

async def online():
    while True:
              channel2 = bot.get_channel(HIER DEINE CHANNEL ID) # Channel ID
              guild = bot.get_guild(HIER DEINE SERVER ID) # Server ID
              online = sum(member.status!=discord.Status.offline and not member.bot for member in guild.members)
              await channel2.edit(name=f"┏ Online: {online}")
              await asyncio.sleep(300) # Zeit der Aktualisierung [Nicht unter 5 min]