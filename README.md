# Fintual test

- [Test description](#test-description)
- [Solutions](#solutions)
  - [Random](#random)
    - [Requirements](#requirements)
    - [Run](#run)
  - [Fintual API](#fintual-api)
    - [Requirements](#requirements-1)
    - [Run](#run-1)
    - [Resources](#resources)

## Test description

Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.

**Bonus Track**: make the Profit method return the "annualized return" of the portfolio between the given dates.

## Solutions

### Random

The first idea that I had was a random based calculation, with some variables to generate similar numbers to a real portfolio, but I don't think that's the best idea without persisting the data throughout the dates. So, it's basically a random value based on an invented formula.

#### Requirements

- Python 3.6+

#### Run

    $ python ./random/main.py

### Fintual API

The second idea was with the Fintual API, I have used it before for a personal project, so I thought it would be a good idea to try it again for this test, and personally, I like that the numbers are actually realistic.

#### Requirements

- Python 3.6+
- `requests` module

#### Run

    $ python ./api/main.py

#### Resources

I used 2 resources, the API docs and a post from the news section of the Fintualist website, to get the asset ids for the request.

- [La API de Fintual](https://fintualist.com/chile/noticias/el-api-de-fintual/)
- [API Docs](https://fintual.cl/api-docs/index.html)
