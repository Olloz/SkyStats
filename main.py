import json
from discord.ext import commands
from discord.ext.commands import Bot
json_data = open('private.json')
data = json.load(json_data)

client: Bot = commands.Bot(command_prefix='.sb ')
client.remove_command('help')

client.load_extension('cogs.own')
client.load_extension('cogs.skyblock')

client.run(data["discordKey"])
json_data.close()
