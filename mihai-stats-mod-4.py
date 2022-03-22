import ctx as ctx
import discord

class StatsMod:
    def __init__(self, capital: str, nationality: str, country: str, updated: int, uuid: int, flag: str, created: str, lan: int, pop: int, factory: int, land: int, emp: str, rank: str, score: float, competitiveRank: str, gdp: str, balance: str, currency: str, coinz: str, tech: str, keys: str, badge1: str, badge2: str, badge3: str):
        self.country = country
        self.updated = updated
        self.uuid = uuid
        self.flag = flag
        self.created = created
        self.lan = lan
        self.pop = pop
        self.factory = factory
        self.land = land
        self.emp = emp
        self.rank = rank
        self.score = score
        self.competitiveRank = competitiveRank
        self.gdp = gdp
        self.balance = balance
        self.currency = currency
        self.coinz = coinz
        self.tech = tech
        self.keys = keys
        self.badge1 = badge1
        self.badge2 = badge2
        self.badge3 = badge3
        self.capital = capital
        self.nationality = nationality

    def UserMod(self):
        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name,
        url="https://ungame.wtf",
        icon_url=ctx.author.avatar_url)


        embed=discord.Embed(title="{ctx.author.display_name}'s Stats",
           url="https://ungame.wtf",
           description="tip: You can always change between mods.",
           color=discord.Color.yellow())

        embed.add_field(name="Competitive Rank", value=f"{(self.competitiveRank)}",inline=False)
        embed.add_field(name="Land Area", value=f"{(self.lan)}" , inline=False)
        embed.add_field(name="Gross Domestic Product", value=f"{(self.gdp)}" , inline=False)
        embed.set_thumbnail(url=self.flag)
        embed.add_field(name="Coinz", value=f"{(self.coinz)}", inline=False)
        embed.add_field(name="Empire", value=f"{(self.emp)}", inline=False)
        embed.add_field(name="Country Population", value=f"{(self.pop)}", inline=False)
        embed.add_field(name="Badges", value=f"{(self.badge1)}{(self.badge2)}{(self.badge3)}", inline=False)
        embed.add_field(name="Updated", value=f"{(self.updated)}", inline=False)
        embed.add_field(name="Processors", value=f"{(self.factory)}", inline=False)
        embed.add_field(name="Score", value=f"{(self.score)}", inline=False)
        embed.add_field(name="Unique ID", value=f"{(self.uuid)}", inline=False)
        embed.add_field(name="Keys", value=f"{(self.keys)}", inline=False)
        embed.add_field(name="Nationality", value=f"{(self.nationality)}", inline=False)
        embed.add_field(name="Capital City", value=f"{(self.capital)}", inline=False)
        embed.add_field(name="Technology Points", value=f"{(self.tech)}", inline=False)
        embed.add_field(name="Free Land Area", value=f"{(self.land)}", inline=False)
        embed.add_field(name="Country Name", value=f"{(self.country)}", inline=False)
        embed.set_footer(text="My nuts, hang, and, add, @everyone.")


        return embed
