import random
import hikari
import requests
import lightbulb
from bs4 import BeautifulSoup

giphy_api_key = ''  # API KEY

bot = lightbulb.BotApp(
    token=''  # DISCORD BOT TOKEN
)

list_of_frogs = ["Leiopelmatidae", "Ascaphidae", "Bombianura", "Costata", "Bombinatoridae", "Alytidae",
                 "Discoglossidae", "Pipanura", "Xenoanura", "Pipidae", "Rhinophrynidae", "Acosmanura", "Anomocoela",
                 "Scaphiopodidae", "Pelodytidae", "Pelobatoidea", "Pelobatidae", "Megophryidae", "Neobatrachia",
                 "Heleophrynidae", "Phthanobatrachia", "Sooglossoidea", "Sooglossidae", "Nasikabatrachidae",
                 "Notogaeanura", "Australobatrachia", "Calyptocephalellidae", "Myobatrachidae", "Limnodynastidae",
                 "Nobleoanura", "Brachycephaloidea", "Ceuthomantidae", "Brachycephalidae", "Eleutherodactylidae",
                 "Craugastoridae", "Hemiphractidae", "Athesphatanura", "Hylidae", "Leptodactyliformes",
                 "Agastorophrynia", "Bufonidae", "Aromobatidae", "Dendrobatidae", "Diphyabatracea",
                 "Leptodactylidae", "Allophrynidae", "Centrolenidae", "Ceratophryidae", "Odontophrynidae",
                 "Cycloramphidae", "Alsodidae", "Hylodidae", "Telmatobiidae", "Batrachylidae", "Rhinodermatidae",
                 "Ranoides", "Allodapanura", "Microhylidae", "Afrobatrachia", "Xenosyneunitanura", "Brevicipitidae",
                 "Hemisotidae", "Laurentobatrachia", "Hyperoliidae", "Arthroleptidae", "Natatanura",
                 "Ptychadenidae", "Victoranura", "Micrixalidae", "Phrynobatrachidae", "Conrauidae",
                 "Pyxicephaloidea", "Petropedetidae", "Pyxicephalidae", "Nyctibatrachidae", "Ceratobatrachidae",
                 "Saukrobatrachia", "Ranixalidae", "Dicroglossidae", "Aglaioanura", "Rhacophoridae", "Mantellidae",
                 "Ranidae"]  # source: https://en.wikipedia.org/wiki/Frog


def get_random_frog():
    randFrog = list_of_frogs[random.randint(0, len(list_of_frogs) - 1)]
    url = 'https://www.google.com/search?q=' + randFrog + '+frog&source=lnms&tbm=isch'

    response = requests.get(url)

    data = BeautifulSoup(response.text, 'html.parser')

    imageURL = data.find('img', attrs={'class': 'yWs4tf'})['src']

    return [str(imageURL), str(randFrog)]


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


@bot.command
@lightbulb.command('frog-definition', 'Returns the definition of a frog')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    resp = "**Frog** /frôg; fräg/\n*noun*\n> a tailless amphibian with a short squat body, moist smooth skin, " \
           "and very long hind legs for leaping.\n*verb*\n> hunt for or catch frogs. "
    await ctx.respond(resp)


@bot.command
@lightbulb.command('random-frog', 'Returns a random frog')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    resp = get_random_frog()
    embed = hikari.Embed(title="Random Frog", description="Scientific Name: " + resp[1], color=0x59c332)
    embed.set_thumbnail(resp[0])
    embed.set_footer(text="Frog photo from Google")
    await ctx.respond(embed=embed)


@bot.command
@lightbulb.command('frog-gang', 'gives frog gang role')
@lightbulb.implements(lightbulb.SlashCommand)
async def add_role(ctx):
    roles = await bot.rest.fetch_roles(guild=ctx.guild_id)

    create_role = True
    role_add = True
    id_index = int

    for i in range(len(roles)):
        if str(roles[i]) == "🐸 frog gang 🐸":
            create_role = False
            id_index = i
    if create_role:
        role = await bot.rest.create_role(
            ctx.guild_id,
            name="🐸 frog gang 🐸",
            color=0x59c332
        )
        await bot.rest.add_role_to_member(user=ctx.author, guild=ctx.guild_id, role=role)
        resp = "<@" + str(ctx.author.id) + ">" + " is now part of the frog gang  🎉"
        await ctx.respond(resp)
        return
    else:
        for i in range(len(ctx.member.role_ids)):
            if str(ctx.member.role_ids[i]) == str(roles[id_index].id):
                role_add = False
    if role_add:
        await bot.rest.add_role_to_member(user=ctx.author, guild=ctx.guild_id, role=roles[id_index].id)
        resp = "<@" + str(ctx.author.id) + ">" + " is now part of the frog gang  🎉"
    else:
        resp = "<@" + str(ctx.author.id) + ">" + " is already part of the frog gang 💪"
    await ctx.respond(resp)

    # resp += str()
    # await ctx.respond(ctx.author.id.fetch_roles(guild=ctx.guild_id))


bot.run()
