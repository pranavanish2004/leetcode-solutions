# Write your MySQL query statement below
select tweet_id
from Tweets
where CHAR_LENGth(content)>15