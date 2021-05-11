import discord
import random
from discord.ext import commands
from cogs.utils.gifs import *

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def create_command(self, images, text, user, author, channel):
        em = discord.Embed(description=text)
        em.set_image(url=random.choice(images))
        if author.color != discord.Colour.default():
                em.colour = author.color
        await channel.send(embed=em)

    @commands.command()
    async def cuddle(self, ctx, user: discord.Member):
        await self.create_command(CUDDLE_IMAGES, f'**{user.name}**, you got cuddled by **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        await self.create_command(HUG_IMAGES, f'**{user.name}**, you got a hug from **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @commands.group(invoke_without_command=True)
    async def kiss(self, ctx, user: discord.Member):
        await self.create_command(KISS_IMAGES, f'**{user.name}**, you got a kiss from **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @kiss.command(name='cheek')
    async def kiss_cheek(self, ctx, user: discord.Member):
        await self.create_command(KISS_CHEEK_IMAGES, f'**{user.name}**, you got a kiss on the cheek from **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @kiss.command(name='forehead')
    async def kiss_forehead(self, ctx, user: discord.Member):
        await self.create_command(KISS_FOREHEAD_IMAGES, f'**{user.name}**, you got a kiss on the forehead from **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @kiss.command(name='lips')
    async def kiss_lips(self, ctx, user: discord.Member):
        await self.create_command(KISS_LIPS_IMAGES, f'**{user.name}**, you got a kiss on the lips from **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @commands.command()
    async def lick(self, ctx, user: discord.Member):
        await self.create_command(LICK_IMAGES, f'**{user.name}**, you got licked by **{ctx.author.name}**', user, ctx.author, ctx.channel)

    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        await self.create_command(SLAP_IMAGES, f'**{user.name}**, you got slapped by **{ctx.author.name}**', user, ctx.author, ctx.channel)

def setup(bot): 
    bot.add_cog(Commands(bot))
