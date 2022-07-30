import random
import hikari
import requests
import lightbulb
from bs4 import BeautifulSoup

giphy_api_key = 'qwFFSLDhGoPgbVLqHfk2pvabFopF8K9u'  # API KEY

bot = lightbulb.BotApp(
    token='MTAwMTk2Njk3NzcwODk4NjUxOQ.G-dkY4.Nt97IBnFqqRJdWZnYgg4f_YVip6iJUqCcXx0Wk'  # DISCORD BOT TOKEN
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

list_of_frog_facts = [
    'There is evidence that frogs have roamed the Earth for more than 200 million years, at least as long as the dinosaurs.',
    'The world\'s largest frog is the goliath frog of West Africa—it can grow to 15 inches and weigh up to 7 pounds. A goliath frog skeleton is featured in Frogs: A Chorus of Colors.',
    'One of the smallest is the Cuban tree toad, which grows to half an inch long.',
    'While the life spans of frogs in the wild are unknown, frogs in captivity have been known to live more than 20 years.',
    'There are over 6,000 species of frogs worldwide. Scientists continue to search for new ones.',
    'Toads are frogs. The word "toad" is usually used for frogs that have warty and dry skin, as well as shorter hind legs.',
    'Frogs have excellent night vision and are very sensitive to movement. The bulging eyes of most frogs allow them to see in front, to the sides, and partially behind them. When a frog swallows food, it pulls its eyes down into the roof of its mouth, to help push the food down its throat.',
    'Frogs were the first land animals with vocal cords. Male frogs have vocal sacs—pouches of skin that fill with air. These balloons resonate sounds like a megaphone, and some frog sounds can be heard from a mile away.',
    'Launched by their long legs, many frogs can leap more than 20 times their body length.',
    'The Costa Rican flying tree frog soars from branch to branch with the help of its feet. Webbing between the frog\'s fingers and toes extends out, helping the frog glide.',
    'To blend into the environment, the Budgett\'s frog is muddy brown in color, while the Vietnamese mossy frog has spotty skin and bumps to make them look like little clumps of moss or lichen.',
    'Many poisonous frogs, such as the golden poison frog and dyeing poison frog, are boldly colored to warn predators of their dangerous toxic skins. Some colorful frogs, such as the Fort Randolph robber frog, have developed the same coloring as a coexisting poisonous species. Although their skins are not toxic, these mimics may gain protection from predators by looking dangerous.',
    'Like all amphibians, frogs are cold-blooded, meaning their body temperatures change with the temperature of their surroundings. When temperatures drop, some frogs dig burrows underground or in the mud at the bottom of ponds. They hibernate in these burrows until spring, completely still and scarcely breathing.',
    'The wood frog can live north of the Arctic Circle, surviving for weeks with 65 percent of its body frozen. This frog uses glucose in its blood as a kind of antifreeze that concentrates in its vital organs, protecting them from damage while the rest of the body freezes solid.',
    'The Australian water-holding frog is a desert dweller that can wait up to seven years for rain. It burrows underground and surrounds itself in a transparent cocoon made of its own shed skin.',
    'Frogs are freshwater creatures, although some frogs such as the Florida leopard frog are able to live in brackish or nearly completely salt waters.',
    'Almost all frogs fertilize the eggs outside of the female\'s body. The male holds the female around the waist in a mating hug called amplexus. He fertilizes the eggs as the female lays them. Amplexus can last hours or days. One pair of Andean toads stayed in amplexus for four months.',
    'The marsupial frog keeps her eggs in a pouch like a kangaroo. When the eggs hatch into tadpoles, she opens the pouch with her toes and spills them into the water.',
    'The gastric brooding frog of Australia swallows her fertilized eggs. The tadpoles remain in her stomach for up to eight weeks, finally hopping out of her mouth as little frogs. During the brooding period, gastric secretions cease—otherwise she would digest her own offspring.',
    'Among Darwin frogs, it is the male who swallows and stores the developing tadpoles in his vocal sac until juvenile frogs emerge.',
    'Pipa pipa, the Suriname toad of South America, carries her young embedded in the skin of her back. After mating, the eggs sink gradually into the female\'s back, and a skin pad forms over the eggs. The developing juvenile frogs are visible inside their pockets for several days before hatching. They emerge over a period of days, thrusting their head and forelegs out first, then struggling free.',
    'One gram of the toxin produced by the skin of the golden poison dart frog could kill 100,000 people.',
    'A frog completely sheds its skin about once a week. After it pulls off the old, dead skin, the frog usually eats it.',
    'When a frog swallows its prey, it blinks, which pushes its eyeballs down on top of the mouth to help push the food down its throat.',
    'A group of birds is called a flock, a group of cattle is called a herd, but a group of frogs is called an army.',
    'There is a frog in Indonesia that has no lungs – it breathes entirely through its skin.',
    'The waxy monkey frog secretes a wax from its neck and uses its legs to rub that wax all over its body. The wax prevents the skin of the frog from drying out in sunlight.',
    'Most frogs have teeth, although usually only on their upper jaw. The teeth are used to hold prey in place until the frog can swallow it.',
    'The biggest frog in the world is the Goliath frog. It lives in West Africa and can measure more than a foot in length and weigh more than 7 pounds – as much as a newborn baby.',
    'There’s a type of poison dart frog called the blue-jeans frog; it has a red body with blue legs. It is also sometimes called the strawberry dart frog.',
    'The red-eyed tree frog lays it eggs on the underside of leaves that hang over water. When the eggs hatch, the tadpoles fall into the water below.',
    'The female Surinam toad lays up to 100 eggs, which are then distributed over her back. Her skin swells around the eggs until they become embedded in a honeycomb-like structure. After 12 to 20 weeks, fully formed young toads emerge by pushing out through the membrane covering the toad’s back.']  # source: https://www.amnh.org/exhibitions/frogs-a-chorus-of-colors/frog-fun-facts & https://www.smithsonianmag.com/science-nature/14-fun-facts-about-frogs-180947089/


def get_high_rez_frog():
    url = 'https://unsplash.com/images/animals/frog'

    response = requests.get(url)

    data = BeautifulSoup(response.text, 'html.parser')

    image_data = data.find_all('img', attrs={'class': 'YVj9w', 'alt': True})

    rand_int = random.randint(0, len(image_data) - 1)

    return [image_data[rand_int]['src'],
            image_data[rand_int]['alt']]


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
    embed = hikari.Embed(title="Frog Definition",
                         description="**Frog** /frôg; fräg/\n*noun*\n> a tailless amphibian with a short squat body, moist smooth skin, " \
                                     "and very long hind legs for leaping.\n*verb*\n> hunt for or catch frogs.",
                         color=0x59c332)
    embed.set_footer(text="Definition by Oxford Languages")
    await ctx.respond(embed=embed)


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


@bot.command
@lightbulb.command('frog-fact', 'Returns a cool frog fact')
@lightbulb.implements(lightbulb.SlashCommand)
async def pic(ctx):
    fact = list_of_frog_facts[random.randint(0, len(list_of_frog_facts) - 1)]
    frog_img = get_high_rez_frog()
    embed = hikari.Embed(title="Frog Fact", description=fact + "\n\nImage Caption: " + frog_img[1], color=0x59c332)
    embed.set_thumbnail(frog_img[0])
    embed.set_footer(text="Frog photo from Unsplash")
    await ctx.respond(embed=embed)


bot.run()
