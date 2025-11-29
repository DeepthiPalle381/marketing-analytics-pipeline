-- 1. Overall Conversion Rate
SELECT 
    ROUND(AVG(target)::NUMERIC * 100, 2) AS conversion_rate_percent
FROM fact_marketing_interactions;


-- 2. Conversion Rate by Job
SELECT 
    c.job,
    COUNT(*) AS total_contacts,
    SUM(f.target) AS total_conversions,
    ROUND(AVG(f.target)::NUMERIC * 100, 2) AS conversion_rate
FROM fact_marketing_interactions f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.job
ORDER BY conversion_rate DESC;


-- 3. Conversion by Month
SELECT 
    month,
    COUNT(*) AS total_contacts,
    SUM(target) AS conversions,
    ROUND(AVG(target)::NUMERIC * 100, 2) AS conversion_rate
FROM fact_marketing_interactions
GROUP BY month
ORDER BY month;


-- 4. Impact of Previous Campaign Outcome
SELECT 
    poutcome,
    COUNT(*) AS total_contacts,
    SUM(target) AS conversions,
    ROUND(AVG(target)::NUMERIC * 100, 2) AS conversion_rate
FROM fact_marketing_interactions
GROUP BY poutcome
ORDER BY conversion_rate DESC;


-- 5. Does call duration affect conversion?
SELECT 
    CASE 
        WHEN duration < 100 THEN 'Short (<100 sec)'
        WHEN duration BETWEEN 100 AND 300 THEN 'Medium (100–300 sec)'
        ELSE 'Long (>300 sec)'
    END AS call_duration_group,
    COUNT(*) AS total_contacts,
    SUM(target) AS conversions,
    ROUND(AVG(target)::NUMERIC * 100, 2) AS conversion_rate
FROM fact_marketing_interactions
GROUP BY call_duration_group
ORDER BY conversion_rate DESC;


-- 6. Which customer age groups convert better?
SELECT 
    CASE 
        WHEN c.age < 30 THEN 'Under 30'
        WHEN c.age BETWEEN 30 AND 50 THEN '30–50'
        ELSE '50+'
    END AS age_group,
    COUNT(*) AS total_contacts,
    SUM(f.target) AS conversions,
    ROUND(AVG(f.target)::NUMERIC * 100, 2) AS conversion_rate
FROM fact_marketing_interactions f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY age_group
ORDER BY conversion_rate DESC;
