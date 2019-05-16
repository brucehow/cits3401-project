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

PRINT CHAR(13) + CHAR(10) + '** INSERTING Dim DATA **';
GO

BULK INSERT DimBreedLabels FROM '$(SQLSourceDataPath)DimBreedLabels.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);


BULK INSERT DimBreed FROM '$(SQLSourceDataPath)DimBreed.csv'
WITH (
    FIRSTROW=2,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimColorLabels FROM '$(SQLSourceDataPath)DimColorLabels.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimColor FROM '$(SQLSourceDataPath)DimColor.csv'
WITH (
    FIRSTROW=2,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);


BULK INSERT DimLocation FROM '$(SQLSourceDataPath)DimLocation.csv'
WITH (
    FIRSTROW=2,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimState FROM '$(SQLSourceDataPath)DimState.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimGender FROM '$(SQLSourceDataPath)DimGender.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimType FROM '$(SQLSourceDataPath)DimType.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimAge FROM '$(SQLSourceDataPath)DimAge.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimMaturitySize FROM '$(SQLSourceDataPath)DimMaturitySize.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimFurLength FROM '$(SQLSourceDataPath)DimFurLength.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimVaccinated FROM '$(SQLSourceDataPath)DimVaccinated.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimDewormed FROM '$(SQLSourceDataPath)DimDewormed.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimSterilized FROM '$(SQLSourceDataPath)DimSterilized.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimHealth FROM '$(SQLSourceDataPath)DimHealth.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

BULK INSERT DimRescuer FROM '$(SQLSourceDataPath)DimRescuer.csv'
WITH (
    FIRSTROW=2,
    CHECK_CONSTRAINTS,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);


BULK INSERT FactPetAdoptionSpeed FROM '$(SQLSourceDataPath)FactPetAdoptionSpeed.csv'
WITH (
    FIRSTROW=2,
    DATAFILETYPE='char',
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);
