-- Business Query 1
-- Non Drilled Query
SELECT ColorPurity, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimColor c
WHERE f.ColorID = c.ColorID
GROUP BY c.ColorPurity
ORDER BY Total DESC;

-- Drilled Down Query
SELECT ColorName, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimColor c, DimColorLabels l
WHERE f.ColorID = c.ColorID
AND c.PrimaryColor = l.ColorLabelID
GROUP BY ColorName
ORDER BY Total DESC;

-- Business Query 2
SELECT Type, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimVaccinated v, DimSterilized s, DimType t
WHERE f.VaccinatedID = v.VaccinatedID
AND f.TypeID = t.TypeID
AND f.SterilizedID = s.SterilizedID
AND s.Sterilized = 'Yes'
AND v.Vaccinated = 'Yes'
GROUP BY Type;

-- Business Query 3
SELECT SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimType t, DimGender g, DimAdoptionSpeed a, DimFurLength l
WHERE f.TypeID = t.TypeID
AND f.GenderID = g.GenderID
AND f.AdoptionSpeedID = a.AdoptionSpeedID
AND f.FurLengthID = l.FurLengthID
AND l.FurLength = 'Long'
AND g.Gender = 'Female'
AND a.AdoptionSpeed = 'Instant'
AND t.Type = 'Cat';

-- Business Query 4
SELECT s.State State, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimLocation l, DimState s, DimAdoptionSpeed a
WHERE f.LocationID = l.LocationID
AND f.AdoptionSpeedID = a.AdoptionSpeedID
AND l.State = s.StateID
AND a.AdoptionSpeedID != 4
GROUP BY s.State
ORDER BY Total DESC;

-- Business Query 5
SELECT BreedPurity, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimHealth h, DimAdoptionSpeed a, DimBreed b
WHERE f.HealthID = h.HealthID
AND f.AdoptionSpeedID = a.AdoptionSpeedID
AND f.BreedID = b.BreedID
AND h.Health = 'Healthy'
AND a.AdoptionSpeed = 'Slow'
GROUP BY b.BreedPurity;
