import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # find maximum salary of each department and add it to each row of employee
    employee["max_sal"] = employee.groupby("departmentId")["salary"].transform("max")

    # filter out rows of employee df based on maxium salary of their department
    maximum_paied_mask = employee["salary"] == employee["max_sal"]
    maximum_paied_employee = employee[maximum_paied_mask]

    # join two dataframes to extract department name corresponding to each department id
    inner_joined_df = pd.merge(left=maximum_paied_employee, right=department,
                      left_on="departmentId", right_on="id",
                      how="inner", suffixes=["_employee", "_department"])

    # choose ande rename proper columns of joined dataframe
    result = inner_joined_df[["name_department", "name_employee", "salary"]].rename(
        columns={
            "name_department": "Department",
            "name_employee": "Employee",
            "salary": "Salary"
        }
    )

    return result