# pycurvert
A terminal-based currency converter

## About
Pycurvert is a terminal-based currency converter written in Python which leverages the API from [ExchangeRate-API](https://www.exchangerate-api.com/) to provide a fully functional currency conversion tool.
The user gets prompted for the required input parameters and is then presented with the final, converted value, which is calculated using the most recent conversion rates available.

## Instructions
> [!NOTE]
> For the application to work, a valid API-Key for [ExchangeRate-API](https://www.exchangerate-api.com/) is required. You can sign up for a free account and get one on their website.
> *This is not an affiliation of any kind, I simple decided to use their service for my application.*

1. Clone the pycurvert repository:
```
git clone https://github.com/nohouse-felix/pycurvert.git
```

2. Set the required Environment Variable on your machine before launching the application:
```
export API_KEY=<YOUR_API_KEY_HERE>
```

Alternatively, you can hardcode your API-Key into the source code by uncommenting the section below `API_KEY = os.getenv("CURRENCY_API_KEY")` and manually putting in your Key there, although this is not recommended.

3. Launch the application:
```
python3 pycurvert/src/main.py
```

*Happy converting!*
