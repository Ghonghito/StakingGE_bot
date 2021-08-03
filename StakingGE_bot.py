#encoding: utf-8
import telebot
import time
import requests
from bs4 import BeautifulSoup
import logging
from telebot.types import Message
from telebot import types
from datetime import datetime
from pycoingecko import CoinGeckoAPI
from web3 import Web3, HTTPProvider, IPCProvider, eth

cg = CoinGeckoAPI()

bot_token = 'ბოტის ტოკენი @BotFather-დან.'

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(token=bot_token)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def cake_staking(eth_address, bsc_w3):

    #იღებს ლარის კურსს
    try:
        get_gel = requests.get("https://transferwise.com/gb/currency-converter/usd-to-gel-rate")
        get_gelsourcecode = BeautifulSoup(get_gel.content, 'html.parser')
        get_gel_string = get_gelsourcecode.find('span', class_="text-success").get_text()
        get_gel_string_float = float(get_gel_string)
    except Exception:
        get_gel_string_float = float(1)
    #

    cake_addr = '0x73feaa1eE314F8c655E354234017bE2193C9E24E'
    cake_abi = '[{"inputs":[{"internalType":"contract CakeToken","name":"_cake","type":"address"},{"internalType":"contract SyrupBar","name":"_syrup","type":"address"},{"internalType":"address","name":"_devaddr","type":"address"},{"internalType":"uint256","name":"_cakePerBlock","type":"uint256"},{"internalType":"uint256","name":"_startBlock","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"BONUS_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IBEP20","name":"_lpToken","type":"address"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cake","outputs":[{"internalType":"contract CakeToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cakePerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_devaddr","type":"address"}],"name":"dev","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"devaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"enterStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"leaveStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"contract IMigratorChef","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingCake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IBEP20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accCakePerShare","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigratorChef","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"syrup","outputs":[{"internalType":"contract SyrupBar","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"multiplierNumber","type":"uint256"}],"name":"updateMultiplier","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    cc = bsc_w3.eth.contract(cake_addr, abi=cake_abi)
    cake_staked = cc.functions.userInfo(0, eth_address).call()[0]
    staked_cake = float(bsc_w3.fromWei(cake_staked, 'ether'))

    if staked_cake > 0:
        token_id = 'pancakeswap-token'
        coin_name = ' CAKE'
        pending_cake = cc.functions.pendingCake(0, eth_address).call() / 1000000000000000000
        staked_cake = float(bsc_w3.fromWei(cake_staked, 'ether'))
        totalstakedcake = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82&address=0x73feaa1ee314f8c655e354234017be2193c9e24e&tag=latest"
        response = requests.get(totalstakedcake)
        qeiqebi = response.json()
        cakepool = (int(qeiqebi["result"]) / 1000000000000000000)
        cakepool = int("{0:.0f}".format(cakepool))
        coin_list = [token_id, 'binancecoin', 'bitcoin', 'ethereum', 'pancakeswap-token']
        coin_list_price = []
        for coinfasi in coin_list:
            coin_price = cg.get_price(ids=coinfasi, vs_currencies='usd')
            coin_fasi = coin_price[coinfasi]['usd']
            coin_list_price.append(coin_fasi)
        pending_usd = coin_list_price[0] * pending_cake
        pending_gel = get_gel_string_float * pending_usd
        pending_bnb = pending_usd / coin_list_price[1]
        pending_btc = pending_usd / coin_list_price[2]
        pending_eth = pending_usd / coin_list_price[3]
        staked_usd = coin_list_price[0] * staked_cake 
        staked_gel = staked_usd * get_gel_string_float
        staked_bnb = staked_usd / coin_list_price[1]
        staked_btc = staked_usd / coin_list_price[2]
        staked_eth = staked_usd / coin_list_price[3]
        stakingunitpercent = '{:.15f}'.format(1 / cakepool * 100)
        totaldailyrewards = 288000
        stakingunitearns = float(stakingunitpercent) / 100 * totaldailyrewards
        ##########################################################################
        yourdailyreward = stakingunitearns * staked_cake
        dailyreward_price = yourdailyreward * float(coin_list_price[0])
        weekly_cake_reward = yourdailyreward * 7
        weekly_cake_reward_price = weekly_cake_reward * float(coin_list_price[0])
        apy = yourdailyreward / staked_cake * 100 * 365
        monthofcompounding = yourdailyreward * 30
        twomonthofcompunding = yourdailyreward * 60
        threemonthofcompunding = yourdailyreward * 90
        twodayreward = yourdailyreward * 2
        threedayreward = yourdailyreward * 3
        twodayreward_price = twodayreward * float(coin_list_price[0])
        threedayreward_price = threedayreward  * float(coin_list_price[0])
        ##########################################################################
        monthofcompoundingprice = float(coin_list_price[0]) * float(monthofcompounding) 
        twomonthofcompundingprice = float(coin_list_price[0]) * float(twomonthofcompunding)
        threemonthofcompundingprice = float(coin_list_price[0]) * float(threemonthofcompunding)
        info = "🔰 *CAKE Staking* (" + '{0:,.2f}'.format(float(apy)) + "%) 🔰" + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "🟢 დაგროვებული: " + '{0:,.8f}'.format(float(pending_cake)) + " CAKE" + "\n" + \
            "▶️ 1 დღეში: " + '{0:,.2f}'.format(float(yourdailyreward)) + " CAKE ($" + '{0:,.2f}'.format(float(dailyreward_price)) + ")" + "\n" + \
            "▶️ 2 დღეში: " + '{0:,.2f}'.format(float(twodayreward)) + " CAKE ($" + '{0:,.2f}'.format(float(twodayreward_price)) + ")" + "\n" + \
            "▶️ 3 დღეში: " + '{0:,.2f}'.format(float(threedayreward)) + " CAKE ($" + '{0:,.2f}'.format(float(threedayreward_price)) + ")" + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "▶️ 1 კვირაში: " + '{0:,.2f}'.format(float(weekly_cake_reward)) + " CAKE ($" + '{0:,.2f}'.format(float(weekly_cake_reward_price)) + ")" + "\n" + \
            "▶️ 1 თვეში: " + '{0:,.2f}'.format(float(monthofcompounding)) + " CAKE ($" + '{0:,.2f}'.format(float(monthofcompoundingprice)) + ")" + "\n" + \
            "▶️ 2 თვეში: " + '{0:,.2f}'.format(float(twomonthofcompunding)) + " CAKE ($" + '{0:,.2f}'.format(float(twomonthofcompundingprice)) + ")" + "\n" + \
            "▶️ 3 თვეში: " + '{0:,.2f}'.format(float(threemonthofcompunding)) + " CAKE ($" + '{0:,.2f}'.format(float(threemonthofcompundingprice)) + ")" + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "▶️ ღირებულება: ~$" + '{0:,.2f}'.format(float(pending_usd)) + " | ~₾" + '{0:,.2f}'.format(float(pending_gel)) + "\n" + \
            "🔸 BNB: " + '{0:,.8f}'.format(float(pending_bnb)) + "\n" + \
            "🔸 BTC: " + '{0:,.8f}'.format(float(pending_btc)) + "\n" + \
            "🔸 ETH: " + '{0:,.8f}'.format(float(pending_eth)) + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "🥞 დასტეიკებული CAKE: " + '{0:,.8f}'.format(float(staked_cake)) + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "▶️ ღირებულება: ~$" + '{0:,.2f}'.format(float(staked_usd)) + " | ~₾" + '{0:,.2f}'.format(float(staked_gel)) + "\n" + \
            "🔸 BNB: " + '{0:,.8f}'.format(float(staked_bnb)) + "\n" + \
            "🔸 BTC: " + '{0:,.8f}'.format(float(staked_btc)) + "\n" + \
            "🔸 ETH: " + '{0:,.8f}'.format(float(staked_eth)) + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "🔹 1 CAKE = $" + '{0:,.4f}'.format(float(coin_list_price[0])) + "\n" + "\n"
        return info

    else:
        pass


def cake_compounding(eth_address, bsc_w3):

    #იღებს ლარის კურსს
    try:
        get_gel = requests.get("https://transferwise.com/gb/currency-converter/usd-to-gel-rate")
        get_gelsourcecode = BeautifulSoup(get_gel.content, 'html.parser')
        get_gel_string = get_gelsourcecode.find('span', class_="text-success").get_text()
        get_gel_string_float = float(get_gel_string)
    except Exception:
        get_gel_string_float = float(1)
    #

    #Yield Watch-დან იღებს ინფორმაციას CAKE Compounding Pool-ის შესახებ 
    yw_url = "https://www.yieldwatch.net/api/all/" + eth_address + "?platforms=pancake"
    response = requests.get(yw_url)
    stats = response.json()
    ##
    
    try:
        stcake = stats['result']['PancakeSwap']['vaults']['vaults'][0]['depositedTokens']
        if stcake > 0:
            cake_vault_name = stats['result']['PancakeSwap']['vaults']['vaults'][0]['name']
            depositedTokens = stats['result']['PancakeSwap']['vaults']['vaults'][0]['depositedTokens']
            priceInUSDDepositToken = stats['result']['PancakeSwap']['vaults']['vaults'][0]['priceInUSDDepositToken']
            currentTokens = stats['result']['PancakeSwap']['vaults']['vaults'][0]['currentTokens']

            dagrovebuli_cake = float(currentTokens) - float(depositedTokens)

            try:
                get_gel = requests.get("https://transferwise.com/gb/currency-converter/usd-to-gel-rate")
                get_gelsourcecode = BeautifulSoup(get_gel.content, 'html.parser')
                get_gel_string = get_gelsourcecode.find('span', class_="text-success").get_text()
                get_gel_string_float = float(get_gel_string)
            except Exception as r:
                get_gel_string_float = float(1)

            coin_list = ['pancakeswap-token', 'binancecoin', 'bitcoin', 'ethereum', 'pancakeswap-token']
            coin_list_price = []
            for coinfasi in coin_list:
                coin_price = cg.get_price(ids=coinfasi, vs_currencies='usd')
                coin_fasi = coin_price[coinfasi]['usd']
                coin_list_price.append(coin_fasi)

            pending_usd = coin_list_price[0] * dagrovebuli_cake
            pending_gel = get_gel_string_float * pending_usd
            pending_bnb = pending_usd / coin_list_price[1]
            pending_btc = pending_usd / coin_list_price[2]
            pending_eth = pending_usd / coin_list_price[3]
            staked_usd = coin_list_price[0] * depositedTokens 
            staked_gel = staked_usd * get_gel_string_float
            staked_bnb = staked_usd / coin_list_price[1]
            staked_btc = staked_usd / coin_list_price[2]
            staked_eth = staked_usd / coin_list_price[3]
            
            totalstakedcake = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82&address=0x73feaa1ee314f8c655e354234017be2193c9e24e&tag=latest"
            response = requests.get(totalstakedcake)
            qeiqebi = response.json()
            cakepool = (int(qeiqebi["result"]) / 1000000000000000000)
            cakepool = int("{0:.0f}".format(cakepool))
            
            totaldailyrewards = 288000
            stakingunitpercent = '{:.15f}'.format(1 / cakepool * 100)
            stakingunitearns = float(stakingunitpercent) / 100 * totaldailyrewards    
            yourdailyreward = stakingunitearns * cakepool
            apy = yourdailyreward / currentTokens * 100 * 365
            yourdailyreward = stakingunitearns * currentTokens
            twodayreward = yourdailyreward * 2
            threedayreward = yourdailyreward * 3
            monthofcompounding = yourdailyreward * 30
            twomonthofcompunding = yourdailyreward * 60
            threemonthofcompunding = yourdailyreward * 90
            dailyreward_price = yourdailyreward * float(coin_list_price[0])
            twodayreward_price = twodayreward * float(coin_list_price[0])
            threedayreward_price = threedayreward  * float(coin_list_price[0])
            monthofcompoundingprice = float(coin_list_price[0]) * float(monthofcompounding) 
            twomonthofcompundingprice = float(coin_list_price[0]) * float(twomonthofcompunding)
            threemonthofcompundingprice = float(coin_list_price[0]) * float(threemonthofcompunding)
            weekly_cake_reward = yourdailyreward * 7
            weekly_cake_reward_price = weekly_cake_reward * float(coin_list_price[0])

            info = "🔄🥞 AUTO CAKE 🥞🔄"  + "\n"  + "\n" + \
                "🟢 დაგროვებული CAKE: " + '{0:,.5f}'.format(float(dagrovebuli_cake))  + "\n" + \
                "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
                "▶️ 1 დღეში: " + '{0:,.4f}'.format(float(yourdailyreward)) + " CAKE ($" + '{0:,.2f}'.format(float(dailyreward_price)) + ")" + "\n" + \
                "▶️ 2 დღეში: " + '{0:,.4f}'.format(float(twodayreward)) + " CAKE ($" + '{0:,.2f}'.format(float(twodayreward_price)) + ")" + "\n" + \
                "▶️ 3 დღეში: " + '{0:,.4f}'.format(float(threedayreward)) + " CAKE ($" + '{0:,.2f}'.format(float(threedayreward_price)) + ")" + "\n" + \
                "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
                "▶️ 1 კვირაში: " + '{0:,.4f}'.format(float(weekly_cake_reward)) + " CAKE ($" + '{0:,.2f}'.format(float(weekly_cake_reward_price)) + ")" + "\n" + \
                "▶️ 1 თვეში: " + '{0:,.4f}'.format(float(monthofcompounding)) + " CAKE ($" + '{0:,.2f}'.format(float(monthofcompoundingprice)) + ")" + "\n" + \
                "▶️ 2 თვეში: " + '{0:,.4f}'.format(float(twomonthofcompunding)) + " CAKE ($" + '{0:,.2f}'.format(float(twomonthofcompundingprice)) + ")" + "\n" + \
                "▶️ 3 თვეში: " + '{0:,.4f}'.format(float(threemonthofcompunding)) + " CAKE ($" + '{0:,.2f}'.format(float(threemonthofcompundingprice)) + ")" + "\n" + \
                "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
                "▶️ ღირებულება: ~$" + '{0:,.2f}'.format(float(pending_usd)) + " | ~₾" + '{0:,.2f}'.format(float(pending_gel)) + "\n" + \
                "🔸 BNB: " + '{0:,.8f}'.format(float(pending_bnb)) + "\n" + \
                "🔸 BTC: " + '{0:,.8f}'.format(float(pending_btc)) + "\n" + \
                "🔸 ETH: " + '{0:,.8f}'.format(float(pending_eth)) + "\n" + \
                "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
                "🥞 დასტეიკებული CAKE: " + '{0:,.8f}'.format(float(currentTokens)) + "\n" + \
                "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
                "▶️ ღირებულება: ~$" + '{0:,.2f}'.format(float(staked_usd)) + " | ~₾" + '{0:,.2f}'.format(float(staked_gel)) + "\n" + \
                "🔸 BNB: " + '{0:,.8f}'.format(float(staked_bnb)) + "\n" + \
                "🔸 BTC: " + '{0:,.8f}'.format(float(staked_btc)) + "\n" + \
                "🔸 ETH: " + '{0:,.8f}'.format(float(staked_eth)) + "\n" + \
                "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
                "🔹 1 CAKE = $" + '{0:,.4f}'.format(float(coin_list_price[0])) + "\n" + "\n" 
            return info
        else:
            pass
    except IndexError:
        pass        


def cherry_staking(eth_address, okex_w3):
    try:

        cherry_address = '0x9Ab8BCf67fE8d8D2aD27D42Ec2A0fD5C206DAE60'
        cherry_abi = '[{"constant":false,"inputs":[{"indexed":false,"internalType":"contract IBEP20","name":"_syrup","type":"address"},{"indexed":false,"internalType":"contract IBEP20","name":"_rewardToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"_rewardPerBlock","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_startBlock","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_bonusEndBlock","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","payable":false,"type":"event"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","payable":false,"type":"event"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","payable":false,"type":"event"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","payable":false,"type":"event"},{"constant":false,"inputs":[],"name":"BONUS_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"bonusEndBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IBEP20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accChePerShare","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"rewardPerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"rewardToken","outputs":[{"internalType":"contract IBEP20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"startBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"syrup","outputs":[{"internalType":"contract IBEP20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"totalDeposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"stopReward","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_from","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"multiplierNumber","type":"uint256"}],"name":"updateMultiplier","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"address","name":"_user","type":"address"}],"name":"pendingReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"massUpdatePools","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"emergencyWithdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"emergencyRewardWithdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
        cc = okex_w3.eth.contract(cherry_address, abi=cherry_abi)
        staked_cherry = cc.functions.userInfo(eth_address).call()
        pending_cherry = cc.functions.pendingReward(eth_address).call() / 1000000000000000000
        staked_cherry = staked_cherry[0] / 1000000000000000000
        #APY-ის გამოთვლა
        total_deposit = cc.functions.totalDeposit().call() / 1000000000000000000
        stakingunitpercent = '{:.15f}'.format(1 / total_deposit * 100)
        totaldailyrewards = 430000
        stakingunitearns = float(stakingunitpercent) / 100 * totaldailyrewards
        yourdailyreward = stakingunitearns * staked_cherry
        apy = yourdailyreward / staked_cherry * 100 * 365
        # END

        #გამოთვლები
        daily_reward = staked_cherry * apy / 100 / 365
        two_day_reward = daily_reward * 2
        three_day_reward = daily_reward * 3
        weekly_cake_reward = daily_reward * 7
        one_month = daily_reward * 30
        two_month = daily_reward * 60
        three_month = daily_reward * 90

        info = "🔰 *CHERRY Staking* (" + '{0:,.2f}'.format(float(apy)) + "%) 🔰" + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "🟢 დაგროვებული: " + '{0:,.3f}'.format(float(pending_cherry)) + " CHE" + "\n" + \
            "▶️ 1 დღეში: " + '{0:,.2f}'.format(float(daily_reward)) + " CHE" + "\n" + \
            "▶️ 2 დღეში: " + '{0:,.2f}'.format(float(two_day_reward)) + " CHE" + "\n" + \
            "▶️ 3 დღეში: " + '{0:,.2f}'.format(float(three_day_reward)) + " CHE" + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "▶️ 1 კვირაში: " + '{0:,.2f}'.format(float(weekly_cake_reward)) + " CHE" + "\n" + \
            "▶️ 1 თვეში: " + '{0:,.2f}'.format(float(one_month)) + " CHE" + "\n" + \
            "▶️ 2 თვეში: " + '{0:,.2f}'.format(float(two_month)) + " CHE" + "\n" + \
            "▶️ 3 თვეში: " + '{0:,.2f}'.format(float(three_month)) + " CHE" + "\n" + \
            "`- - - - - - - - - - - - - - - - - -`" + "\n" + \
            "🍒 დასტეიკებული CHERRY: " + '{0:,.3f}'.format(float(staked_cherry))
        return info
    except Exception:
        pass


@bot.message_handler(func=lambda message: True)
def misamartis_migeba(message):
    cid = message.chat.id
    eth_address = Web3.toChecksumAddress(message.text)

    #####უკავშირდება BSC-ქსელს
    bsc_w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
    print("BSC Connected: " + str(bsc_w3.isConnected))

    cake_addr = '0x73feaa1eE314F8c655E354234017bE2193C9E24E'
    cake_abi = '[{"inputs":[{"internalType":"contract CakeToken","name":"_cake","type":"address"},{"internalType":"contract SyrupBar","name":"_syrup","type":"address"},{"internalType":"address","name":"_devaddr","type":"address"},{"internalType":"uint256","name":"_cakePerBlock","type":"uint256"},{"internalType":"uint256","name":"_startBlock","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"BONUS_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IBEP20","name":"_lpToken","type":"address"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cake","outputs":[{"internalType":"contract CakeToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cakePerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_devaddr","type":"address"}],"name":"dev","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"devaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"enterStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"leaveStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"contract IMigratorChef","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingCake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IBEP20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accCakePerShare","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigratorChef","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"syrup","outputs":[{"internalType":"contract SyrupBar","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"multiplierNumber","type":"uint256"}],"name":"updateMultiplier","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    cc = bsc_w3.eth.contract(cake_addr, abi=cake_abi)
    cake_staked = cc.functions.userInfo(0, eth_address).call()[0]
    staked_cake = float(bsc_w3.fromWei(cake_staked, 'ether'))

    if staked_cake > 0:
        bot.send_message(cid, cake_staking(eth_address, bsc_w3), parse_mode='Markdown')
    else:
        pass


    #####უკავშირდება OKExCHAIN-ქსელს
    okex_w3 = Web3(Web3.HTTPProvider('https://exchainrpc.okex.org'))
    print("OEC Connected: " + str(okex_w3.isConnected))
    #####


    cherry_address = '0x9Ab8BCf67fE8d8D2aD27D42Ec2A0fD5C206DAE60'
    cherry_abi = '[{"constant":false,"inputs":[{"indexed":false,"internalType":"contract IBEP20","name":"_syrup","type":"address"},{"indexed":false,"internalType":"contract IBEP20","name":"_rewardToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"_rewardPerBlock","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_startBlock","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_bonusEndBlock","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","payable":false,"type":"event"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","payable":false,"type":"event"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","payable":false,"type":"event"},{"constant":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","payable":false,"type":"event"},{"constant":false,"inputs":[],"name":"BONUS_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"bonusEndBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IBEP20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accChePerShare","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"rewardPerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"rewardToken","outputs":[{"internalType":"contract IBEP20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"startBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"syrup","outputs":[{"internalType":"contract IBEP20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"totalDeposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"stopReward","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_from","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"multiplierNumber","type":"uint256"}],"name":"updateMultiplier","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"address","name":"_user","type":"address"}],"name":"pendingReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"massUpdatePools","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"emergencyWithdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"emergencyRewardWithdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
    cc = okex_w3.eth.contract(cherry_address, abi=cherry_abi)
    staked_cherry = cc.functions.userInfo(eth_address).call()
    staked_cherry = staked_cherry[0] / 1000000000000000000

    if staked_cherry > 0:
        bot.send_message(cid, cherry_staking(eth_address, okex_w3), parse_mode='Markdown')
    else:
        pass

    #####Yield Watch-დან იღებს ინფორმაციას CAKE Compounding Pool-ის შესახებ 
    yw_url = "https://www.yieldwatch.net/api/all/" + eth_address + "?platforms=pancake"
    response = requests.get(yw_url)
    stats = response.json()
    #####

    try:
        stcake = stats['result']['PancakeSwap']['vaults']['vaults'][0]['depositedTokens']

        if stcake > 0:
            bot.send_message(cid, cake_compounding(eth_address, bsc_w3), parse_mode='Markdown')
        else:
            pass
    except Exception:
        pass


while True:
    try:
        bot.polling()
        break
    except Exception:
        time.sleep(30)