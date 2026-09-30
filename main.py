from fastapi import FastAPI # importing fast api.

app = FastAPI() 

@app.get("/customer")
def get_cutomer(customer_id: int, customer_city: str):
    return{
        "customer_id": customer_id,
        "customer_city": customer_city,
        "name":"ravi",
        "status":"active"
    }
