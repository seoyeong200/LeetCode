select student_subject.student_id, 
        student_subject.student_name, 
        student_subject.subject_name,
        COALESCE(exam_cnt.cnt, 0) as attended_exams
from
    (select Students.student_id, Students.student_name, Subjects.subject_name 
    from Students, Subjects) as student_subject
left join 
    (select student_id, subject_name, count(*) as cnt
    from Examinations
    group by student_id, subject_name) as exam_cnt
on exam_cnt.student_id = student_subject.student_id 
    and exam_cnt.subject_name = student_subject.subject_name 
order by student_subject.student_id, student_subject.subject_name