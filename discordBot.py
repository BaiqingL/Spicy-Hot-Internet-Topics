import spicyHotInternetTopics, asyncio, discord, re
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
posted = []


@client.command()
async def rate(ctx, arg):
    text = temp = re.sub(r"[^A-Za-z0-9 ]+", "", arg)
    positive, negative = spicyHeadlinesInventedToday.getSentiment(text)
    embed = discord.Embed(
        title="Text sentiment analysis",
        description="Uses the MAX Text Sentiment Classifier provided by IBM",
        color=0x738ADB,
    )
    embed.add_field(name="Text", value=arg, inline=False)
    embed.add_field(
        name="Positive Sentiment", value=str(positive * 100)[0:4], inline=False
    )
    embed.add_field(
        name="Negative Sentiment", value=str(negative * 100)[0:4], inline=False
    )
    embed.set_footer(text="https://github.com/IBM/MAX-Text-Sentiment-Classifier")
    await ctx.send(embed=embed)


def goThroughSub(posted):
    post = ""
    url = ""
    sentiment = 0
    subreddits = [
        "relationship_advice",
        "PoliticalCompassMemes",
        "changemyview",
        "insaneparents",
        "actualpublicfreakouts",
        "iamanutterpieceofshit",
    ]
    if len(posted) > 20:
        posted = []
    for subs in subreddits:
        print("Current subreddit:", subs)
        temppost, tempurl, tempsentiment = spicyHeadlinesInventedToday.spiciestInSub(
            subs, posted
        )
        if sentiment == 0:
            post = temppost
            url = tempurl
            sentiment = tempsentiment
        elif sentiment < tempsentiment:
            post = temppost
            url = tempurl
            sentiment = tempsentiment
    posted.append(post)
    return (post, url, sentiment)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


async def background_loop():
    await client.wait_until_ready()
    while True:
        channel = client.get_channel(CHANNEL_ID_HERE)
        post, url, sentiment = goThroughSub(posted)
        print("Posted:", posted)
        print("Posting:", post)
        embed = discord.Embed(
            title="Spicy Hot Internet Topics",
            description="Spiciness confidence: {}%".format(str(sentiment * 100)[0:4]),
            color=0xFF5700,
        )
        embed.add_field(name="Headline", value=post, inline=False)
        embed.add_field(name="Link", value=url, inline=False)
        embed.set_footer(text="Spicy Hot Internet Topics")
        await channel.send(embed=embed)
        await asyncio.sleep(600)


client.loop.create_task(background_loop())

client.run("TOKEN_HERE")
