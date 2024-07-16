Create a `.env` file like this:
```
OPENAI_API_KEY=asdf
KITTYCAD_API_TOKEN=asdf
```

Then setup your python and run the app:

```
python3.12 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

Open http://localhost:8001 to see the application