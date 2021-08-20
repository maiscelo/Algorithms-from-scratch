SELECT patient_county
	,avg(avg_visits_per_patient)*1.0 avg_visits
	,avg(avg_cost_per_patient)*1.0 avg_cost
    ,'Avg of Averages' table_type
FROM agg_patient_counties 
GROUP BY patient_county,table_type
