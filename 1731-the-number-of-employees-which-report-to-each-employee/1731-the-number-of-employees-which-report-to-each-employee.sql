# Write your MySQL query statement below
select reports_to as employee_id,(select name from Employees where e.reports_to=employee_id) as name,count(*) as reports_count,round(avg(age)) as average_age
from Employees e
where reports_to is not null
group by reports_to
order by employee_id

