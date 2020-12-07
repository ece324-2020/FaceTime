# FaceTime

## Build

`cd env/`

Start the virtual environment: `source bin/activate`

If any dependancies are not installed run: `pip install -r requirements.txt`

if you add more dependancies run: `pip freeze > requirements.txt` 

Once you're finished working with the virtual env run: `deactivate`

## Run

`baseline.ipynb` contains the code to run the baseline model

`hypertuning.ipynb` contains the code to run the binary models on particular actors

Set `desired=#` with the following lookup to train on that particular actor:

'Leonard': 1,
'Penny': 3,
'Raj': 4,
'Sheldon': 5,
'Wolowitz': 6

`onscreen.ipynb` contains the code to find the final onscreen time for each actor on an episode
