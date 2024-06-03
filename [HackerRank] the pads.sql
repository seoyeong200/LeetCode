/*
output
이름과 직업으로 되어있는 Occupation 테이블에서 
각 이름의 직업 첫 글자를 출력하고, 
각 직업의 인원 수를 출력한다.
..
Ketty(P)
Maria(A)
Meera(S)
..
There are a total of 2 doctors.
There are a total of 2 singers.
There are a total of 3 actors.
There are a total of 3 professors.

*/

select concat(Name, "(", left(Occupation, 1), ")") 
from OCCUPATIONS
order by Name;

select "There are a total of", count(*) as counting, concat(lower(Occupation), "s.")
from OCCUPATIONS
group by Occupation
order by counting, Occupation;