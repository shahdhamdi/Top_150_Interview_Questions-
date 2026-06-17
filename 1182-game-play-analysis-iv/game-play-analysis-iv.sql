# Write your MySQL query statement below
with cte as (
select player_id,min(event_date) as first_login
from Activity 
group by player_id
),
cte2 as (
    select c.player_id
    from cte c
    join Activity a on a.player_id= c.player_id
    where datediff(a.event_date,c.first_login)=1
)

select round(count(distinct player_id)/(select count(distinct player_id) from activity),2) as fraction
from cte2



