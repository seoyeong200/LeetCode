select machine_id, round(avg(processed_time), 3) as processing_time
from
    (select start_.machine_id as machine_id, 
            end_.timestamp - start_.timestamp as processed_time
    from 
        (select machine_id, process_id, timestamp 
        from Activity 
        where activity_type = 'start') as start_,
        (select machine_id, process_id, timestamp 
        from Activity 
        where activity_type = 'end') as end_
    where start_.machine_id = end_.machine_id and start_.process_id = end_.process_id) as subtract
group by machine_id