import discord


class Bot(discord.Client):

    prefix = '%'

    async def on_ready(self):
        print("connected to server: ", self.guilds.__getitem__(0))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        elif message.content.startswith(Bot.prefix):
            message.content = message.content[1:]
            if message.content.startswith('prefix'):
                Bot.prefix = message.content[(len(message.content)-1)]
                strmsg = "New prefix: " + Bot.prefix
                await message.channel.send(strmsg)

        else:
            return
        """if message.author.id != self.user.id:
            await message.channel.send("du bist behindert")"""


client: Bot = Bot()
client.run('ODE2Mzc4MzkyOTY5NjA5MjU3.YD6FoA.DCtvB90xmQ09qPv7_bPa8tbEdaY')
