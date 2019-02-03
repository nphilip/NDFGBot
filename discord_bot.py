# Non-Degenerate Friend Group Discord Bot

# Initializations
import discord # Obviously, as a Discord Bot, an include is necessary for that portion
import os # Required for pulling environment variables
import requests # Required for building POST requests
import json # Correctly format JSON

# References
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

# Switches
debug = True # Enables verbose outputs for diagnostics.

# Debug
if debug == True:
    print ('Running debug statements:')
    print (os.environ.get('DISCORD_BOT_KEY'))
    print (os.environ.get('LIFX_Key_Phil'))
    print (os.environ.get('Phils-cell'))
    print (os.environ.get('Telnyx_Phone'))
    print (os.environ.get('Telnyx_SMS_Key'))

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

    elif message.content.startswith('!test-new'): # Test code using rewrite branch method
            with message.channel.typing():
                await message.channel.send('Message written using message.channel.send')

    elif message.content.startswith('!phil-lightstoggle'): # Toggle Phil's lights
            await message.channel.send('Sending lights toggle command to LIFX bulbs @ Phil (all)')
            token = os.environ.get('LIFX_Key_Phil')
            response = requests.post('https://api.lifx.com/v1/lights/all/toggle', auth=(token, ''))
            await message.channel.send(response.text)

    elif message.content.startswith('!phil-programmingmode'):
            with message.channel.typing():
                await message.channel.send("Changing lights to try and stay the fuck awake.")
                token = os.environ.get('LIFX_Key_Phil')
                payload = {
                    "color": "kelvin:9000",
                    "brightness" : "100",
                    "power": "on",
                    }
                response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, auth=(token, ''))
                await message.channel.send(response.text)

    elif message.content.startswith('!phil-lightsoff'):
        with message.channel.typing():
                await message.channel.send("Night-night time.")
                token = os.environ.get('LIFX_Key_Phil')
                payload = {
                    "power" : "off"
                }
                response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, auth=(token, ''))
                await message.channel.send(response.text)
            
    elif message.content.startswith('!fuckyou-phil'): # Send a meanie text message to Phil
            await message.channel.send('Sending a fuck you to Phil')
            headers = {'x-profile-secret': os.environ.get('Telnyx_SMS_Key'), 'Content-Type':'application/json'}
            payload = json.dumps({'from': os.environ.get('Telnyx_Phone'), 'to': os.environ.get('Phils-cell'), 'body': 'Fuck you!'})
            if debug == True:
                print ("Printing var = payload:")
                print (payload)
                print ("Printing var = headers:")
                print (headers)
            response = requests.post('https://sms.telnyx.com/messages', data=payload, headers=headers)
            await message.channel.send(response.text)

    elif message.content.startswith('!fuckyou-lily'): # Send a meanie text message to Lily
            await message.channel.send('Sending a fuck you to Lily')
            headers = {'x-profile-secret': os.environ.get('Telnyx_SMS_Key'), 'Content-Type':'application/json'}
            payload = json.dumps({'from': os.environ.get('Telnyx_Phone'), 'to': os.environ.get('Lilys-cell'), 'body': 'Fuck you!'})
            if debug == True:
                print ("Printing var = payload:")
                print (payload)
                print ("Printing var = headers:")
                print (headers)
            response = requests.post('https://sms.telnyx.com/messages', data=payload, headers=headers)
            await message.channel.send(response.text)
                                       
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
