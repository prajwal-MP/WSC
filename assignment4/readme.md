# WEB AND SOCIAL COMPUTING

analyse properties of corona spread graph

The graph is constructed based on the data collected from COVID19-India API, A volunteer-driven, crowdsourced database for COVID-19 stats & patient tracing in India. We used the daily data from January 30, 2020 to June 04, 2020.


1. If patient level information is available we have taken each patient as a node

2. If only districtwise information is available, one node is taken for each district

3. If only statewise information is available, one node is created for each state

4. Each vertex has the attributes such as age,gender,State,Current status,Type of Transmission
and weight. 

5. Weight of each vertex indicate the number of patients. 

6. In the Covid graph a directed edge between patient x and patient y indicates that patient x
contracted disease from patient y. 

7. An outbreak begins when one or more nodes are infected from outside the population. These are
called imported infections. IMP node represent such transmission
