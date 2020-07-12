# Racing-Cars

## Context

CrioLand is famous for it’s racing events. Every year the finale of racing events is organised. This year due to the pandemic, the event was cancelled. But the governor of CrioLand decided to have a virtual contest. The winner of the contest is the one with the fastest car.

Each team has some brands of cars already present in their garage. Each team has a maximum amount of funds that they can spend. Each car will have certain spare parts that can be attached to the car. These spare parts will give a speed boost but come with a cost.

## Problem Statement

For each team, given the list of cars and parts, we have to decide which car will be selected and which spare part will be added to the car such that maximum speed is achieved in the given budget.

Upon building all the cars, finally, we have to print the car name, team name, and the id of each of the spare parts attached to the car that can go the fastest in the race.

## Input and Output

#### Input

Three files are given:

- Teams.csv
- Cars.csv
- Parts.csv

The CSV files are to be read and parsed accordingly. The data model for the application is as follows:

##### Teams.csv

|team_id|team_name|cars|funds|

##### Cars.csv

|car_id|car_name|base_speed|top_speed|part_list_id|

##### Parts.csv

|part_list_id|part_id|price|speed_boost|

#### Output

    ======Winner======
    Team : Mercedes
    Car Name : MODEL_DF178
    Maximum Speed Achieved : 252
    Funds Spent : 5108
    Parts :
    PART_8FE6D
    PART_7839A
    PART_30ECC
    PART_F7574
    PART_3C7D6
    PART_A5005

## Solution steps:

    1. Read and parse all the 3 csv files
    2. For each team, find the fastest car
    3. For each car, find maximum achievable speed
    4. To achieve the maximum speed for a car using minimum funds, apply 0/1 knapsack problem approach
    5. Find and return the fastest car among all the teams

## Running:

##### Installing Dependencies

```bash
pip install -r requirements.txt
```

##### Executing Solution

```bash
cd src
python main.py ../data/Teams.csv ../data/Cars.csv ../data/Parts.csv
```

Copyright © 2020, Nikunj Agarwal. All rights reserved.
