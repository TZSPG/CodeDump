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


import discord
import urllib.request

client = discord.Client()
game = discord.Game()


def to_snake(spaced_words, flag):
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
        if message.content.endswith('--random'):
            opener = urllib.request.build_opener()
            request = urllib.request.Request('https://en.wikipedia.org/wiki/Special:Random')
            u = opener.open(request)
            await client.send_message(message.channel,
                                      u.geturl())
            return
        msg = message.content[len(trigger_phrase)+1::]
        await client.send_message(message.channel, 'https://en.wikipedia.org/wiki/{}'.format(to_snake(msg, keep_capital)))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    game.name = 'with the grandkids'
    await client.change_status(game)

    for channel in client.get_all_channels():
        await client.send_message(channel, 'Wikibot is now operational! Type "!wikibot" to use.')


with open('bot-token.txt','r') as file:
    client.run(file.read())
