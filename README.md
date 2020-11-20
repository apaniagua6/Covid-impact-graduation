# Impact of COVID-19 on school graduation rates.


The pandemic has impacted educational activities with several countries shifting to online or hybrid models of education. As a result, students in specific demographic groups (under-represented minorities, low-income students, etc.) are dropping out of high school. 

High school dropout rate is defined as the percentage of 16- to 24-year-olds who are not enrolled in school and have not earned a high school credential (either a diploma or an equivalency credential such as a GED certificate) and, as of 2018, this rate varies by race/ethnicity with minorities, including Native Americans and people of color, having higher dropout rates than white youth (Asian at 1.9 percent, White at 4.2 percent, mixed raced at 5.2 percent, Black at 6.4 percent, Hispanic at 8.0 percent, Pacific Islander at 8.1 percent, and American Indian/Alaska Native at 9.5 percent) with males dropping out at higher rates than females for most groups.



## Data Sets

The following are the sources of the datasets that are used for our analysis. 


1. https://www.opendatanetwork.com/dataset/data.cityofnewyork.us/35ey-ieq4 - 2005 - 2015 Graduation rates for New York public schools 

2. https://nces.ed.gov/programs/digest/current_tables.asp  - Provides high level statistics on high school to college graduation and job prospects. Dropout rates, employment based on graduation levels, years .

3.  [Washington State Graduation Rates 2014-2019](https://data.wa.gov/browse?q=Report%20Card%20Graduation&sortBy=relevance) - Provides Report Card Graduation data for the 2014-19 school year through the most current year of graduation data available for Washington state. This data is disaggregated by the school, district, and state levels and includes counts and graduation rates of students by the following groups: grade level, gender, race/ethnicity, and student programs and special characteristics. 

4. Hindawi study - Outcomes  for students in UK e-learning study (age level, region, assessment score, final outcome)

5. USA aggregation of school drop out rates

6. https://www.mckinsey.com/industries/public-and-social-sector/our-insights/covid-19-and-student-learning-in-the-united-states-the-hurt-could-last-a-lifetime - COVID learning loss prediction model for low income/minority students
Washington State Graduation Rate - using Washington state as a control; we assume that washington state is more integrated across zip codes & school districts (2014-2019, dropout & year by demographics “studentgroup” & county/district level)

7. LA Youth Center data for dropout rates ages 14-21 (but only 2016-2017)

8. American Community Survey is an ongoing survey by the US Census that collects data January through December to provide communities with information for their decision-making. Table Table 219.75 is particularly relevant, as it includes the percentage of high school dropouts among persons 16 to 24 years old (status dropout rate) and percentage distribution of status dropouts, by labor force status and years of school completed from 1970 to 2018.


# Regions 
Census Bureau Regions. [See Map in PDF format](./readmefiles/census_regions.pdf) 

A check next to a state represents that we obtained the high school enrollment rate for that state. 


## Northeast
- [ ] Connecticut	(09)
- [ ] Maine 	(23)
- [ ] Massachusetts (25)
- [ ] New Hampshire 	(33)
- [ ] Rhode Island 	(44)
- [ ] Vermont 	(50)
- [ ] New Jersey	(34)
- [ ] New York	(36)
- [ ] Pennsylvania	(42)
## Midwest
- [ ] Indiana (18)
- [ ] Illinois (17)
- [ ] Michigan	(26)
- [ ] Ohio (	39)
- [ ] Wisconsin	(55)
- [ ] Iowa	 (19) 	 
- [ ] Nebraska	(31)
- [ ] Kansas 	(20) 
- [ ] North Dakota	(38)
- [ ] Minnesota	(27) 
- [ ] South Dakota	(46)
- [ ] Missouri	(29)

## South
- [ ] Delaware	(10)
- [ ] District of Columbia	(11)
- [ ] Florida 	(12)
- [ ] Georgia	(13)
- [ ] Maryland 	(24)
- [ ] North Carolina (37)
- [ ] South Carolina (45)
- [ ] Virginia (51)
- [ ] West Virginia	 (54)
- [ ] Alabama	(01)
- [ ] Mississippi	(28)
- [ ] Tennessee	(47)
- [ ] Arkansas	(05)
- [ ] Louisiana	(22)
- [ ] Oklahoma	(40)
- [x] Texas	 (48)

## West
- [ ] Arizona	 ( 04)
- [ ] Colorado	(08)
- [ ] Idaho	 (16)
- [ ] New Mexico	(35)
- [ ] Montana	(30)
- [ ] Utah	 (49)
- [ ] Nevada (32)
- [ ] Wyoming (56)
- [ ] Alaska 	(02)
- [ ] California	(06)
- [ ] Hawaii	 (15)
- [ ] Oregon	 (41)
- [ ] Washington	(53)

# Domain knowledge

- https://nces.ed.gov/programs/dropout/intro.asp

# Contribution Guidelines 
These are general guidelines on how to make changes to this repository. 

1. Clone the Repository 
2. Create a Branch
3. Add your data sets
4. Create your own notebook for data_exploration ex. abe_scratch.ipynb
5. Work on your data exploration notebook
6. git commmit
7. git push origin master
8. Create a pull request via github.com
9. Someone reviews your pull request. 
10. Merge this branch into master
