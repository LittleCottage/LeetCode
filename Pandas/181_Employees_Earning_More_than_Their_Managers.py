import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, how='left', left_on='managerId', right_on='id').query('(salary_x > salary_y) & (salary_y != None)')
    return df[['name_x']].rename(columns={'name_x': 'Employee'})