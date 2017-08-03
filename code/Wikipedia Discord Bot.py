'''
Some links from wikipedia:
https://en.wikipedia.org/wiki/Delaunay_triangulation
https://en.wikipedia.org/wiki/Lexical_chain
https://en.wikipedia.org/wiki/Internet_meme
https://en.wikipedia.org/wiki/Social_status
https://en.wikipedia.org/wiki/Social_Security_number
https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra

Pattern: Capitalised snake case

'''

#TODO https://en.wikipedia.org/w/index.php?title=Iphone&redirect=no
#TODO capitalisation flag (--U)

import discord

client = discord.Client()

def to_snake(spaced_words, flag):
    # TODO special cases, thinking of just brute force
    words = [word for word in spaced_words.split(' ')]
    if not flag:
        words = [word.lower() for word in words]
        words[0] = words[0].title()

    return '_'.join(words)


# Discord API

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    trigger_phrase = '!wikibot'
    keep_capital = False
    if message.content.startswith(trigger_phrase):
        if message.content.endswith('--U'):
            message.content = message.content.rstrip(' --U')
            keep_capital = True
        msg = message.content[len(trigger_phrase)+1::]
        await client.send_message(message.channel, 'https://en.wikipedia.org/wiki/{}'.format(to_snake(msg, keep_capital)))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzQyMjU0MTMzNTQzMzA1MjE2.DGM82w.EVRtBtX91SHKFq8k0cKzYMJbPAY')
