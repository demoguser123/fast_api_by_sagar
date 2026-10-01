from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# here the client is sending the complete json modules with all the features.
class LoanApplication(BaseModel):
    age: int
    income: float
    loan_amount: float
    employeement_years: int

# function will receive that json module which is send above and process it and send it back.
@app.post("/predict")
def predict_loan(application: LoanApplication):

    # pretend this trining model

    if application.income > 50000 and application.employeement_years > 2:
        decision = "approved"
    else:
        decision = "rejected"

    return {
        "application_age": application.age, 
        "decision": decision
    }

