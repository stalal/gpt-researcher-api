from fastapi import FastAPI
from gpt_researcher import GPTResearcher
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "GPT Researcher API is running"}

@app.post("/research")
async def research(query: str):
    # This uses the gpt-researcher package from PyPI
    researcher = GPTResearcher(query=query)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report, "query": query}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
```

**`requirements.txt`:**
```
fastapi
uvicorn
gpt-researcher
