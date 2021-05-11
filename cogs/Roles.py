import asyncio
import discord
from discord.ext import commands

embedColour = 0xff69b4

class Roles(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def admin_roles(self, ctx):
        yearEmbed = discord.Embed(description="Please select your year of study:")
        yearEmbed.set_author(name='Year')
        yearEmbed.colour = embedColour
        msg = await ctx.send(embed=yearEmbed)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
    
        newsEmbed = discord.Embed(description="Would you like to be pinged for news related to anime & manga?")
        newsEmbed.set_author(name='News')
        newsEmbed.colour = embedColour
        msg = await ctx.send(embed=newsEmbed)
        await msg.add_reaction('📰')

        recommendEmbed = discord.Embed(description="Are willing to chat with someone looking for media recommendations?")
        recommendEmbed.set_author(name='Recommend')
        recommendEmbed.colour = embedColour
        msg = await ctx.send(embed=recommendEmbed)
        await msg.add_reaction('💡')

        irlEventEmbed = discord.Embed(description="Are you willing/able to attend irl events? Most useful for international and commuter students")
        irlEventEmbed.set_author(name='IRL Event')
        irlEventEmbed.colour = embedColour
        msg = await ctx.send(embed=irlEventEmbed)
        await msg.add_reaction('👪')

        gameInviteEmbed = discord.Embed(description="Are you up for playing games online with other society members?")
        gameInviteEmbed.set_author(name='Game Invite')
        gameInviteEmbed.colour = embedColour
        msg = await ctx.send(embed=gameInviteEmbed)
        await msg.add_reaction('🕹️')

        nsfwEmbed = discord.Embed(description="Access to the nsfw chats")
        nsfwEmbed.set_author(name='NSFW')
        nsfwEmbed.colour = embedColour
        msg = await ctx.send(embed=nsfwEmbed)
        await msg.add_reaction('🔞')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        Channel = self.bot.get_channel(837669072497672233)
        if reaction.message.channel.id != 837669072497672233:
            return
        if user.id == 841059265615101952:
            return
        if reaction.emoji == '1️⃣':
            if discord.utils.get(user.roles, id=841373002029334588):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841373002029334588))
            if discord.utils.get(user.roles, id=841373002029334588) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841373002029334588))
        elif reaction.emoji == '2️⃣':
            if discord.utils.get(user.roles, id=841373046938140683):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841373046938140683))
            if discord.utils.get(user.roles, id=841373046938140683) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841373046938140683))
        elif reaction.emoji == '3️⃣':
            if discord.utils.get(user.roles, id=841373144941723718):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841373144941723718))
            if discord.utils.get(user.roles, id=841373144941723718) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841373144941723718))
        elif reaction.emoji == '4️⃣':
            if discord.utils.get(user.roles, id=841373188775739402):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841373188775739402))
            if discord.utils.get(user.roles, id=841373188775739402) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841373188775739402))
        elif reaction.emoji == '📰':
            if discord.utils.get(user.roles, id=841372549497880677):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841372549497880677))
            if discord.utils.get(user.roles, id=841372549497880677) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841372549497880677))
        elif reaction.emoji == '👪':
            if discord.utils.get(user.roles, id=841372653306511430):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841372653306511430))
            if discord.utils.get(user.roles, id=841372653306511430) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841372653306511430))
        elif reaction.emoji == '🕹️':
            if discord.utils.get(user.roles, id=841372712802320385):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841372712802320385))
            if discord.utils.get(user.roles, id=841372712802320385) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841372712802320385))
        elif reaction.emoji == '🔞':
            if discord.utils.get(user.roles, id=841372852276035634):
                return await user.remove_roles(discord.utils.get(user.guild.roles, id=841372852276035634))
            if discord.utils.get(user.roles, id=841372852276035634) is None:
                await user.add_roles(discord.utils.get(user.guild.roles, id=841372852276035634))

def setup(bot): 
    bot.add_cog(Roles(bot))