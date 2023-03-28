# ML-model-API-deployment



## Steps:

### 1. Upload model and python file with FastAPI app



### 2. Create requirements.txt

run command 'pip freeze > requirements.txt' in terminal and upload it!


### 3. Create Procfile 

- crate new file named Procfile (without any extension, such as .txt)
- inside, add a line: 'web: uvicorn app:app --host=0.0.0.0 --port=${PORT:-5000}'
- make sure to replace app:app with the name of your FastAPI app file and the name of the FastAPI app instance

### 4. Create file runtime.txt (optional)

- inside you specify your python version (run: 'python --version' in terminal)
- example of the entry: python-3.9.16
