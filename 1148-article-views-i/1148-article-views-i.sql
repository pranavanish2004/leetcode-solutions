# Write your MySQL query statement below
select Distinct author_id as id  #rename to id 
from Views
where author_id=viewer_id
order by author_id