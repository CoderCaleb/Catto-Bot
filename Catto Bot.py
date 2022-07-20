import discord
import os
import requests
import json
import random
client = discord.Client()
yes = True
def get_pic():
  cattoURL = requests.api.get("https://api.thecatapi.com/v1/images/search").json()[0]['url']
  print(cattoURL)
def get_fact():
  catFact = requests.get("https://catfact.ninja/fact?max_length=140")
  json_data = json.loads(catFact.text)
  return json_data['fact']
print(get_fact())                               
fact = get_fact()
catResponse = ["Heres a catto for you :D","Omg! A wild catto popped up.", "Imagine liking dogs...","Hope you brought pizza"]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
     return

  if message.content.startswith('-catto') or message.content.startswith('-Catto'): 

   await message.channel.send(random.choice(catResponse))
   
   await message.channel.send(content=requests.api.get("https://api.thecatapi.com/v1/images/search").json()[0]['url'])
  if message.content.startswith('-catfact'):
    fact = get_fact()
    await message.channel.send(fact)

client.run('OTk0NDg3MDgyNzI4ODMzMDI0.GasXKw.Mow6s-874FqooRJJyqRdWY6BPs9pHGSU7_RAfs')

     