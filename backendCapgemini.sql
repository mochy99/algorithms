SELECT state, tm as start_interval, LEAD(tm) OVER (ORDER BY tm) as end_interval
FROM (
    SELECT tm, state, LAG(state) OVER (ORDER BY tm) AS prev_state
    FROM my_table
) AS new
WHERE new.state <> new.prev_state OR new.prev_state IS NULL;
