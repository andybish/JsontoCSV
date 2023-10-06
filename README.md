# JsontoCSV
Quick JSON to CSV converter in python

Set headers and filename manually. (Samples are commented out for reference)
Will convert filename.json to filename.csv.
Will no longer leave blank rows between data rows.
Will output total row count, number of each header field that were not found and replaced with blanks, 
number of each header field that was present but empty, and number that were skipped due to missing primary key.
Not at all optimised, if you have large JSONs, have a lot of RAM.
