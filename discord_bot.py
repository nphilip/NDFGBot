# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import os

client = discord.Client()
tohangup = ""

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!nightnight'):
    #    member = message.mentions[0]

        for currentchannel in message.server.channels:
            if(currentchannel.name == "Admiral"):
              chanelid = currentchannel.id
              channeltoremove = currentchannel

        await client.delete_channel(channeltoremove)
        await client.create_channel(message.server, 'Admiral', type=discord.ChannelType.voice)
        msg = ('Good night. All users have been removed from Admiral.').format(message)
        msg = msg.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!test-new'): # New code using rewrite branch method
            with message.channel.typing():
                await message.channel.send('Message written using message.channel.send')
    elif message.content.startswith('!add'):
        member = message.mentions[0]
        msg = ('Adding %s to the priority' % member)
        msg = msg.format(message)
    #    role = message.guild.roles.find(r => r.name === "Moonman")
        server = message.server
        role = discord.utils.get(server.roles, name="Moonman")
        await client.add_roles(member, role)
    #    membr = message.mentions[0]
    #    membr.addRole("Moonman").catch(console.error)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!remove'):
        member = message.mentions[0]
        msg = ('Removing %s from the priority' % member)
        msg = msg.format(message)
    #    role = message.guild.roles.find(r => r.name === "Moonman")
        server = message.server
        role = discord.utils.get(server.roles, name="Moonman")
        await client.remove_roles(member, role)
    #    membr = message.mentions[0]
    #    membr.addRole("Moonman").catch(console.error)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!bot'):
        msg = 'I am not a robot.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Hello'):
        msg = 'Helllllo.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Hey'):
        msg = 'Yo.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('hey'):
        msg = 'sup dude.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('hangup'):
        msg = str(message.mentions[0])
        await client.send_message(message.channel, msg)
    #    msg = str(message.author)
    #    await client.send_message(message.channel, msg)
        server = message.server
#        vClient = client.voice_client_in(server)
#        chosenMember = server.get_member_named(msg)
#        vClient.disconnect();
        client.join_voice_channel('Admiral')
        hah = client.is_voice_connected(server)
        print(hah)
    #    if message.mentions[0] == :
    #        msg = 'Deleting {0.author.mention}'.format(message)
    #        await client.send_message(message.channel, msg)
#        tohangup = str(message.mentions[0])
#        msg = str(client.voice_clients)
#        await client.send_message(message.channel, msg)
#        for x in client.voice_clients:
#            msg = str(x.user.id)
#            await client.send_message(message.channel, msg)
#            if x.server == ctx.message.server:
#                msg = str(x.user)
#                await client.send_message(message.channel, msg)
#                if x.user == tohangup:
                #    msg = "Disconecting?".format(message)
                #    await client.send_message(message.channel, msg)
#                    return await x.disconnect()
#            return await client.say("NO")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ.get('DISCORD_BOT_KEY')) # NO HARDCODED TOKENS, LILY.
