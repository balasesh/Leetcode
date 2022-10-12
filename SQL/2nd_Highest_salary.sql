Write a SQL query to select the 2nd highest salary in the engineering department. If more than one person shares the highest salary, the query should select the next highest salary.

Example:

Input:

employees table

Column	Type
id	INTEGER
first_name	VARCHAR
last_name	VARCHAR
salary	INTEGER
department_id	INTEGER


departments table

Column	Type
id	INTEGER
name	VARCHAR

Output:

Column	Type
salary	INTEGER


------------------------------------------------------------------------
with eng_salaries as (
    Select
        employees.salary,
        departments.name,
        dense_rank() over (
            partition by departments.name
            order by
                employees.salary desc
        ) as salary_rank
    from
        employees
        LEFT JOIN departments ON departments.id = employees.department_id
)
select
    salary
from
    eng_salaries
where
    departments.name = 'engineering'
    and salary_rank = 2
limit
    1