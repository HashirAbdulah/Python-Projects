from instabot import Bot

bot = Bot()

bot.login(username = "", password = "")
bot.follow("any user profile name")
bot.unfollow("any user profile name")

bot.upload_photo("Path of the file ", caption=" ")

#Multiple messages:

messages = ["Hello", "This is Hashir Abdullah testing bot messages"]
for message in messages:
    bot.send_message("any user profile name", message)

bot.send_message("message",["user1","user2","user3",])


# More functions can be perfomed google them according to your need 