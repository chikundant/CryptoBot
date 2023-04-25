# Hi guys! I am Crypty


### Clone me 😎

``` git clone https://github.com/chikundant/CryptoBot.git ```


# Overview

Ctypty is a simple bot which can help you to fast control current coins value ✅ <br>
It built with modulse that can help you easy create a new one and add it to your project
Some strong sides of Telebot are:
- Contol default the most polular coins value
- Add your own coins
- Coins value mailing every hour


# Getting Started

To configure the bot you need to have an account on the Heroku and JawsDB MySQL plugin <br>
Notice that you need a pro account to use broadcast feature, because heroku does not allow you to use 2 threads in free account<br>

### Configuration

- Open ``` settings.py ```
```
DB_USERNAME = 'Your value here'
DB_PASSWORD = 'Your value here'
HOST_NAME = 'Your value here'
DB_NAME = 'Your value here'
```
- Write in ```APP_NAME``` your app name
```
APP_NAME = 'Your-bot-here.herokuapp.com'
```
- Put your bo token into ```BOT_API```
```
BOT_API = 'API from Bot Father'
```
- Put in the ```Database configuration``` your JawsDB MySQL plugin data
```
DB_USERNAME = 'Your value here'
DB_PASSWORD = 'Your value here'
HOST_NAME = 'Your value here'
DB_NAME = 'Your value here'
```

### Heroku deploy
- Open "Deploy tab"
- Choose "Deployment method"
- Upload your bot with Github or Heroku git
- Enjoy

### Run on the local computer 
- Go to config. py
- Set ```DEBUG = True```
- Set ```NOTIFICATIONS = True```

> Pay attention to the requirements.txt, heroku automatically installs the libraries, but sometimes you need install them by yourself on your host

# Testing
Bot cointest the 'tests' folder where you can find some db and coingecko api tests <br>

If you do not have MySql server you can comment the <br> ```DATABASE_URI = 'mysql://' + f'{DB_USERNAME}:{DB_PASSWORD}@{HOST_NAME}:{DB_PORT}/{DB_NAME}'``` <br>
line and use <br>```DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')```

> While testing on the db server will be automatically created test table to do not touch main data

To test functionality you can try:
- Add new coin which does not exist
- Try to register with incorrect data

