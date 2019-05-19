-- Business Query 1
SELECT ColorName, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimColor c, DimAdoptionSpeed a, DimColorLabels l
WHERE f.ColorID = c.ColorID
AND c.PrimaryColor = l.ColorLabelID
AND c.ColorPurity = 'Pure'
AND f.AdoptionSpeedID = a.AdoptionSpeedID
AND a.ListingDuration <= 30
GROUP BY ColorName;

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
SELECT BreedPurity, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimBreed b, DimAdoptionSpeed a
WHERE f.BreedID = b.BreedID
AND a.AdoptionSpeedID = f.AdoptionSpeedID
AND a.AdoptionSpeed = 'Instant'
AND fee = 0 GROUP BY BreedPurity;

-- Business Query 5
SELECT s.State State, SUM(Quantity) Total
FROM FactPetAdoptionSpeed f, DimLocation l, DimState s
WHERE f.LocationID = l.LocationID
AND l.State = s.StateID
GROUP BY s.State
ORDER BY Total DESC;

