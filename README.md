**Current Files**
- project3.py: the program you want to run, handles commands and btree logic
- test.idx: provided idx file
- input.csv: example input csv file with a couple example lines
- forTesting directory: assorted .idx and .csv files that were useful for testing the program
- devlog.md: my devlog

**How to Run**

Start every command with `python3 project3.py` and then add the commands and args afterwards. Format specified in project specifications or through error messages provided.

These are all examples of valid commands:
```
python3 project3.py create test.idx
python3 project3.py insert test.idx 15 100
python3 project3.py search test.idx 15 
python3 project3.py load test.idx input.csv
python3 project3.py print test.idx
python3 project3.py extract test.idx output.csv
```

Obligatory note: was unable to test on cs1/cs2 machines, please let me know if any compatibility issues arise.


