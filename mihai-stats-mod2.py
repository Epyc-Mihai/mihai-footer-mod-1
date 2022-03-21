import ctx as ctx
import discord

class StatsMod:
    def __init__(self, capital: str, nationality: str, country: str, genrank: str, playerreputation: str, empirerole: str, timeplayed: str, updated: int, uuid: int, flag: str, created: str, lan: int, pop: int, factory: int, land: int, emp: str, rank: str, score: float, competitiveRank: str, gdp: str, balance: str, currency: str, coinz: str, tech: str, keys: str, badge1: str, badge2: str, badge3: str):
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
        self.genrank = genrank #generation the player is
        self.capital = capital
        self.nationality = nationality
        self.timeplayed = timeplayed #this shows how much the user played the bot in total
        self.empirerole = empirerole #this shows what rank the user has in his empire (if not in empire then leave empty)
        self.playerreputation = playerreputation #this shows the reputation the user has, bad for cheater, normal for nothing and high for community servant

    def UserMod(self):
        embed = discord.Embed()
        embed.set_author(name=ctx.author.display_name,
        url="https://ungame.wtf",
        icon_url=ctx.author.avatar_url)


        embed=discord.Embed(title="{ctx.author.display_name}'s Stats",
           url="https://ungame.wtf",
           description="tip: You can always change between mods.",
           color=discord.Color.yellow())

        embed.add_field(name="Reputation", value=f"{(self.playerreputation)}")
        embed.add_field(name="Empire Role", value=f"{(self.empirerole)}")
        embed.add_field(name="Time Played", value=f"{(self.timeplayed)}")
        embed.add_field(name="Player Generation", value=f"{(self.genrank)}")
        embed.add_field(name="Competitive Rank", value=f"{(self.competitiveRank)}")
        embed.add_field(name="Land Area", value=f"{(self.lan)}")
        embed.add_field(name="Gross Domestic Product", value=f"{(self.gdp)}")
        embed.set_thumbnail(url=self.flag)
        embed.add_field(name="Coinz", value=f"{(self.coinz)}")
        embed.add_field(name="Empire", value=f"{(self.emp)}")
        embed.add_field(name="Country Population", value=f"{(self.pop)}")
        embed.add_field(name="Badges", value=f"{(self.badge1)}{(self.badge2)}{(self.badge3)}")
        embed.add_field(name="Updated", value=f"{(self.updated)}")
        embed.add_field(name="Processors", value=f"{(self.factory)}")
        embed.add_field(name="Score", value=f"{(self.score)}")
        embed.add_field(name="Unique ID", value=f"{(self.uuid)}")
        embed.add_field(name="Keys", value=f"{(self.keys)}")
        embed.add_field(name="Nationality", value=f"{(self.nationality)}")
        embed.add_field(name="Capital City", value=f"{(self.capital)}")
        embed.add_field(name="Technology Points", value=f"{(self.tech)}")
        embed.add_field(name="Free Land Area", value=f"{(self.land)}")
        embed.add_field(name="Country Name", value=f"{(self.country)}")
        embed.set_footer(text="My nuts, hang, and, add, @everyone.")


        return embed
