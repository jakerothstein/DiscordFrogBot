import random
import hikari
import requests
import lightbulb


def random_frog_gif(search):
    giphy_api_key = ''  # API KEY
    headers = {
        'limit': 50,
        'lang': 'en'
    }

    url = 'https://api.giphy.com/v1/gifs/search?q=' + search + '+&api_key=' + giphy_api_key

    response = requests.get(url)
    parsed = response.json()

    return parsed['data'][random.randint(0, 49)]['embed_url']


bot = lightbulb.BotApp(
    token=''  # DISCORD BOT TOKEN
)


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
    await ctx.respond(random_frog_gif('frogs'))


@bot.command
@lightbulb.command('frog-gif-meme', 'Returns a random gif of a cool frog meme using a giphy API')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    await ctx.respond(random_frog_gif('frog meme'))


@bot.listen(hikari.MessageCreateEvent)
async def react(ctx):
    if ctx.content.lower().find("frog") != -1:
        await ctx.message.add_reaction("🐸")


bot.run()
