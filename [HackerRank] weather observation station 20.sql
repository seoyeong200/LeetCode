set @rowIndex:=-1;
select round(avg(LAT_N), 4)
from(
    select @rowIndex:=@rowIndex+1 as rowNumber, LAT_N
    from STATION
    order by LAT_N
) as sub_table
where rowNumber in (floor(@rowIndex / 2), ceil(@rowIndex / 2));