**OLAP Design -- Day 1**

**Logical modeling for Health Care System.**

In the logical modeling process, data are represented in details as much
as possible. Thus, Logical modeling is the base for designing physical
model.

In the logical phase, the attributes of the entity are listed and
defined their business mode. Here, we have selected the project name as
Health Care System because the sample data file contains the data of
employees working in a health sector through out the region of
Kathmandu, Pokhara and Hetauda. The dimension tables are made
accordingly to their domains like date is allocated to dimDate where all
dates fields are stored and employee data are stored in dimEmployee.

![](.//media/image1.jpeg)

Figure 1: Logical Representation of Health Care System

In the above figure, we have extracted the one fact table named as
factEmployee and other three dimension table which stores the
qualitative data of factEmployee table. The main concept for the
attributes of the table is that it must give how much or how many answer
of some dimensions. The other three dimension table dimDepartment,
dimDate and dimEmployee stores the data of department, date and
employess respectively. We have chosen the factEmployee as a fact table
because it contains data that can be aggregated like sum, count and
others as well.

**Physical Implementation of Health Care System**

For the physical implementation of Health Care System, we have selected
following database,

Database Engine: PostgreSQL

Database Name : healthCareSystem

![](.//media/image2.jpeg)

Figure 2: physical Implementation of Health Care System.

In the above figure, all possible datatypes of all attributes in each
dimension table and fact table is listed accordingly so that it can be
helpful for the physical implementation of those figure into the
database.
