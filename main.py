from fastapi import FastAPI

app = FastAPI()

@app.get("/connector/{num1}/{num2}")
async def your_endpoint(num1:int, num2: int):
    # Process the request and prepare the response
    sum = num1+num2
    response_body = f"sum of two number is: {sum}"
    return response_body
