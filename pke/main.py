from fastapi import FastAPI

from pke.core.database import Base, engine
import pke.models  # noqa: F401


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Knowledge Engine",
    description="Backend service for collecting and processing knowledge sources",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}