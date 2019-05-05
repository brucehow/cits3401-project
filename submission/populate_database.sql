/*
SQL Script for insrting data into the 'PetAdoption' database

Author: Bruce How
Student ID: 22242664

** Run this script in SSMS and ensure to enable SQLCMD mode.
*/

 :setvar SQLSource "csv\"


PRINT CHAR(13) + CHAR(10) + '** INSERTING DATA **';
GO

USE PetAdoption;
GO

BULK INSERT DimBreed FROM '$(SQLSource)DimBreed.csv'
WITH (
    --CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimBreedLabels FROM '$(SQLSource)breed_labels.csv'
WITH (
    --CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimColorLabels FROM '$(SQLSource)color_labels.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimColor FROM '$(SQLSource)color.csv'
WITH (
    --CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimType FROM '$(SQLSource)type.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimGender FROM '$(SQLSource)gender.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSource)vaccinated.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimAge FROM '$(SQLSource)age.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimState FROM '$(SQLSource)state.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimLocation FROM '$(SQLSource)location.csv'
WITH (
	--CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimFee FROM '$(SQLSource)fee.csv'
WITH (
	CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT FactPetAdoptionSpeed FROM '$(SQLSource)fact.csv'
WITH (
	--CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);
