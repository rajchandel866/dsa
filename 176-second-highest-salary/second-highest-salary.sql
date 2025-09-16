select coalesce ( (select distinct e.salary
from Employee as e
order by salary desc
limit 1 
offset 1)) as SecondHighestSalary
