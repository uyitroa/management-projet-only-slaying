# management-projet-only-slaying

Brute force Management de projet QCM. 

The algo send bruteforce requests to the server and progressively ratio centrale answer correctly to each questions, starting from the first one.
Takes about ~4 minutes to get 16/20.
Time complexity O(n_note_desired * n_answers_per_questions)

## Requirements:

```
pip install -r requirements.txt
```


## Run

Modify `config.json` file to your edunao account (CS email and edunao password).

```
cd management-projet-only-slaying
python algo.py
```

Current max score: 16/20


### banana code btw
