# NDFGBot
Discord Bot for the Non-Degenerate Friend Group (NDFG)


Requirements:
* Python 3.7
* Environment Variables 

Python dependencies
* Rapptz's Discord.py, using rewrite branch
* requests

Env vars set:
* Discord Bot Key
* Telnyx SMS Key
* LIFX API key (optional)
* Private data (cell phones, for example)

Probably good, but not necessary with some tweaking:
* Telnyx (You can honestly use any telecom provider that uses a JSON API call to send text messages, but this is spec'd for Telnyx v1 out of the box.)

Setup
1. Grab a copy of the repo.
2. Using your preferred CD tool, deploy the code to your PaaS platform. Remember that it requires Python 3.7 and environment variables set. (Or just clone the repo locally).
3. Run discord.py
