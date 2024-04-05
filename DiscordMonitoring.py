from discord_webhook import DiscordWebhook
import json
def discord(dico1,dico2):
    """
    Fonction qui prend comme parametres les dictionnaires de monitoring et les envois sur un serveur Discord dédié
    INPUT: dico1,dico2
    OUTPUT: None
    """

    webhook_url = "https://discord.com/api/webhooks/1225715184438611980/3ShGtk7f_3eQFKVt5ubJoK9r1tJ9EmFW8Q4XS7yrAGtfGfyB0NQjFG2FgxmtjDmX9yIv"

    dico1.update(dico2)

    message = "\n".join([f"{cle} : {valeur}" for cle, valeur in dico1.items()])
    #objet DiscordWebhook avec l'URL du webhook
    webhook = DiscordWebhook(url=webhook_url, content=message)

    # Envoyer le message
    response = webhook.execute()
    return