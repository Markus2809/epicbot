@client.command()
async def suggest(ctx, *, args):
    channel = client.get_channel() #Replace with channel ID where suggestion embed will be sent :)
    embed = discord.Embed(title=f'Suggestion from {ctx.author.name}!', description=f'{args}')
    await channel.send(embed=embed)
    await ctx.send(f'Thanks for your feedback! (ctx.author.mention))
