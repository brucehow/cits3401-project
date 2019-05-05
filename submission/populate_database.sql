/*
SQL Script for inserting data into the database 'PetAdoption'
When running this script in SSMS, ensure that SQLCMD mode is enabled.
This script should only be run after running build_database.sql successfully.

Authors: Bruce How (22242664) & Haolin Wu (21706137)
*/

 :setvar SQLSourceDataPath "csv\"

PRINT CHAR(13) + CHAR(10) + '** INSERTING DATA **';
GO

USE PetAdoption;
GO

PRINT CHAR(13) + CHAR(10) + '** INSERTING Dim **';
BULK INSERT DimBreed FROM '$(SQLSourceDataPath)DimBreed.csv'
WITH (
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimBreedLabels FROM '$(SQLSourceDataPath)DimBreedLabels.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimColor FROM '$(SQLSourceDataPath)DimColor.csv'
WITH (
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimColorLabels FROM '$(SQLSourceDataPath)DimColorLabels.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimLocation FROM '$(SQLSourceDataPath)DimLocation.csv'
WITH (
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimState FROM '$(SQLSourceDataPath)DimState.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimGender FROM '$(SQLSourceDataPath)DimGender.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimType FROM '$(SQLSourceDataPath)DimType.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimAge FROM '$(SQLSourceDataPath)DimAge.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimMaturitySize.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimFurLength.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimVaccinated.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimDewormed.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimSterilized.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimHealth.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimRescuer.csv'
WITH (
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);


BULK INSERT FactPetAdoptionSpeed FROM '$(SQLSourceDataPath)FactPetAdoptionSpeed.csv'
WITH (
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);
