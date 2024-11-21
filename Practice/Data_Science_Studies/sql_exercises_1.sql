-- Display all data (i.e., all columns) about patients in the table torako.pacjent:

SELECT * FROM torako.pacjent;

-- Display pacjent_id, wzrost, and waga for all patients sorted by height from tallest to shortest:

SELECT pacjent_id, wzrost, waga
FROM torako.pacjent
ORDER BY wzrost DESC;

-- How many patients are in the database, what is their average age, and what are the minimum and maximum heights?

SELECT 
    COUNT(pacjent_id) AS liczba_pacjentów, 
    AVG(wiek) AS sredni_wiek, 
    MIN(wzrost) AS min_wzrost, 
    MAX(wzrost) AS max_wzrost
FROM torako.pacjent;

-- How many patients in the database are older than 82 years and are either 171 cm tall or taller?

SELECT COUNT(*) 
FROM torako.pacjent
WHERE wiek > 82 AND wzrost >= 171;
Description: Count the number of patients with:

/*For data analysis, select:
Men aged between 80 and 83 years who weigh 77 kilograms,
Women aged between 67 and 68 years who also weigh 77 kilograms.*/

SELECT * 
FROM torako.pacjent
WHERE 
    ((plec = 'M' AND wiek BETWEEN 80 AND 83)
    OR
    (plec = 'K' AND wiek BETWEEN 67 AND 68))
    AND waga = 77;


-- Calculate BMI for all patients and display it along with other patient information:

SELECT torako.pacjent.*,
       (waga / ((wzrost / 100::decimal) * (wzrost / 100::decimal))) AS bmi
FROM torako.pacjent;


-- Find the average, maximum, and minimum weight for male patients with BMI indicating obesity (BMI > 30):

SELECT 
    AVG(waga) AS avg_waga, 
    MIN(waga) AS min_waga, 
    MAX(waga) AS max_waga
FROM (
    SELECT 
        waga, 
        (waga / ((wzrost / 100::decimal) * (wzrost / 100::decimal))) AS bmi, 
        plec
    FROM torako.pacjent
) AS subquery
WHERE bmi > 30 AND plec = 'M';
