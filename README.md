# lingo
## A helper app to the language learning process.

- Vocab charts
- Sentence dependencies visualizer
- Translation and language detection
- Text to speech

## Setup
This project uses Google Translate API to perform language detection, which means it requires the setup of a Google Cloud project. Follow the steps in the [API documentation](https://cloud.google.com/translate/docs/setup) until you have a JSON file containing your service account credentials.

Lastly, run the following commands in your terminal, from the **same dir of the JSON file**:

```
git clone https://github.com/danplevs/lingo.git
cd lingo
mv ../ENTER_CREDENTIALS_FILE_NAME.json ./credentials/google-translate.json
```
We'll install depencies in a virtual environment, which have platform-specific commands. If you have conda installed, just use:
```
conda env create -f environment.yml
```
Otherwise, we'll use pip: 
### Windows (PowerShell)
```
python -m venv .
./Scripts/Activate.ps1
pip install -r requirements.txt
```
### POSIX (bash/zsh)
```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
```
## Launching
To launch the app, run in your terminal:
```
streamlit run ./src/app.py
```
## Related documentation
[venv](https://docs.python.org/3/library/venv.html)  
[Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)  
[pip](https://pip.pypa.io/en/stable/user_guide/)
