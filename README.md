# gscholar-scraper
Takes a keyword and returns papers sorted by amount of citations, a simple tool used for my final year project when scouting the most influential papers in a desired topic area.

Google has since made changes to how they handle webscrapers, rendering this tool much more inconsistent due to reCaptcha enforcement.

## Update 17/7/23

I have changed the implementation so that the tool works again (selenium in/requests out), manual reCaptcha solving is required for the time being. Working on dealing with 0 citation papers and multiple-page scraping w/o captcha checks every request.

Alternatively, use:
>www.scinapse.io
