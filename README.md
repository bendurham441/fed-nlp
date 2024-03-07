# Groupthink and Conformity in the FOMC in Unfavorable Economic Conditions

This is a repository containing code for my mathematical economics honors thesis at Gettysburg College investigating the potency of groupthink in the Federal Open Market Committee and how this groupthink might vary based on economic conditions.

## Files

- `data-collection/` contains the process for retrieving transcripts and speeches from the Federal Reserve website and creating the initial csv files
    - `get_speeches.ipynb`: This file outlines the web-scraping procedure which uses the Federal Reserve website's underlying API to get a list of speech links, and then uses BeautifulSoup to extract the date, title, speaker, and speech contents. I am not using this in my current iteration of the paper, but I am leaving it as I may use it later on to assess differences in conformity in speeches vs. transcripts.
    - `get_transcripts.ipynb`: This fetches all of the FOMC meeting transcripts (along with conference call transcripts, though I am not currently using these) in the PDF form made available on the [FOMC Historical Materials by Year](https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm) page and stores them in `transcripts/pdfs`.
    - `extract_transcripts.ipynb`: Given the transcript PDFs, this converts them into csv form in so-called "utterance" format, such that one observation corresponds to one "utterance" by a speaker. Note that there is almost always more than one utterance per speaker at a given meeting.
- `figures/` contains figures I use in various iterations of my paper.
- `fomc-membership/` includes my process for determining who is on the FOMC at any given time, and which of those members are voting members.
- `models` has the binary files for the Gensim dictionary of terms I use in my topic model and the binary files for my topic model.
- `ngrams/` contains details of my process of identifying bigrams and trigrams that should be treated as one entity. I use these to "enhance" utterances by appending bigrams and trigrams found in that utterance with a single word version so the topic model treates them as a single item.
    - `common_ngrams.ipynb`: In this, I 
- `conformity.ipynb` is my initial descriptive investigation of whether conformity, as measured by topic distribution similarity, increases during periods of economic stress (particularly recessions).
- `discipline.ipynb` is my initial investigation of so-called discipline effects in the FOMC.
- `dropbox_sync_csvs.ipynb` is a utility file to sync the working csvs to dropbox to allow me to work on them from another computer without having to generate them again.
- `grouped_cleaning.ipynb` removes utterance from non-specific speakers such as "SEVERAL" or "PARTICIPANT."
- `prepare.ipynb` prepares adds the ngram-enhancement, includes the TF-IDF threshold filtering, and combines all utterances from a given speaker at a meeting to create the final speaker-meeting observations that I use my topic model.
- `todo.md` contains various ideas I have on things I want to try.
- `topic_cyclicality.ipynb` ranks the LDA topics according to their differences in share of discussion during recessions versus all other times in order to get a measure of cyclicality.
- `topic_modelling.ipynb` creates the actual LDA topic model and stores it in the models folder.


## Note
I do not use version control to track changes to most of my working csv files. They can be very large, and also the files in this repository contain the code needed to replicate them anyway. I also do not track the transcript pdfs in this repository for similar reasons.

## Instructions on how to reproduce the results
1. Run `data-collection/get_transcripts.ipynb` to fetch the transcripts in PDF form and store them in `data-collection/pdfs`.
2. Run `data-collection/extract_transcripts.ipynb` to extract the speech from the transcripts in "utterance" form and store them in `working-csvs/raw_transcripts.csv`.
3. Run `transcript-subdiv` to extract only the economic situation round and the policy round.
4. Run `ngrams/common_ngrams.ipynb` to identify possible terminology bigrams and trigrams and store these in `ngrams/bigrams` and `ngrams/trigrams`, respectively.

