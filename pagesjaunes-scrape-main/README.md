# pagesjaunes-scrape

## Usage
- run script using `python main.py`

## Cli Arguments
Cli arguments are used for testing purposes. When using cli args output is writen to seperate xlsx sheet with corresponding name format

- **--region**
    - specify region to scrape
    - Usage `--region <region>`
    - eg: `python main.py --region Alsace` or `python main.py --region Alsace --cityStartsWith b`
    - output file: 
        - 'region_{region}.xlsx'
        - if --cityStartsWith is given: '{region}_city__{starts_with}.xlsx'
- **--cityStartsWith**
    - specify which city start letter to scrape.
    - Usage `--cityStartsWith <char>`
    - should be used together with `--region`
    - eg: `python main.py --region Alsace --cityStartsWith b`

- **--professionalUrl**
    - specify professionals url to scrape.
    - Usage `--professionalUrl <url>`
    - eg: `python main.py --professionalUrl https://www.pagesjaunes.fr/pros/08760073`
    - output file: 'output-{timestamp}.xlsx'

- **--citySlug**
    - specify url slug of the city to scrape.
    - Usage `--citySlug <slug>`
    - eg:- `python main.py --citySlug anzin-59`
    - output file: '{args.city_slug}_output-{timestamp}.xlsx'
- **--pageNos**
    - specify the page no under professional url to be scraped.
    - usage `--pageNos <page_nos>`
    - eg;- `python main.py --pageNos 4` or `python main.py --pageNos 4, 5, 6`

## NOTES:
- to change the scrape starting page number edit `self.start_scraping_at_page_no` variable (currently set to 2)
- To use proxy server (brightdata) uncomment lines 22-23

## Running Script in RDP
- Install python (python3.9 reccomended) and chrome in RDP
- Copy script folder to rdp
- open cmd cd to script folder and run `pip install -r requirements.txt` to install dependencies.
- run script by executing `python main.py` along with required cli args