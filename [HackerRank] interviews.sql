/* problem description
Contests - contest_id, hacker_id, name
Colleges - college_id, contest_id
Challenges - challenge_id, college_id
View_Stats - challenge_id, total_views, total_unique_views
Submission_Stats - challenge_id, total_submissions, total_accepted_submission

contest_id, hacker_id, name, 
the sums of total_submissions, 
            total_accepted_submissions, 
            total_views, 
            total_unique_views
for each contest 
sorted by contest_id.
Exclude the contest from the result if all four sums are 0.
*/

/* first trial - failed
challenge_id 기준으로 Challenges.college_id->Colleges.contest_id->Contests.contest_id, hacker_id, name
Submission_Stats, View_Stats left join 먼저 해서 필요한 디멘션 가져올 challenge_id 뽑자
    - submit해야 view stat 나올ㄹ테니까 submit기준으로 left join

LEFT JOIN은 WHERE 절 전에 사용되어야 합니다.

contest_id로 aggregate 하기 전에 Contest 조인 먼저 한다. 
contest_id 뿐만 아니라 hacker_id도 디멘션으로 잡아야하니까.
*/
select contest_id, hacker_id, name,
    sum(total_submissions) as total_submissions_by_contest_id,
    sum(total_accepted_submissions) as total_accepted_submissions_by_contest_id,
    sum(total_views) as total_views_by_contest_id,
    sum(total_unique_views) as total_unique_views_by_contest_id
from (
        select Contests.contest_id, Contests.hacker_id, Contests.name,
            Submission_and_View.total_submissions as total_submissions, 
            Submission_and_View.total_accepted_submissions as total_accepted_submissions, 
            Submission_and_View.total_views as total_views,
            Submission_and_View.total_unique_views as total_unique_views
        from (
                select Submission_Stats.challenge_id,
                        Submission_Stats.total_submissions, Submission_Stats.total_accepted_submissions,
                        View_Stats.total_views, View_Stats.total_unique_views
                from Submission_Stats
                left join View_Stats on Submission_Stats.challenge_id = View_Stats.challenge_id
        ) as Submission_and_View
        left join Challenges on Submission_and_View.challenge_id=Challenges.challenge_id
        left join Colleges on Challenges.college_id=Colleges.college_id
        left join Contests on Colleges.contest_id=Contests.contest_id
) as joined_tbl
group by contest_id, hacker_id, name
having total_submissions_by_contest_id+total_accepted_submissions_by_contest_id+total_views_by_contest_id+total_unique_views_by_contest_id>0
order by contest_id

/* second trial - accepted
첫번째 쿼리는 맨 처음에 submission과 view를 challenge_id 기준 조인해두고 시작했는데,
contest_id 기준으로 모든 fact들이 aggregate되지 않고 view에서의 데이터 누락이 발생한다.

contest_id 기준 submission, view 각각 aggregate 이후 contest_id 기준으로 inner join 한다.
*/
select agg_submission.contest_id, agg_submission.hacker_id, agg_submission.name, 
    agg_submission.ts, agg_submission.tas, 
    agg_view.tv, agg_view.tuv
from (
    select ct.contest_id, ct.hacker_id, ct.name, sum(ss.total_submissions) as ts, sum(ss.total_accepted_submissions) as tas
    from Contests ct
    join Colleges cl on ct.contest_id=cl.contest_id
    join Challenges ch on cl.college_id=ch.college_id
    join Submission_Stats ss on ch.challenge_id = ss.challenge_id
    group by ct.hacker_id, ct.name, ct.contest_id
) as agg_submission
join(
    select ct.contest_id, sum(vs.total_views) as tv, sum(vs.total_unique_views) as tuv
    from Contests ct
    join Colleges cl on ct.contest_id=cl.contest_id
    join Challenges ch on cl.college_id=ch.college_id
    join View_Stats vs on ch.challenge_id = vs.challenge_id
    group by ct.contest_id
) as agg_view
on agg_submission.contest_id = agg_view.contest_id