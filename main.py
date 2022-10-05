'https://www.youtube.com/watch?v=SPTfmiYiuok'
'https://insult.mattbas.org/api/random'

import discord
import os
import requests
import json
import random



client = discord.Client()

trigger_words = ["sad" , "depressed", "gay", "good", "cracked", "gamer", "lol", "bot", "who", "lmao", "lmfao", "bro", "duke", "dude", "whats", "val", "up", "impostor"] 

sus_triggers = ['sus', 'among us']

sus_response = ['https://tenor.com/view/among-us-amog-us-among-shitting-shitting-gif-19980480',
'https://tenor.com/view/boiled-soundcloud-boiled-boiled-irl-boiled-utsc-boiled-cheesestick-agem-soundcloud-gif-20049996', 'https://tenor.com/view/among-us-gif-18684920']

start_response = [ "ayo", "u are stone head :moyai:", "easy", "to be frank, I would have to be jackson Mcguinness", 'homophobic, scared of homes', ':beareded_person::beer:', ":skull: imagine talking to a bot ", 'im homophone', 'literally the sussest person'
]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

'''
def update_response(msg):
  if "response" in db.keys():
    response = db['response']
    response.append(msg)
    db['response'] = response
  else:
    db['response'] = [msg]

def delete_response(index):
  response = db['response']
  if len(response)>index:
    del response[index]
    db['response'] = response
'''



@client.event
async def on_ready():
  #this formats the login to duke bot#0322 when printing
  print('logged in as {0.user}'.format(client))

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='deez nuts'))


@client.event
async def on_message(message):
  if message.author == client.user:
    return


  msg = message.content

  if msg.startswith('.bean'):
    await message.channel.send(get_quote())
  
  if msg.startswith(".help"):
    await message.channel.send("commands: .bean .ping rick and bruh\nmore functions soon \n- soy#0310")

  if msg.startswith(".ping"):
    await message.channel.send("@everyone lol")

  if msg.startswith("santi"):
    await message.channel.send("santi is gay")
  
  if any(word in msg for word in trigger_words):
    await message.channel.send(random.choice(start_response))
  
  if any(word in msg for word in sus_triggers):
    await message.channel.send(random.choice(sus_response))

  if msg.startswith("rick"):
    await message.channel.send("https://tenor.com/view/rick-ashley-dance-80s-music-gif-12136175")

  if msg.startswith("bruh"):
    await message.channel.send('https://tenor.com/view/ricky-berwick-we-be-fighting-bruh-fight-gif-12675481')
  
#actually runs the bot using the token from the environment(.env) file
client.run(os.getenv('token'))

