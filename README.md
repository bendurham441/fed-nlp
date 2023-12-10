# How the Fed Shapes Its Message

This is a repository containing code for my honors thesis analyzing the difference between the informational content of FOMC transcripts and speeches made by FOMC governors.

## Files

- `transcripts`: This folder contains the process for retrieving transcripts and speeches from the Federal Reserve website and creating the initial csv files
    - `get_speeches.ipynb`: This file outlines the web-scraping procedure which uses the Federal Reserve website's underlying API to get a list of speech links, and then uses BeautifulSoup to extract the date, title, speaker, and speech contents. I am not using this in my current iteration of the paper, but I am leaving it as I may use it later on to assess differences in conformity in speeches vs. transcripts.
    - `get_transcripts.ipynb`: This fetches all of the FOMC meeting transcripts (along with conference call transcripts, though I am not currently using these) in the PDF form made available on the [FOMC Historical Materials by Year](https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm) page and stores them in `transcripts/pdfs`.
    - `extract_transcripts.ipynb`: Given the transcript PDFs, this converts them into csv form in so-called "utterance" format, such that one observation corresponds to one "utterance" by a speaker. Note that there is almost always more than one utterance per speaker at a given meeting.
- `common_ngrams.ipynb`: Following Hansen, McMahon, and Prat,

## Instructions on how to reproduce the results

