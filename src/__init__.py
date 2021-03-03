import discord


class Bot(discord.Client):
    async def on_ready(self):
        print("connected to server: ", self.guilds.__getitem__(0))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        elif message.content.startswith('Hallo'):
            message.channel.send('Du bist immernoch behindert')


        """if message.author.id != self.user.id:
            await message.channel.send("du bist behindert")"""


client: Bot = Bot()
client.run('ODE2Mzc4MzkyOTY5NjA5MjU3.YD6FoA.DCtvB90xmQ09qPv7_bPa8tbEdaY')
