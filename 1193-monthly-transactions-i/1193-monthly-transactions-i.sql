# Write your MySQL query statement below
select Date_format(trans_date,"20%y-%m") as month,country,count(*) as trans_count,sum(case when state="approved" then 1 else 0 end) as approved_count,sum(amount) as trans_total_amount,sum(case when state="approved" then amount else 0 end)as approved_total_amount
from Transactions t
group by Date_format(trans_date,"%y-%m"),country
