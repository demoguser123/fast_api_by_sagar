# Phase 6 Building a Machine learning project. (just for demonstrating the fastAPI)

- We are having some of the business problem and we are solving it. 

- Company having 1000s of the agents. and every time if someone asks for the house price then for that it need to give the final price by making some call and doing some of the analysis.

- But that makes problem.
    1. speed matters if we take too much time to respond then the client might go away.
    2. human inconsistency. if the client is talking to the 2 agents. but it may possible that both agents from the same company will give us the different different price via their analysis.
    3. scale is also important. if company having 500 agents and coming 2000 queries from those agents but we have just 10 experts to tell the price.
   
- Now, we will have multiple data with multiple aspects and we will train model on top of it. 

1. Train the model.
2. Warp in the api ( fast api ).
3. 24 x 7 available.

### Getting the data and Inquiring about the data.

`explore.py`

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

df["Price"] = data.target
print("Shape", df.shape)
print(df.head())
print(df.describe())

```

```
(venv) slinux@Sandips-PC:~/projects/python_learning/fastapi_by_sagar/house prediction_api$ uv run explore.py
Shape (20640, 9)
   MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude  Price
0  8.3252      41.0  6.984127   1.023810       322.0  2.555556     37.88    -122.23  4.526
1  8.3014      21.0  6.238137   0.971880      2401.0  2.109842     37.86    -122.22  3.585
2  7.2574      52.0  8.288136   1.073446       496.0  2.802260     37.85    -122.24  3.521
3  5.6431      52.0  5.817352   1.073059       558.0  2.547945     37.85    -122.25  3.413
4  3.8462      52.0  6.281853   1.081081       565.0  2.181467     37.85    -122.25  3.422
             MedInc      HouseAge      AveRooms  ...      Latitude     Longitude         Price
count  20640.000000  20640.000000  20640.000000  ...  20640.000000  20640.000000  20640.000000
mean       3.870671     28.639486      5.429000  ...     35.631861   -119.569704      2.068558
std        1.899822     12.585558      2.474173  ...      2.135952      2.003532      1.153956
min        0.499900      1.000000      0.846154  ...     32.540000   -124.350000      0.149990
25%        2.563400     18.000000      4.440716  ...     33.930000   -121.800000      1.196000
50%        3.534800     29.000000      5.229129  ...     34.260000   -118.490000      1.797000
75%        4.743250     37.000000      6.052381  ...     37.710000   -118.010000      2.647250
max       15.000100     52.000000    141.909091  ...     41.950000   -114.310000      5.000010

[8 rows x 9 columns]
(venv) slinux@Sandips-PC:~/projects/python_learning/fastapi_by_sagar/house prediction_api$ 
```

- Here we have made our file inside the `house prediction` folder we can see all the codes and pass things in the `/docs` and can do the prediction and check it out.

<span style = color:#800020> First run the train.py which will have the files .joblib and then run the main.py </span>