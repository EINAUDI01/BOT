
import discord

#importation du module commands depuis discord.ext
#le module contient la classe qui va permetre d'instancier l'objet bot
#from discord.ext import commands

default_intents = discord.Intents.default()
default_intents.members = True
#On va ensuite créer un client qui ici est le bot
client = discord.Client(intents=default_intents)
#Avec le paramètre, command_prefix, on indique que les commandes 
#commencent par un point d'exclamation
#bot = commands.Bot(command_prefix="!")

#Il existe une dizaine d'évènements
#Pour envoyer un message lorsque le bot est en ligne
@client.event
#async permet de créer corotine
async def on_ready():
    print("Le bot est prêt !")
    
#Cette fonction va permettre de réagir à un message envoyé dans le serveur 
#Pour cela, on utilise l'évènement on_message
#On récupère le message avec la variable message à l'entrée de la fonction
@client.event
async def on_message(message):
    #Avec la méthode "lower" on convertit les caractères du message en miniscule
    #Ainsi, peu importe la manière dont est écrit ping, le code va fonctionner
    if message.content.lower() == "ping":
        #await permet de s'assurer que les choses vont se dérouler dans le bon ordre
        await message.channel.send("pong")

#Souhaiter la bienvenue aux nouveaux venus sur le serveur
@client.event
async def on_member_join(member):
    #Déclarer la variable general-channel
    #Dire que cette variable est de type TextChannel
    general_channel: discord.TextChannel = client.get_channel(958698262842445836)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name}!")

#Commande qui permet de supprimer des message du serveur
@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
#Créer des commandes
#Le nom de la commande créée ici est donc del
#Ne pas oublier qu'on a défini que la commande fonctionne précédée de !
#A la fonction delete, on passe en paramètre ctx et number
#ctx permet de récupérer des infos sur le serveur dans lequel la commande a été utilisée
#Avec ctx.channel par exemple, on récupère le salon dans lequel la commande a été tapée
#number de type int permet de récupérer le nombre qui a été tapé à la suite de del 
#@bot.command(name="del")
#async def delete(ctx, number: int):
    #messages = await ctx.channel.history(limit=number + 1).flatten() 
    #for each_message in messages:
        #await each_message.delete()
    
#Avec la méthode run, on connecte le bot
#Entre guillemet, c'est le token de mon bot
#On démarre le bot
client.run("OTU4Njk0OTk5NTY0ODgxOTIw.YkRESw.kbZ53omhvBoJk3dVOmx9ZmZLNL8")
