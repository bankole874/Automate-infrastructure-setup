import os

def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

directories = [
    'Finance_Budgets',
    'Contract_Documents',
    'Business_Projections',
    'Business_Models',
    'Employee_Data',
    'Company_Vision_and_Mission_Statement',
    'Server_Configuration_Script'
]

create_directories(directories)

