# Write your MySQL query statement below
with cte as 
(select num ,lag(num) over() as prev_num, lead (num) over() as next_num
from logs)

select distinct num as ConsecutiveNums 
from cte 
where num=prev_num and num=next_num 