# Non-Degenerate Friend Group Discord Bot

# Initializations
import discord # Obviously, as a Discord Bot, an include is necessary for that portion
import os # Required for pulling environment variables
import requests # Required for building POST requests
import json # Correctly format JSON

# References
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

# Switches
debug = False # Enables verbose outputs for diagnostics.

# Debug
if debug == True:
    print ('Running debug statements:')
    print (os.environ.get('DISCORD_BOT_KEY'))
    print (os.environ.get('LIFX_Key_Phil'))
    print (os.environ.get('Phils-cell'))
    print (os.environ.get('Telnyx_Phone'))
    print (os.environ.get('Telnyx_SMS_Key'))

client = discord.Client()

@client.event
async def on_ready():
    print('------')
    print('Logged in as', client.user.name,)
    print('Client UserID: ', client.user.id)
    print('------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!test-new'): # Test code using rewrite branch method
        with message.channel.typing():
            await message.channel.send('Message written using message.channel.send')

    if message.content.startswith('!phil-lightstoggle'): # Toggle Phil's lights
        await message.channel.send('Sending lights toggle command to LIFX bulbs @ Phil (all)')
        with message.channel.typing():
            token = os.environ.get('LIFX_Key_Phil')
            response = requests.post('https://api.lifx.com/v1/lights/all/toggle', auth=(token, ''))
        await message.channel.send(response.text)

    if message.content.startswith('!phil-getlights'):
            await message.channel.send('Getting lights status')
            with message.channel.typing():
                token = os.environ.get('LIFX_Key_Phil')
                response = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))
            await message.channel.send(response.text)

    if message.content.startswith('!phil-programmingmode'):
        await message.channel.send("Changing lights to try and stay the fuck awake.")
        with message.channel.typing():
            token = os.environ.get('LIFX_Key_Phil')
            payload = {
                "color": "kelvin:9000",
                "brightness" : "100",
                "power": "on",
                }
            response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, auth=(token, ''))
        await message.channel.send(response.text)

    if message.content.startswith('!phil-lightsoff'):
        with message.channel.typing():
            await message.channel.send("Night-night time.")
            token = os.environ.get('LIFX_Key_Phil')
            payload = {
                "power" : "off"
            }
            response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, auth=(token, ''))
            await message.channel.send(response.text)
            
    if message.content.startswith('!fuckyou-phil'): # Send a meanie text message to Phil
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

    if message.content.startswith('!fuckyou-lily'): # Send a meanie text message to Lily
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

client.run(os.environ.get('DISCORD_BOT_KEY')) # NO HARDCODED TOKENS, LILY.