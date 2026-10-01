from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# this class is our form. here we are expecting our data which is coming to be in the specific datatype
class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employeement_years: int

@app.post("/predict")
def predict_loan(application: LoanApplication):
    """
    model logic will write here.
    """
    approved = (
        application.income > 50000 and
        application.employeement_years > 2 and 
        application.age >= 21
    )

    return {
        "applcation name": application.name,
        "loan_amount": application.loan_amount,
        "decision":"approved" if approved else "rejected",
        "review_income": application.income
    }