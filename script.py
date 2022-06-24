import requests

id = input("Enter channel id  : ")
token = input("Enter the token  : ")
message = input("Enter the message : ")

Payload = {
    'content': message

}

header = {
    'authorization' : token
}

spam = input("spam mod ( y / n )  : ")

if spam == "y" or spam == "Y":
    while True:
        r = requests.post("https://discord.com/api/v9/channels/" + id + "/messages" , data=Payload , headers=header)
else:
    r = requests.post("https://discord.com/api/v9/channels/" + id + "/messages" , data=Payload , headers=header)
