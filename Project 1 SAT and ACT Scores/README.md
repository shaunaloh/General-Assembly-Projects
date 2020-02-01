# Project-1  
Submitted by: Loh Si Jun Shauna

## Problem Statement
Provide recommendations to improve SAT participation rates and scores, by making reference from SAT and ACT 2017 data trends across states.

## Executive Summary
Contents:

2017 Data Import & Cleaning

2018 Data Import and Cleaning

Exploratory Data Analysis

Data Visualization

Descriptive and Inferential Statistics

Outside Research

Conclusions and Recommendations

## Data Dictionary

| Feature                                      | Data Type     | Data Set                               | Description                   |
| -------------                                | ------------- |-------------                           | -------------                 |
| state                                        | object        | sat_2017, sat_2018, act_2017, act_2018 | State name                    |
| act_2017_participation                       | int64         | act_2017                               | 2017 ACT Participation Rate   |
| act_2017_english                             | float64       | act_2017                               | 2017 ACT English Score        |
| act_2017_math                                | float64       | act_2017                               | 2017 ACT Math Score           |
| act_2017_reading                             | float64       | act_2017                               | 2017 ACT Reading Score        |
| act_2017_science                             | float64       | act_2017                               | 2017 ACT Science Score        |
| act_2017_composite                           | float64       | act_2017                               | 2017 ACT Composite Score      |
| sat_2017_participation                       | int64         | sat_2017                               | 2017 SAT Participation Rate   | 
| sat_2017_evidence-based_reading_and_writing  | int64         | sat_2017                               | 2017 SAT Reading/Writing Score| 
| sat_2017_math                                | int64         | sat_2017                               | 2017 SAT Math Score           | 
| sat_2017_total                               | int64         | sat_2017                               | 2017 SAT Total Score          |
| act_2018_participation                       | int64         | act_2018                               | 2018 ACT Participation Rate   | 
| act_2018_math                                | float64       | act_2018                               | 2018 ACT Math Score  
| act_2018_reading                             | float64       | act_2018                               | 2018 ACT Reading Score 
| act_2018_science                             | float64       | act_2018                               | 2018 ACT Science Score 
| act_2018_composite                           | float64       | act_2018                               | 2018 ACT Composite Score 
| sat_2018_participation                       | int64         | sat_2018                               | 2018 SAT Participation Rate   
| sat_2018_evidence-based_reading_and_writing  | int64         | sat_2018                               | 2018 SAT Reading/Writing Score | sat_2018_math                                | int64         | sat_2018                               | 2018 SAT Math Score     
| sat_2018_total                               | int64         | sat_2018                               | 2018 SAT Total Score     | 
| sat_2018_total                               | int64         | sat_2018                               | 2018 SAT Total Score     | 
| sat_2017_no_of_sat_takers                    | int64         | sat_2017_withstudpop                   | 2017 SAT Number of SAT Takers|
| sat_2017_high_school_graduates               | int64         | sat_2017_withstudpop                   | 2017 SAT high school graduates| 
| sat_2017_percentage                          | float64       | sat_2017_withstudpop                   | 2017 SAT Percentage of high school students who took SAT| 
| sat_2018_no_of_sat_takers                    | int64         | sat_2018_withstudpop                   | 2018 SAT Number of SAT Takers|
| sat_2018_high_school_graduates               | int64         | sat_2018_withstudpop                   | 2018 SAT high school graduates| 
| sat_2018_percentage                          | float64       | sat_2018_withstudpop                   | 2018 SAT Percentage of high school students who took SAT| 


## Conclusions and Recommendations

Conclusion: 

The EDA shows me which states have the highest participation rates, lowest participation rates, and largest change in participation rates. This gives us insights into the states which embraces the ACT and/or SAT, as well as the states which were affected by state decisions to review the ACT and/or SAT. For example, Florida, Georgia and Hawaii experience the highest SAT and ACT participation rates in both 2017 and 2018, while Oregon experience the lowest SAT and ACT participation rates in 2017 and 2018. Illinois and Colorado experience the greatest change in participation rate for SAT and ACT from 2017 to 2018.

The scatterplots also show me that students who perform well in one subject, also perform well in the rest of the subjects, for ACT and SAT. The difficulty of the individual subject exams can also be seen from the distribution i.e. right skewed, left skewed or normal distribution. The box plot also gives us insights on the range of scores for the individual subjects.  

Recommendations:

More effort should be pumped in to boost participation rates in low participating states such as Oregon. This could include understanding how other states induce high participation rates and adopting their approach, and reviewing the difficulty of the ACT/SAT subject tests, because high level of difficulty may act as a deterrence for students to sit for the exam. 

State with low participation rate: North Dakota 

North Dakota has 2% SAT participation rate in both 2017 and 2018, making this state the lowest SAT participation rate for both years.
To increase participation rate, the state could mandate the completion of SAT and ACT for all high school students, or provide subsidy/funding to students who are interested to take the SAT and/or ACT exam.


Additional data for more informed investigations:
- SAT/ACT scores and participation rates for districts within each state. With a larger dataset, this would provide me greater granularity on the relationship between population size and participation rate, and the relationship between population size and scores.
- number of attempts at SAT/ACT (this is because College Board places no restrictions on how many times students can take the SAT or ACT). I would then explore the correlation between the student score and their number of attempts.
- total high school student population in each state. This is because it would be more useful to prioritize on improving participation rates in states with large student population, especially states with large student untapped potential i.e. large number of students who have yet to take the SAT.


## Citations

"SAT Score Averages by State, 2017 and 2018", (Aug 2019), 
https://ipsr.ku.edu/ksdata/ksah/education/6ed16.pdf

"Average ACT Scores by State (Most Recent)", (Aug 2017),
https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows

"Average ACT Scores by State Graduating Class 2018", (2018),
http://www.act.org/content/dam/act/unsecured/documents/cccr2018/Average-Scores-by-State.pdf

"Illinois has embraced the SAT, and the ACT is mad about it", (Elaine Chen, Jul 2018), https://www.chalkbeat.org/posts/chicago/2018/07/27/act-protests-state-boards-embrace-of-rival-test-provider/

"Colorado Changed to the SAT in 2017: What You Need to Know", (Daniel Wheeler, Jan 2017), https://www.testive.com/colorado-sat-change-2017/

"Western Oregon no longer requires SAT, ACT", (Natalie Pate, Nov 2016), https://www.statesmanjournal.com/story/news/education/2016/11/17/western-oregon-no-longer-requires-sat-act-scores/93505778/
