from fastapi import FastAPI # importing fast api.

app = FastAPI() 

@app.get("/customer")
def get_cutomer(customer_id: int):
    return{
        "customer_id": customer_id,
        "name":"ravi",
        "status":"active"
    }

    """
    now here we are having a code above.

    here the function expecting to the customer id. 
    so in the url if we give it the customer_id then it will return us the things we expects. so the url will look like.

    http://127.0.0.1:8000/customer?customer_id=101 # here "/customer" is our endpoint and "?customer_id=101" we are passing to the function.

    and this "?customer_id=101" is known as query.
    """

    """
    
    Output:

    {"customer_id":101,"name":"ravi","status":"active"}
    """