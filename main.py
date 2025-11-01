from fastapi import FastAPI
from gpt_researcher import GPTResearcher
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "GPT Researcher API is running"}

@app.post("/research")
async def research(query: str):
    researcher = GPTResearcher(query=query)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report, "query": query}

# This is important for Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
