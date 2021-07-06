## What is to the moon tracker :rocket:?
So let's be honest. Life was boring and I decided to make a very simple guide and script to make a crypto price tracker in telegram. It sends the price of your desired coin (like Bitcoin ₿) every ```x``` seconds to your telegram channel. It uses OKEx exchange ticker API endpoint.

## Why "to the moon"?
Well I guess it all started from Dogecoin:rocket: ... hmm

## How simple is it?
Very simple! you can set it up in less than 10 minutes. you only need:
  * A telegram bot 
  * A telegram public channel
  * This script (which is less than 100 lines I guess, if you delete the logging etc.)


### Steps


#### 1. Create your own telegram bot
In order to control and communicate with your telegram through python, you need a telegram bot. This bot will post automatically your desired content (in our case the coin price) to your telegram channel.

To create a telegram bot, you should contact https://t.me/botfather , which is the telegram official bots manager, and send ```/newbot``` command and follow the steps (choose a name, id etc.).

At the end, you'll get an API-KEY (or ```token```) which is really important to keep it secure and don't share it with anyone and a ```bot id``` which you choose. Later you'll use this ```token``` to send messages via python. 

------

#### 2. Create a telegram public channel
This is where your bot send the results constantly. It must be a public channel, which has an ID like ```@mychannel```. 

------

#### 3. Add your bot to the channel and make it admin
So from your channel description menu (or whatever it's called) > Members > Subscribers > Add subscribers, search your bot id. For example ```@myawesome_bot``` and add it to the group. Then you should accept it as an Admin (because bots can only be admin in a channel).

After that just give posting messages permission to the bot and approve it. Now your bot is in the channel and is able to post messages.

------

#### 4. Clone this project:
```bash
git clone https://github.com/mfiro/to-the-moon-tracker
cd to-the-moon-tracker
```

------

#### 5. Make a new virtual environment and install dependencies (It can be different for Windows):
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

------

#### 6. Make a copy of config_sample.ini and rename it to config.ini:

```bash
cd tracker
cp config_sample.ini config.ini
```

------

#### 7. Edit config.ini with your preferred text editor:

 * Change ```api_key``` under [TelegramAPI] section with your bot's ```token```
 * Change ```channel_id``` under [PriceTracker] and [PriceTracker_debug] section with your telegram ```channel id```
 * You can also change the coin to your desired coin like (ETH-USDT or XRP-USDT)
 * You can also change how frequent the updates you would like to be.

Notes:
  * You don't need ' ' or " " for strings in config.ini file.
------

#### 8. Run the code:
```bash
python tracker.py
```


