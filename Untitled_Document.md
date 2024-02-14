trigger1= """
CREATE PROCEDURE InsertIntoUtenti(IN NEW_Gender VARCHAR(15), IN NEW_Age INT, IN NEW_CAP VARCHAR(6), IN NEW_Province VARCHAR(50), IN NEW_Work VARCHAR(255))
BEGIN
    DECLARE AgeGroup VARCHAR(20);

    IF NEW_Age < 18 THEN 
        SET AgeGroup = 'under 18';
    ELSEIF NEW_Age >= 18 AND NEW_Age < 25 THEN
        SET AgeGroup = '18-24';
    ELSEIF NEW_Age >= 25 AND NEW_Age < 35 THEN 
        SET AgeGroup = '25-34';
    ELSEIF NEW_Age >= 35 AND NEW_Age < 45 THEN
        SET AgeGroup = '35-44';
    ELSEIF NEW_Age >= 45 AND NEW_Age < 55 THEN
        SET AgeGroup = '45-54';
    ELSE
        SET AgeGroup = 'over 55';
    END IF;

    INSERT INTO utenti(Gender, Age, CAP, Province, Work, Age_groups) VALUES(NEW_Gender, NEW_Age, NEW_CAP, NEW_Province, NEW_Work, AgeGroup);
END;
"""
