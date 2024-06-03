--
-- @lc app=leetcode id=1527 lang=mysql
--
-- [1527] Patients With a Condition
--

-- @lc code=start

"""Basics
WHERE column_name = 'value'

WHERE column_name <> 'value'
WHERE column_name != 'value'

WHERE column_name LIKE 'value%'
WHERE column_name LIKE 'v_lue'

WHERE column_name NOT LIKE 'value%'

WHERE column_name IN ('value1', 'value2', 'value3')

WHERE column_name BETWEEN 'value1' AND 'value2'
"""

"""Regexp
[ most_used_functions ]
REGEXP_LIKE     | if the input string matches the regular expression pattern, if returns true.
                |   where REGEXP_LIKE(product_name, '^A');
REGEXP_REPLACE  | replace matched pattern characters from the given field
                |   select REGEXP_REPLACE(phone_number, '[^0-9]', '') AS cleaned_number 
REGEXP_SUBSTR   | extract a substring from a string that matches pattern
                |   select REGEXP_SUBSTR(email, '@[^.]+') AS domain 

. : Matches any single character.
* : Matches zero or more of the preceding element.
+ : Matches one or more of the preceding element.
[abc] : Matches any of the enclosed characters.
[^abc] : Matches any character not enclosed.
^ : Matches the start of a string.
$ : Matches the end of a string.
| : Logical OR operator.
(abc) : Matches 'abc' and remembers the match.

1. validate if a given string matches the typical pattern of an email address
WHERE REGEXP_LIKE(email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

2. extract url from text
SELECT REGEXP_SUBSTR(message, 'https?://[^ ]+') AS url

3. replace non-numeric characters in a string
SELECT REGEXP_REPLACE(phone_number, '[^0-9]', '') AS cleaned_number 
    - [^0-9] : matches any character that is not a number
"""


select * from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'


-- @lc code=end

