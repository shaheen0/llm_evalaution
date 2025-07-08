
#### 1. Clone the Repository

```bash
git clone <https://github.com/shaheen0/llm_evalaution.git>
cd <llm_evaluation>
```


```bash
pip install -r requirements.txt
```

#### 3. Create a `.env` File

In the root of your project folder, create a file named `.env` and add the following:

```
OPENAI_API_KEY=your_openai_api_key_here
LAUNCHDARKLY_SDK_KEY=your_launchdarkly_sdk_key_here
```

Replace the values with your actual API keys.

#### 4. Run the FastAPI App

Use Uvicorn to start the server:

```bash
uvicorn app:app --reload
```
OR

```bash
fastapi dev app.py
```