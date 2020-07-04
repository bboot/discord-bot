#!/usr/bin/env python3
import argparse
import json
import logging
import os
import sys
import discord
from dotenv import load_dotenv

client = discord.Client()

class CrypticsAssistant:
    def __init__(self):
        self.auth = self.get_auth()

    def run(self):
        client.run(self.auth['token'])

    def get_auth(self):
        #TOKEN = os.getenv('DISCORD_TOKEN')
        auth = {}
        with open('auth.json') as f:
            auth = json.loads(f.read())
        return auth

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
    if message.content.lower() == 'ping':
        await message.channel.send('Pong! 🏓')
    if message.content.lower() == 'hi':
        await message.channel.send('Hi ' + message.author + '!')

@client.event
async def on_error(event, *args, **kwargs):
    with open('bot-err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

def main(args):
    load_dotenv()

    assistant = CrypticsAssistant()
    assistant.run()

    return 0

if __name__=="__main__":
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output')
    args, extra = parser.parse_known_args()
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main(args))
