from fastapi import FastAPI
from gpt_researcher import GPTResearcher

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "running"}

@app.post("/research")
async def research(query: str):
    researcher = GPTResearcher(query=query)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report}
```

**`requirements.txt`:**
```
fastapi
uvicorn[standard]
gpt-researcher
```

**`Procfile`:**
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
