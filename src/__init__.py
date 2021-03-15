import discord
import TicTacToe
import RockPaperScissors
import time as t

class Bot(discord.Client):
    prefix = '%'

    async def on_ready(self):
        print("connected to server: ", self.guilds.__getitem__(0))
        await client.change_presence(activity=discord.Game("Der Coolste aufm Server"), status=discord.Status.online)


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

            if message.content.startswith('rps'):
                await rockpaperscissors(message)

            if message.content.startswith('rock') or message.content.startswith('paper') or message.content.startswith('scissor'):
                await rockpaperscissorsPlay(message)


tic_tac_toe = TicTacToe
rock_paper_scissors = RockPaperScissors
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

async def rockpaperscissors(message):
    await message.channel.send('To play Rock, Paper, Scissors against the bot, use the commands "%rock", "%paper", "%scissor"')

async def rockpaperscissorsPlay(message):
    await message.channel.send(rock_paper_scissors.play(message.content))


client: Bot = Bot()
client.run('')
