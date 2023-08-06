
![Logo](assets/yoo-telegram.png)


# yoo-Telegram

The python package that allows you simple communication with your telegram app.


## Installation

```bash
pip install yoo-telegram
```
    
## Usage 

`BOT_TOKEN` is required—more info in the Bot creation section. 
### Basic setup

Import and init Notifier object with your telegram bot token.
```python
from yoo_telegram import Notifier

client = Notifier("<BOT_TOKEN>")
```

Send a message to your telegram account id, which connects to your telegram bot.
```python
client.sendMessage("<RECIVER_ID>","<MESSAGE>")
```

### Advanced setup

Import and init Notifier object with your telegram bot token and create a dictionary of possible users.
```python
from yoo_telegram import Notifier

members = {
    "me" : "<RECIVER_ID>"
}

client = Notifier("<BOT_TOKEN>",members)
```
Notifier is able to send message to accounts by their aliases. 
```python
client.sendMessage("me","<MESSAGE>")
```

### Finding user id 

When your telegram account establishes communication with your telegram bot it is possible to get all chat ids by the following functionality.

```python
client.printChatIds()
```
or API Call
```
https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
```

### Print all members of notifier 

```python
client.printMembers()
```
## Bot creation

Tutorial how to create your own bot!

[Official telegram tutorial](https://core.telegram.org/bots#6-botfather)


## Deployment

Build package.
```python
python3 setup.py sdist bdist_wheel
```

Deploy package.
```python
twine upload dist/*
```


## Authors

- [@williambrach](https://github.com/williambrach)

