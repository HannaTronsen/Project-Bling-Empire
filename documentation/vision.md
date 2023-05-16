### Project Bling Empire

![image](https://m.media-amazon.com/images/M/MV5BMDJjYzY0YTEtNDJiOS00Yzk1LTgyZTctYmM0YTU3NzQwYmViXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX1000_.jpg)


This project is inspired firstly by my first stock assistant tool I made in 2020 and that is described on my [personal website](https://hannatronsen.herokuapp.com/projects)
but then later also by the netflix tv show named Bling Empire. My stock analysis tool was developed in an attempt to make picking stocks easier and less risk prone, but considering my lack
of coding experience back then, only a fool (like me) would actually trust the assistant;  Though I have to say that my stock assistant picked Kitron to be Oslo Børs number one stock pick,
and I have monitored Kitron's stock price shoot up to the moon while silently watching from the side line after taking profit too early in the run-up... 

![image](https://user-images.githubusercontent.com/85925436/235963425-47fb04dd-3e56-417e-8924-65e0f1ced4b0.png)

I bought around 17-18 NOK and now I just cry in my sleep 😭

## Reason for working on this project

- Fun to have a hobby project
- 99% of newly founded companies statistically go bankrupt within 5-10 years
- I read somewhere that investing could be compared with runing a business, but the overhead and amount of work required to run a succesful business is way more demanding
- Passive income for the win, get better at making money in your sleep instead of having sleepless nights worrying about business matters
- I thought I wanted to build a business, to prove myself and to add to the small number of feemale leeders in the top possitions, but why do all the work and risk neglecting the important things in life

- Plan B is to use this project as a launchingpad for aquiring a 9-5 job and to show at least what I can do with code

## Supported stock exchanges
    STANDARD_AND_POOR_500
    NORWAY
    GERMANY
    HONG_KONG
    UNITED_KINGDOM | They changed table format [NOT SUPPORTED]
    NETHERLAND
    FRANCE


## MVP - Stock Assistant V2 
- Periodically add more tickers [on-going]
- [X] Pick a suitable API for fetching stock ticker data
- [X] Write test to confirm that API working
- [X] Figure out what data I want to save and what stock indicators to emphasize when determening the value of a stock
- [X] Sort the key metrics for determening the value of a stock in decending order
- [ ] Create a common Stock Data class that will handle metrics and formulas related to yquery modules:
    - [X] General stock information
    - [X] Revenue data
    - [ ] Earnings data
    - [X] Debt data
    - [ ] Return on Investment (ROI) & Return on Invested Capital (ROIC)
    - [ ] Cash flow
    - [X] Gross profit margin
    - [X] Operating margin
    - [X] Price to earnings (P/E) ratio
    - [X] Price to book (P/B) ratio
    - [ ] Market share
    - [X] Enterprise value to EBITDA (EV/EBITDA) ratio
    - [X] Dividend yield
    - [C] Price to cash flow (P/CF) ratio
    - [ ] Insider trading
    - [ ] Recommendations
- [ ] Extend Stock Data class that will handle dataframe metrics and formulas reated to yqeruy financials
- [ ] Crunch the data by the formulas I write
- [ ] Export the data in a CSV file with possibility to sort the rows by column
- [ ] Refactor
- [ ] Have comprehensive test coverage

## Future vision

Make the CSV data into an interactive report that will only give you the most important information and the most interesting companies. In the report it would be good to also read about investing and to learn the theories applied to come up with the sorted stock list. 
    