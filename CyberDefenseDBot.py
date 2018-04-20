import discord
import asyncio
import json
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)



@client.event
async def on_message(message):
    
    if message.content.startswith("!"):
        if message.content[1:13] == "randomnumber":
            end = message.content.find("|")
            
            min = int(message.content[14:end])
            max = int(message.content[end+1:])

            num = random.randint(min,max)
    
            await client.send_message(message.channel, num )
  
        if message.content[1:] == "hi":
            await client.send_message(message.channel, "Hello! I hope you are having a wonderful day!")

        if message.content[1:] == "bye":
            await client.send_message(message.channel, "Goodbye! See you later!")

        if message.content[1:] == "whoRU":
            await client.send_message(message.channel, "I am the friendly assistant for this channel.  I am here to help.")

        if message.content[1:] == "howoldareyou":
            await client.send_message(message.channel, "I was initially programmed in April of 2018, so I am very young I think...")

    if message.content == "cheetopuff":
        await client.send_message(message.channel, "Did I hear my favorite food???")
    if message.content == "BambooSteak":
        await client.send_message(message.channel, "I'm a bot, not a mind reader Bamboo.")
    if message.content == "Exhillious":
        await client.send_message(message.channel, "*Oooh, that's nasty!*")
    if message.content == "Frenchtoast":
        await client.send_message(message.channel, "Best food ever created!")
    if message.content == "djpj86":
        await client.send_message(message.channel, "Onya bike. Tell your story walkin'")
    if message.content == "ForgottenNow":
        await client.send_message(message.channel, "I'm hungry for cheescake...")


        #check your own balance
        if message.content[1:] == "checkbal":
            user = str(message.author)
            
            if not os.path.isfile("balances1"):
                bal = [user,0,]
                with open("balances1","w") as balances:
                    balances.writelines(bal)
                
            else:
                with open("balances1", "r") as balance:
                    bal = balance


                if user in str(bal) == False:
                #inserts another user in the database
                    bal.append((user,0),0)
                        
                    with open("balances1", "w") as balances:
                        balances.writelines(bal)

            with open("balances1", "r") as balances:
                bal = balances.readlines()
                    
            index = bal.index(user)
            amount = bal[index + 1]

            output = user + " has " + str(amount) + " CyberCoins."
            await client.send_message(message.channel, output)

"""
        #insert money into balance
        if message.content.startswith("!changebal"):
            #if message.author == "Frenchtoast#8942":
                with open ("balances", "r") as bal:
                    bal = json.load(bal)
                    
                    end = message.content.find("|")
                    name = message.content[9:end]
                    amount = message.content[end+1:]
                    index = bal.index(message.author) + 1
                    
                with open ("balances", "r") as bal:
                    bal = json.load(bal)
                    bal.insert(index, amount)
                
                print(bal)

                await client.send_message(message.channel, "Balance changed successfully.")    
            


@client.event
async def on_message(message):
    if message.content == "code1":
        idCode = message.channel
        await client.send_message(message.channel, str(message.channel) + " " + str(type(idCode)))
    if message.content == "code2":
        member = message.author
        channel = member.channel.Channel
        await client.send_message(channel, "Hooray! It works!")

@client.event
async def on_member_join(member):
    server = member.server
    print(server)
    channel = get_channel(433393963391516672) #general discussions channel
    print(channel) 
    message = "Welcome to the server " + str(member) + "!"
    await client.send_message(channel, message)
    print("Sent message!")
"""    

client.run("NDMzNDIyNjE3NTMwMzM1MjMy.Da7qmA.LujQztR2onERgLMiE_kkJysKK_s")
