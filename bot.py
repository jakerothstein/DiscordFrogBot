import random
import hikari
import requests
import lightbulb
from bs4 import BeautifulSoup

giphy_api_key = ''  # API KEY

bot = lightbulb.BotApp(
    token=''  # DISCORD BOT TOKEN
)


def get_frog_quote():
    url = 'https://www.goodreads.com/quotes/tag/frogs'

    response = requests.get(url)

    data = BeautifulSoup(response.text, 'html.parser')

    quoteText = data.find_all('div', attrs={'class': 'quoteText'})

    quotes = []
    authors = []

    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
        quotes += [quote]
        author = i.find('span', attrs={'class': 'authorOrTitle'}).text.strip()
        author = author[:len(author) - 1]
        authors += [author]

    i = random.randint(0, len(quotes))
    return [quotes[i], authors[i]]


def get_pepe():
    url = 'https://pepewisdom.com/pwrandom'  # 147 pages

    response = requests.get(url)

    data = BeautifulSoup(response.text, 'html.parser')
    parsed = data.find("img", src=True)["src"]

    return 'https://pepewisdom.com/' + parsed


def random_gif(search):
    headers = {
        'limit': 50,
        'lang': 'en'
    }

    url = 'https://api.giphy.com/v1/gifs/search?q=' + search + '+&api_key=' + giphy_api_key

    response = requests.get(url)
    parsed = response.json()

    return parsed['data'][random.randint(0, 49)]['embed_url']


@bot.command
@lightbulb.command('frog-pic', 'Returns a random photo of a cool frog using a frog photo API')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    rand = str(random.randint(1, 54))
    if len(rand) < 2:
        rand = '0' + rand
    frog_url = 'http://www.allaboutfrogs.org/funstuff/random/00' + rand + '.jpg'
    await ctx.respond(frog_url)


@bot.command
@lightbulb.command('frog-gif', 'Returns a random gif of a cool frog using a giphy API')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    await ctx.respond(random_gif('frogs'))


@bot.command
@lightbulb.command('frog-gif-meme', 'Returns a random gif of a cool frog meme using a giphy API')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    await ctx.respond(random_gif('frog meme'))


@bot.listen(hikari.MessageCreateEvent)
async def react(ctx):
    if ctx.author.id != 1001966977708986519:
        if ctx.content.lower().find("frog") != -1:
            await ctx.message.add_reaction("🐸")


@bot.command
@lightbulb.command('pepe', 'Returns a random image or gif of a pepe')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    await ctx.respond(get_pepe())


@bot.command
@lightbulb.command('frog-quote', 'Returns a random frog themed quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    resp = get_frog_quote()
    quote_text = '*> {}*'.format(resp[0]) + '- ' + resp[1]
    await ctx.respond(quote_text)


bot.run()
