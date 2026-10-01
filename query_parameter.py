from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id": 101, "name": "Ravi", "city":"Bangaluru", "risk":"low"},
    {"id": 103, "name": "Om", "city":"Mumbai", "risk":"high"},
    {"id": 104, "name": "Prakash", "city":"Ahmedabad", "risk":"medium"},
    {"id": 105, "name": "Yash", "city":"Gandhinagar", "risk":"high"},
    {"id": 102, "name": "Gopal", "city":"Kerala", "risk":"low"},
]

@app.get("/customers")
def get_customer(city:str, risk:str):
    filtered = [
        c for c in all_customers
        if c["city"] == city and c ["risk"] == risk
    ]

    return {
        "city": city, 
        "risk": risk,
        "count": len(filtered),
        "results": filtered
    }