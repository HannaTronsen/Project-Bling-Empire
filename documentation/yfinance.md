### Yfinance Calls & Responses

## Fast Info
```
    lazy-loading dict with keys = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']
```

## get_history_metadata()
```
   {
    "currency":"USD",
    "symbol":"AAPL",
    "exchangeName":"NMS",
    "instrumentType":"EQUITY",
    "firstTradeDate":"Timestamp(""1980-12-12 09:30:00-0500",
    "tz=""America/New_York"")",
    "regularMarketTime":"Timestamp(""2023-02-17 16:00:04-0500",
    "tz=""America/New_York"")",
    "gmtoffset":-18000,
    "timezone":"EST",
    "exchangeTimezoneName":"America/New_York",
    "regularMarketPrice":152.55,
    "chartPreviousClose":151.01,
    "previousClose":153.71,
    "scale":3,
    "priceHint":2,
    "currentTradingPeriod":{
        "pre":{
            "start":"Timestamp(""2023-02-17 04:00:00-0500",
            "tz=""America/New_York"")",
            "end":"Timestamp(""2023-02-17 09:30:00-0500",
            "tz=""America/New_York"")"
        },
        "regular":{
            "start":"Timestamp(""2023-02-17 09:30:00-0500",
            "tz=""America/New_York"")",
            "end":"Timestamp(""2023-02-17 16:00:00-0500",
            "tz=""America/New_York"")"
        },
        "post":{
            "start":"Timestamp(""2023-02-17 16:00:00-0500",
            "tz=""America/New_York"")",
            "end":"Timestamp(""2023-02-17 20:00:00-0500",
            "tz=""America/New_York"")"
        }
    }}
    'tradingPeriods':                                           pre_start                   pre_end                     start                       end                post_start                  post_end
    Date                                                                                                                                                                                 
    2023-02-13 00:00:00-05:00 2023-02-13 04:00:00-05:00 2023-02-13 09:30:00-05:00 2023-02-13 09:30:00-05:00 2023-02-13 16:00:00-05:00 2023-02-13 16:00:00-05:00 2023-02-13 20:00:00-05:00
    2023-02-14 00:00:00-05:00 2023-02-14 04:00:00-05:00 2023-02-14 09:30:00-05:00 2023-02-14 09:30:00-05:00 2023-02-14 16:00:00-05:00 2023-02-14 16:00:00-05:00 2023-02-14 20:00:00-05:00
    2023-02-15 00:00:00-05:00 2023-02-15 04:00:00-05:00 2023-02-15 09:30:00-05:00 2023-02-15 09:30:00-05:00 2023-02-15 16:00:00-05:00 2023-02-15 16:00:00-05:00 2023-02-15 20:00:00-05:00
    2023-02-16 00:00:00-05:00 2023-02-16 04:00:00-05:00 2023-02-16 09:30:00-05:00 2023-02-16 09:30:00-05:00 2023-02-16 16:00:00-05:00 2023-02-16 16:00:00-05:00 2023-02-16 20:00:00-05:00, 'dataGranularity': '1h', 'range': '1wk', 'validRanges': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']}
```

## Dividends
```
Date
1987-05-11 00:00:00-04:00    0.000536
1987-08-10 00:00:00-04:00    0.000536
1987-11-17 00:00:00-05:00    0.000714
1988-02-12 00:00:00-05:00    0.000714
1988-05-16 00:00:00-04:00    0.000714
                               ...   
2022-02-04 00:00:00-05:00    0.220000
2022-05-06 00:00:00-04:00    0.230000
2022-08-05 00:00:00-04:00    0.230000
2022-11-04 00:00:00-04:00    0.230000
2023-02-10 00:00:00-05:00    0.230000
Name: Dividends, Length: 78, dtype: float64
```

## get_dividends()
```
Date
1987-05-11 00:00:00-04:00    0.000536
1987-08-10 00:00:00-04:00    0.000536
1987-11-17 00:00:00-05:00    0.000714
1988-02-12 00:00:00-05:00    0.000714
1988-05-16 00:00:00-04:00    0.000714
                               ...   
2022-02-04 00:00:00-05:00    0.220000
2022-05-06 00:00:00-04:00    0.230000
2022-08-05 00:00:00-04:00    0.230000
2022-11-04 00:00:00-04:00    0.230000
2023-02-10 00:00:00-05:00    0.230000
```

## Splits
```
Date
1987-06-16 00:00:00-04:00    2.0
2000-06-21 00:00:00-04:00    2.0
2005-02-28 00:00:00-05:00    2.0
2014-06-09 00:00:00-04:00    7.0
2020-08-31 00:00:00-04:00    4.0
Name: Stock Splits, dtype: float64
```


## Income statement (#: .get_income_stmt() for more options) - Throwing error

## Balance sheet - Throwing error
    
## Cash flow statement - Throwing error
  
## Major holders
```
        0                                      1
0   0.07%        % of Shares Held by All Insider
1  61.36%       % of Shares Held by Institutions
2  61.40%        % of Float Held by Institutions
3    5709  Number of Institutions Holding Shares
```

## Institutional holders
```
                              Holder      Shares Date Reported   % Out         Value
0         Vanguard Group, Inc. (The)  1278250538    2022-12-30  0.0808  194997123472
1                     Blackrock Inc.  1029208322    2022-12-30  0.0650  157005732661
2            Berkshire Hathaway, Inc   895136175    2022-12-30  0.0566  136553026227
3           State Street Corporation   586857405    2022-12-30  0.0371   89525098923
4                           FMR, LLC   321162411    2022-12-30  0.0203   48993326778
5      Geode Capital Management, LLC   282749817    2022-12-30  0.0179   43133485446
6      Price (T.Rowe) Associates Inc   226281368    2022-12-30  0.0143   34519223378
7                     Morgan Stanley   208655323    2022-12-30  0.0132   31830370160
8         Northern Trust Corporation   174276229    2022-12-30  0.0110   26585839265
9  Norges Bank Investment Management   167374278    2022-12-30  0.0106   25532946619
```

## Mutual fund holders - To be verified

## Earnings - Throwing error

## Sustainability (Do I want to use it in my comapny evaluation?) - Throwing error

## Recomendations - Throwing error

## Recomencations summary - Throwing error

## analyst price target - Throwing error

## Revenue forcast - Throwing error

## Earnings forcast - Throwing error

## Earnings trend - Throwing error

## News
```
[
   {
      "uuid":"7e322d4a-15f3-3fd2-ab56-98900538adb8",
      "title":"Have $1,000? These 2 Stocks Could Be Bargain Buys for 2023 and Beyond",
      "publisher":"Motley Fool",
      "link":"https://finance.yahoo.com/m/7e322d4a-15f3-3fd2-ab56-98900538adb8/have-%241%2C000%3F-these-2-stocks.html",
      "providerPublishTime":1676903803,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/H2d1aYiGTpN1mIMQ9xzmkg--~B/aD0xNDAyO3c9MjEzNzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/motleyfool.com/4eaaa7f1dd6050b3de67e78ef1332d0c",
               "width":2137,
               "height":1402,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/hYviAQhZj3M3Jg1x58eN.w--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/motleyfool.com/4eaaa7f1dd6050b3de67e78ef1332d0c",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "TSM",
         "CRM",
         "AAPL"
      ]
   },
   {
      "uuid":"f88ee1c8-e143-3c4a-8055-f9d0e4a72fb0",
      "title":"Where Will Roku Stock Be in 1 Year?",
      "publisher":"Motley Fool",
      "link":"https://finance.yahoo.com/m/f88ee1c8-e143-3c4a-8055-f9d0e4a72fb0/where-will-roku-stock-be-in-1.html",
      "providerPublishTime":1676892360,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/UM9bbjmbPPwO.lxg5SyHUQ--~B/aD0xNDAzO3c9MjEzODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/motleyfool.com/aa2c3c2af870d69afc912c9e0cf56b4e",
               "width":2138,
               "height":1403,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/dTcsp4ML9Db05z36vAGwnQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/motleyfool.com/aa2c3c2af870d69afc912c9e0cf56b4e",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "ROKU",
         "AAPL",
         "GOOGL"
      ]
   },
   {
      "uuid":"5a58f4a6-3d9d-3f89-8e59-8c220e603de5",
      "title":"Apple iPhone Growth Could Lag Rivals for First Time Since 2019",
      "publisher":"Barrons.com",
      "link":"https://finance.yahoo.com/m/5a58f4a6-3d9d-3f89-8e59-8c220e603de5/apple-iphone-growth-could-lag.html",
      "providerPublishTime":1676892300,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/5afxuSR1bNXbdfjxo32OGg--~B/aD02NDA7dz0xMjgwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/Barrons.com/863edb5c791cdef89788b03d6ec8b9cb",
               "width":1280,
               "height":640,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/zqdy8F66w3OMwAbSTEwgkQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/Barrons.com/863edb5c791cdef89788b03d6ec8b9cb",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "AAPL"
      ]
   },
   {
      "uuid":"de461190-6159-30c0-9083-94b4fdaa07c1",
      "title":"Apple Watch faces potential import ban over patent dispute with Masimo",
      "publisher":"Fox Business",
      "link":"https://finance.yahoo.com/news/apple-watch-faces-potential-import-201330855.html",
      "providerPublishTime":1676837610,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/rG03MOZAcdHCQE1imFKDXw--~B/aD0yODAwO3c9NDE5ODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/fox_business_text_367/f91c57b3979e0a2125bd002fa338bbcc",
               "width":4198,
               "height":2800,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/TrAxKE1SAF.1fiyGl4qzNQ--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/fox_business_text_367/f91c57b3979e0a2125bd002fa338bbcc",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "MASI",
         "AAPL"
      ]
   },
   {
      "uuid":"93647ecf-54a1-4352-aa77-e910e62feb34",
      "title":"Shark Tank's Kevin O'Leary: ChatGPT is 'killing' Google's dominance",
      "publisher":"Yahoo Finance",
      "link":"https://finance.yahoo.com/news/shark-tanks-kevin-oleary-chatgpt-is-killing-googles-dominance-185504919.html",
      "providerPublishTime":1676832941,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/GqjO8dCGSu4QnImpGqUMtQ--~B/aD0yNjQzO3c9Mzg4MTthcHBpZD15dGFjaHlvbg--/https://s.yimg.com/os/creatr-uploaded-images/2023-02/e88f93f0-a60e-11ed-af0c-985185729923",
               "width":3881,
               "height":2643,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/4vCPsNu3BzN3pP80DDM2.A--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://s.yimg.com/os/creatr-uploaded-images/2023-02/e88f93f0-a60e-11ed-af0c-985185729923",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "AAPL",
         "GOOG",
         "GOOGL",
         "META",
         "MSFT",
         "AI"
      ]
   },
   {
      "uuid":"bca0e21b-e727-3d51-9cdc-58887fa0afc2",
      "title":"Meta to launch subscription service for Facebook and Instagram",
      "publisher":"Financial Times",
      "link":"https://finance.yahoo.com/m/bca0e21b-e727-3d51-9cdc-58887fa0afc2/meta-to-launch-subscription.html",
      "providerPublishTime":1676830886,
      "type":"STORY",
      "relatedTickers":[
         "META",
         "AAPL"
      ]
   },
   {
      "uuid":"a20f8850-0597-3c5d-8a79-05f300d81ff7",
      "title":"Is The Trade Desk Stock a Buy Now?",
      "publisher":"Motley Fool",
      "link":"https://finance.yahoo.com/m/a20f8850-0597-3c5d-8a79-05f300d81ff7/is-the-trade-desk-stock-a-buy.html",
      "providerPublishTime":1676819580,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/4FkUR2KbSEi63SKuNw2nkQ--~B/aD0xNDE0O3c9MjEyMTthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/motleyfool.com/8d8228c7823f73b047023a75ee3f5c22",
               "width":2121,
               "height":1414,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/uAGRDvp324s8UUhUL3LTAg--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/motleyfool.com/8d8228c7823f73b047023a75ee3f5c22",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "TTD",
         "GOOGL",
         "META",
         "AAPL"
      ]
   },
   {
      "uuid":"5aa89083-ff94-3c5a-9bf7-8aec74624675",
      "title":"10 Best Performing Warren Buffett Stocks in 2023",
      "publisher":"Insider Monkey",
      "link":"https://finance.yahoo.com/news/10-best-performing-warren-buffett-143853972.html",
      "providerPublishTime":1676817533,
      "type":"STORY",
      "thumbnail":{
         "resolutions":[
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/mixii8ffhCS9uT7xt_fT5w--~B/aD01NzE7dz01MDA7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/insidermonkey.com/ffb55fadeda2b2e4d1ba50e5e06977a0",
               "width":500,
               "height":571,
               "tag":"original"
            },
            {
               "url":"https://s.yimg.com/uu/api/res/1.2/.GE0urOSFVo9f8UgIFHMlg--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/insidermonkey.com/ffb55fadeda2b2e4d1ba50e5e06977a0",
               "width":140,
               "height":140,
               "tag":"140x140"
            }
         ]
      },
      "relatedTickers":[
         "AXP",
         "TSM",
         "AAPL",
         "NU",
         "FND"
      ]
   }
]
```
