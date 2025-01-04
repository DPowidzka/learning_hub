-- 3.1
-- Ask for the average, maximum, and minimum weight for each gender for patients who have a comorbid condition related to hypertension.
SELECT plec, MIN(waga) AS min_waga, MAX(waga) AS max_waga, AVG(waga) AS average_waga
FROM torako.pacjent AS p
JOIN torako.choroby_wspolistniejace AS chw
ON p.pacjent_id = chw.pacjent_id
WHERE chw.nadcisnienie_tetnicze = 'TAK'
GROUP BY p.plec;

-- 3.2
-- Show the average, maximum, and minimum weight for individuals with hypertension, broken down by the genders of the patients.
SELECT plec, chw.nadcisnienie_tetnicze, AVG(waga) AS average_waga, MIN(waga) AS min_waga, MAX(waga) AS max_waga
FROM torako.pacjent AS p
JOIN torako.choroby_wspolistniejace AS chw
ON p.pacjent_id = chw.pacjent_id
GROUP BY plec, chw.nadcisnienie_tetnicze;

-- 3.3
-- Query all patients who have postoperative complications (from the complications table).
-- Display the columns for atelectasis, mechanical ventilation, and postoperative death.
SELECT p.pacjent, pow.niedodma, pow.wentylacja_mechaniczna, pow.zgon_po_operacji
FROM torako.pacjent AS p
LEFT JOIN torako.powiklania AS pow
ON p.pacjent_id = pow.pacjent_id;

-- 3.4
-- Query patients without postoperative complications.
SELECT *
FROM torako.pacjent p
WHERE p.pacjent_id NOT IN (SELECT pacjent_id FROM torako.powiklania);

-- 3.5
-- Find patients who have hypertension as a comorbid condition,
-- a pleural wall infiltration in histopathology, and complications related to atelectasis (column niedodma = 'TAK').
SELECT p.pacjent
FROM torako.pacjent p
JOIN torako.powiklania pow USING(pacjent_id)
JOIN torako.choroby_wspolistniejace chw USING(pacjent_id)
JOIN torako.histopatologia h USING(pacjent_id)
WHERE chw.nadcisnienie_tetnicze = 'TAK'
  AND h.naciek_oplucnej_sciennej = 'TAK'
  AND pow.niedodma = 'TAK';

-- 3.6 Using CASE
-- For patients with other complications in the choroby_wspolistniejace table,
-- change the descriptive value to 'TAK' so that the column has only two values.
SELECT inne_powiklania,
       CASE inne_powiklania
           WHEN 'NIE' THEN 'NIE'
           ELSE 'TAK'
       END AS updated_inne_powiklania
FROM torako.choroby_wspolistniejace;

-- 3.7 Using CASE
-- Query all patients (from the pacjent table) based on their histopathological data.
-- If a patient had a histopathological diagnosis of "adenocarcinoma" with a tumor diameter > 20
-- or "squamous cell carcinoma" with a tumor diameter > 30, add a flag kohorta with the value 'TAK'.
-- For others, display the value 'NIE' in the kohorta column.
SELECT p.*,
       CASE
           WHEN (histo.rozpoznanie_histopatologiczne = 'rak gruczołowy' AND srednica_guza > 20) THEN 'TAK'
           WHEN (histo.rozpoznanie_histopatologiczne = 'rak płaskonabłonkowy' AND srednica_guza > 30) THEN 'TAK'
           ELSE 'NIE'
       END AS kohorta
FROM torako.pacjent p
LEFT JOIN torako.histopatologia histo
ON p.pacjent_id = histo.pacjent_id;

-- 3.8 Using PARTITION BY
-- Calculate the average weight for all patients, the average weight by gender,
-- the average weight for patients with the same height,
-- and the average weight for patients with the same height within the same gender.
SELECT waga, plec, wzrost,
       AVG(waga) OVER() AS avg_waga,
       AVG(waga) OVER(PARTITION BY plec) AS avg_waga_plec,
       AVG(waga) OVER(PARTITION BY wzrost) AS avg_waga_wzrost,
       AVG(waga) OVER(PARTITION BY plec, wzrost) AS avg_waga_wzrost_plec
FROM torako.pacjent;

-- 3.9
-- Use the RANK and DENSE_RANK functions to assign patients to groups based on their height.
SELECT
    pacjent, wzrost, waga, plec,
    RANK() OVER (ORDER BY wzrost DESC) AS rank_wzrost,
    DENSE_RANK() OVER (ORDER BY wzrost DESC) AS dense_rank_wzrost
FROM torako.pacjent;

-- 3.10
-- Use the NTILE function to create a set of patients to be used as a training dataset for our algorithm,
-- ensuring that only the tallest men or women in the patient population are included.
SELECT p.*,
       NTILE(4) OVER(ORDER BY wzrost DESC) AS grupa_treningowa
FROM torako.pacjent p
WHERE plec = 'M';
