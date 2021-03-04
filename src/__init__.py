import discord
import TicTacToe
import time as t

class Bot(discord.Client):
    prefix = '%'

    async def on_ready(self):
        print("connected to server: ", self.guilds.__getitem__(0))

    async def status_task(self):
        while True:
            await client.change_presence(activity=discord.Game('Simon'), status = discord.Status.online)
            t.sleep(2)
            await client.change_presence(activity=discord.Game('ist'), status=discord.Status.online)
            t.sleep(2)
            await client.change_presence(activity=discord.Game('lost'), status=discord.Status.online)
            t.sleep(2)

    async def on_message(self, message):
        if message.author.id != self.user.id and message.content.startswith(Bot.prefix):
            message.content = message.content[1:]
            if message.content.startswith('prefix'):
                Bot.prefix = message.content[(len(message.content) - 1)]
                strmsg = "New prefix: " + Bot.prefix
                await message.channel.send(strmsg)

            if message.content.startswith('play'):
                await play(message)

            if message.content.startswith('tictactoe'):
                await tictactoe(message)

            if message.content.startswith('join'):
                await join(message)

            if message.content.startswith('cross'):
                await cross(message)

            if message.content.startswith('reset'):
                await reset(message)


tic_tac_toe = TicTacToe
player_ids = []


async def play(message):
    await message.channel.send(
        'You can play these games: \n    -tictactoe\n\nTo play one, simply type its name after a "%" prefix!')


async def tictactoe(message):
    player_ids.append(message.author.id)
    await message.channel.send('You are Player X!\nYour mate can join via "%join"!')


async def join(message):
    player_ids.append(message.author.id)
    await message.channel.send(
        'You are Player O! Player X can start now with "%cross x" where x denotes a number between 1 and 9')
    tic_tac_toe.game = tic_tac_toe.Game(player_ids[0], player_ids[1])


async def cross(message):
    message.content = message.content[6:]
    await message.channel.send(tic_tac_toe.game.move(message.author.id, int(message.content)))
    if tic_tac_toe.game.get_winner():
        await message.channel.send(tic_tac_toe.game.get_winner())


async def reset(message):
    if not tic_tac_toe.game.get_winner():
        await message.channel.send('There is already a game in progress!')
    else:
        await message.channel.send(tic_tac_toe.game.reset())


client: Bot = Bot()
client.run('ODE2Mzc4MzkyOTY5NjA5MjU3.YD6FoA.uPFGI0G0oMXq-jyRCpk9DjTJ5eA')
