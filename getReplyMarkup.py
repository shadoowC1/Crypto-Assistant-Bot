import json

def getReplyMarkup(command) :

    about_feyorra = json.dumps({"inline_keyboard" :[[{"text":"Feyorra" , "url" :"https://feyorra.com"}] , [{"text":"Introducing-Feyorra" , "url" :"https://feyorra.medium.com/feyorra-introduction-604822d2b9c3" }]]})

    locked_tokens = json.dumps({"inline_keyboard" :[[{"text":"Team Finance" , "url" :"https://team.finance/view-coin/0xe8E06a5613dC86D459bC8Fb989e173bB8b256072?name=Feyorra&symbol=FEY"}]]})

    latest = json.dumps({"inline_keyboard" :[[{"text":"Twitter" , "url" :"https://twitter.com/feyorraofficial"}]]})

    liquidity_mining = json.dumps({"inline_keyboard" :[[{"text":"ETH-FEY POOL" , "url" :"https://v2.info.uniswap.org/pair/0xb6e544c3e420154c2c663f14edad92737d7fbde5"}] , [{"text":"USDT-FEY POOL" , "url":"https://v2.info.uniswap.org/pair/0xdeea5c497b7557e8742f2707549e8b2f9f09594c"}] , [{"text":"Stake LP-TOKENS" , "url":"https://dapp.feyorra.com/farming"}] , [{"text" :"What are liquidity pools?" ,"url":"https://feyorra.medium.com/feyorra-fey-liquidity-mining-9a0e98582206"}]]})

    verify_stake =  json.dumps({"inline_keyboard" :[[{"text":"Pasino" , "url" :"https://pasino.com/?user_id=720"}]]})

    stake = json.dumps({"inline_keyboard" :[[{"text":"Decentralized staking ( recommended)" , "url" :"https://dapp.feyorra.com/stake"}] , [{"text":"Pooled staking" , "url":"https://faucetpay.io/fey/pooled-staking"}] , [{"text":"FEY-ETH STAKE ( BOUGHT+STAKE AUTOMATED)" , "url":"https://dapp.feyorra.com/eth-feyorra-staking"}] , [{"text" :"Token Disclaimer" , "url":"https://feyorra.com/page/disclaimer"}]]})

    exchanges = json.dumps({"inline_keyboard" :[[{ "text":"Uniswap ETH-FEY POOL (recommended)" , "url":"https://v2.info.uniswap.org/pair/0xb6e544c3e420154c2c663f14edad92737d7fbde5"}] ,[{"text":" Uniswap USDT-FEY POOL" , "url":"https://v2.info.uniswap.org/pair/0xdeea5c497b7557e8742f2707549e8b2f9f09594c"}] ,[{"text":"CoinTiger" , "url":"https://www.cointiger.com/en-us/#/trade_center?coin=fey_usdt"}] ,[{"text":"BitGlobal" , "url":"https://www.bitglobal.com/en-us/spot/trade?q=FEYUSDT"}],[{"text":"Bololex" , "url":"https://bololex.com/trading/sessions/market-view?symbol=FEY-TRX"}] , [{"text":"FaucetPay (3% fees)" , "url":"https://faucetpay.io/?r=396533"}] , [{"text":"How to Use Uniswap with Feyorra (FEY) ? " ,"url":"https://feyorra.medium.com/how-to-use-uniswap-with-feyorra-fey-ac517fac8146"}]]})

    contract = json.dumps({"inline_keyboard" :[[{"text":"Contract" , "url" :"https://etherscan.io/address/0xe8e06a5613dc86d459bc8fb989e173bb8b256072"}] , [{"text":"Contract audit" , "url":"https://johnwick.io/verify/52c49b381b1a26db127b03570655f2db"}] ,[{"text":"How to View Your Feyorra (FEY) Tokens in Metamask ? " , "url":"https://feyorra.medium.com/how-to-view-your-feyorra-fey-tokens-in-metamask-19e4efda8231"}]]})

    reply_markups = {"/about_feyorra":about_feyorra ,"/about_feyorra@FeyorraBot":about_feyorra , "/locked_tokens":locked_tokens , "/locked_tokens@FeyorraBot":locked_tokens , "/latest":latest , "/latest@FeyorraBot":latest , "/liquidity_mining":liquidity_mining , "/liquidity_mining@FeyorraBot":liquidity_mining , "/verify_stake":verify_stake , "/verify_stake@FeyorraBot":verify_stake , "/stake":stake , "/stake@FeyorraBot":stake , "/exchanges":exchanges , "/exchanges@FeyorraBot":exchanges , "/contract":contract , "/contract@FeyorraBot":contract }

    return reply_markups[command]
