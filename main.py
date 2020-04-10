import discord
codes = {
    'a': "Alpha",
    'b': "Bravo",
    'c': "Charlie",
    'd': "Delta",
    'e': "Echo",
    'f': "Foxtrot",
    'g': "Golf",
    'h': "Hotel",
    'i': "India",
    'j': "Juliet",
    'k': "Kilo",
    'l': "Lima",
    'm': "Mike",
    'n': "November",
    'o': "Oscar",
    'p': "Papa",
    'q': "Quebec",
    'r': "Romeo",
    's': "Sierra",
    't': "Tango",
    'u': "Uniform",
    'v': "Victor",
    'w': "Whisky",
    'x': "XRay",
    'y': "Yankee",
    'z': "Zulu",
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "nine"
}
relayed_message = []
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    encrypt = "!asd"
    if message.author == client.user:
        return

    if message.content.startswith(encrypt):
        p1 = Message(message.content, encrypt)
        p1.start()
        await message.delete()
        await message.channel.send(" ".join(relayed_message))
        del relayed_message[:]

class Message:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def start(self):
        self.split()

    def split(self):
        list = [ch for ch in str(self.message)]
        self.codeRetrieval(list)

    def codeRetrieval(self, characters):
        for items in characters:
            for letters in codes:
                if letters == items:
                    relayed_message.append(codes[letters])
        self.cleanList()

    def cleanList(self):
        n = len(self.key) - 1
        del relayed_message[:n]


client.run('')
