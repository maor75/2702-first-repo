from discordwebhook import Discord
web_Hook_url ="https://discord.com/api/webhooks/1128253115590770718/O_LB62rGTxm6hGwYe_GRX2_glWzuyFjWmXwWjWlcVPkNaSyT-oqOBlHW30DSZViY1Hwd"
discord = Discord(url=web_Hook_url)
input_message = input("enter a message:")
discord.post(content=input_message)
