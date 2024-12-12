1.	B   



2.	B



3.	SELECT Name, InsuranceID
    FROM Patient


    
4.	SELECT *
    FROM Physician
    WHERE Position = "Surgical Attending Physician"


    
5.	SELECT count(*)
    FROM Patient


    
6. SELECT D.name AS Department_name, 
       (SELECT P.Name 
        FROM Physician AS P 
        JOIN Affiliated_With AS AW 
          ON P.EmployeeID = AW.Physician
        WHERE AW.Department = D.DepartmentID AND AW.PrimaryAffiliation = TRUE
        LIMIT 1) AS Primary_Physician
  FROM Department AS D


    
7.	SELECT Physician, COUNT(*)
    FROM Appointment
    GROUP BY Physician


    
8.	SELECT A.AppointmentID, P.Name AS Patient_Name, PH.Name AS Physician_Name
    FROM Patient AS P
    JOIN Appointment AS A 
      ON P.SSN = A.Patient
    JOIN Physician AS PH
      ON A.Physician = PH.EmployeeID


      
9.	SELECT P.Name 
     FROM Patient AS P
     JOIN Appointment AS A
       ON A.Patient = P.SSN
   GROUP BY P.Name
   HAVING COUNT(AppointmentID) > 1


   
10. SELECT P.Name AS Patient_Name, M.Name AS Medication_Name
     FROM Patient AS P
     JOIN Prescribes AS PS 
       ON P.SSN = PS.Patient
     JOIN Medication AS M 
       ON PS.Medication = M.Code
