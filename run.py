import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        port=8000,
        host="0.0.0.0"
    )
