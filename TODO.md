# Requirements
R1 Create spreadsheet API\
R1.1 Python wrapper around spreadsheet object\
R1.1.1 Create the spreadsheet object, which takes in as a parameters all the fields fields according to the Google spreadsheet reference\
R1.1.1.1 Create reference for literal fields\
R1.1.1.2 Create Spreadsheet properties object\
R1.1.1.2.1 Create fields for literals\
R1.1.1.2.2 Create Recalculation interval enum\
R1.1.1.2.3 Create cellformat object\
R1.1.1.2.3.01 create number format object\
R1.1.1.2.3.01.1 create literal fields - understand pattern\
R1.1.1.2.3.01.2 create number format type enum\
R1.1.1.2.3.02 create Color object\
R1.1.1.2.3.02.1 literal values - also understand the article about it\
R1.1.1.2.3.03 create Colorstyle object\
R1.1.1.2.3.03.1 create --union color object\
R1.1.1.2.3.03.1.1 create the literals and understand the article\
R1.1.1.2.3.03.2 create theme color type enum\
R1.1.1.2.3.04 create Borders object\
R1.1.1.2.3.04.1 create and fit the border object\
R1.1.1.2.3.04.1.1 create literal fields\
R1.1.1.2.3.04.1.2 create style enum\
R1.1.1.2.3.04.1.3 create color object\
R1.1.1.2.3.04.1.3.1 create literals and understand article\
R1.1.1.2.3.04.1.4 create colorstyle object\
R1.1.1.2.3.04.1.4.1 create --union color object\
R1.1.1.2.3.03.1.4.1.1 create the literals and understand the article\
R1.1.1.2.3.03.1.4.2 create theme color type enum\
R1.1.1.2.3.05 create padding object\
R1.1.1.2.3.05.1 create literal\
R1.1.1.2.3.06 create horizontal align enum\
R1.1.1.2.3.07 create vertical align enum\
R1.1.1.2.3.08 create wrap strategy enum\
R1.1.1.2.3.09 create text direction enum\
R1.1.1.2.3.10 create text format object\
R1.1.1.2.3.10.1 create literals\
R1.1.1.2.3.10.2 create color object\
R1.1.1.2.3.10.2.1 create literal fields\
R1.1.1.2.3.10.3 create color style object\
R1.1.1.2.3.10.3.1 create --union color object\
R1.1.1.2.3.10.3.1.1 create literal fields\
R1.1.1.2.3.10.3.2 create --union theme color literal\
R1.1.1.2.3.10.4 creae link object\
R1.1.1.2.3.10.4.1 create literal fields\
R1.1.1.2.3.11 create hyperlinkdisplay type enum\
R1.1.1.2.3.12 create text rotation object\
R1.1.1.2.3.12.1 create --union literal fields\
R1.1.1.2.4 Create iterativeCalculationSettings object\
R1.1.1.2.4.1 create the literal fields\
R1.1.1.2.5 Create spreadsheet theme object\
R1.1.1.2.5.1 create literal fields\
R1.1.1.2.5.2 create theme colors pair object\
R1.1.1.2.5.2.1 create color type enum\
R1.1.1.2.5.2.1 create colorstyle object\
R1.1.1.2.5.2.1.1 create --union theme color enum\
R1.1.1.2.5.2.1.2 create --union color object\
R1.1.1.2.5.2.1.2.1 create literal fields\
R1.1.1.3 Create Sheet object\
R1.1.1.3.01 Create Sheet properties object\
R1.1.1.3.01.1 create fields for literals\
R1.1.1.3.01.2 create sheet type enum\
R1.1.1.3.01.3 create grid properties object\
R1.1.1.3.01.3.1\
R1.1.1.3.01.4 create color Object\
R1.1.1.3.01.4.1\
R1.1.1.3.01.5 create color style object\
R1.1.1.3.01.5.1 \
R1.1.1.3.01.6 create tab color syle object\
R1.1.1.3.01.6.1\
R1.1.1.3.01.7 create data source properties object\
R1.1.1.3.01.7.1\
R1.1.1.3.02 Create GridData object\
R1.1.1.3.02.1 create literal fields\
R1.1.1.3.02.2 create row data object\
R1.1.1.3.02.2.1\
R1.1.1.3.02.3 create dimension properties object\
R1.1.1.3.02.3.1\
R1.1.1.3.02.4\ fit the dimension properties object for the need of colmnMetadata
R1.1.1.3.03 Create Grid range object\
R1.1.1.3.03.1 create the literal fields\
R1.1.1.3.03.2 it would be great to implement all the index translations at this point\
R1.1.1.3.04 create Conditional format rule object\
R1.1.1.3.04.1 create the grid range object\
R1.1.1.3.04.1.1\
R1.1.1.3.04.2 create the --union boolean rule object\
R1.1.1.3.04.2.1\
R1.1.1.3.04.3 create the --union gradient rule object\
R1.1.1.3.04.3.1\
R1.1.1.3.05  create filterview object\
R1.1.1.3.05.1 create fields for literals\
R1.1.1.3.05.2 create grid range object\
R1.1.1.3.05.2.1\
R1.1.1.3.05.3 create sort spec object\
R1.1.1.3.05.3.1\
R1.1.1.3.05.4 create filter criteria object\
R1.1.1.3.05.4.1\
R1.1.1.3.05.5 create filter spec object\
R1.1.1.3.05.5.1\
R1.1.1.3.06 create Protected range object\
R1.1.1.3.06.1 create fields for literals\
R1.1.1.3.06.2 create grid range object\
R1.1.1.3.06.2.1\
R1.1.1.3.06.3 fit the grid range object for unprotected ranges purposes\
R1.1.1.3.06.4 create editors object\
R1.1.1.3.06.4.1\
R1.1.1.3.07 create basicfilter object\
R1.1.1.3.07.1 create grid range object\
R1.1.1.3.07.1.1\
R1.1.1.3.07.2 create sort spect object\
R1.1.1.3.07.2.1\
R1.1.1.3.07.3 create criteria object\
R1.1.1.3.07.3.1\
R1.1.1.3.07.4 create filter spec object\
R1.1.1.3.07.4.1\
R1.1.1.3.08 create embedded chart object\
R1.1.1.3.08.1\
R1.1.1.3.09 create banded range object\
R1.1.1.3.09.1 create literal fields\
R1.1.1.3.09.2 create grid range object\
R1.1.1.3.09.2.1\
R1.1.1.3.09.3 create banding properties object\
R1.1.1.3.09.3.1\
R1.1.1.3.09.4 fit the banding properties for needs of column properties\
R1.1.1.3.10 create developer metadata object\
R1.1.1.3.10.1 create fields for literals\
R1.1.1.3.10.2 create developer metadata location object\
R1.1.1.3.10.2.1\
R1.1.1.3.10.3 create developer metadata visibility enum\
R1.1.1.3.11 create dimesion group object\
R1.1.1.3.11.1 create literal fields\
R1.1.1.3.11.2 create object dimension range object\
R1.1.1.3.11.2.1\
R1.1.1.3.12 create column group - same as dimension group\
R1.1.1.3.12.1 fit the dimesnion groups for needs of column group\
R1.1.1.3.13 create slicer object\
R1.1.1.3.13.1 create literal fields\
R1.1.1.3.13.2 create slicer spec object\
R1.1.1.3.13.2.1\
R1.1.1.3.13.3 create embedded object position\
R1.1.1.3.13.3.1\
R1.1.1.4 Create NamedRange object\
R1.1.1.4.1 create fields for literal fields\
R1.1.1.4.2 create grid range object\
R1.1.1.4.2.1\
R1.1.1.5 Create developer metadata object\
R1.1.1.5.1 create fields for the literals\
R1.1.1.5.2 create DEveloper metadata location object\
R1.1.1.5.2.1\
R1.1.1.5.3 create developer metadata visibility enum\
R1.1.1.5.3.1\
R1.1.1.6 Create datasources object\
R1.1.1.6.1 create fields for literals\
R1.1.1.6.2 create data source spec object\
R1.1.1.6.2.1\
R1.1.1.6.3 create data source column spec\
R1.1.1.6.3.1\
R1.1.1.7 Create datasource reffresh schedules object\
R1.1.1.7.1 create fields for literals\
R1.1.1.7.2 create datasource refresh scope object\
R1.1.1.7.2.1\
R1.1.1.7.3 create interval object\
R1.1.1.7.3.1\
R1.1.1.7.4 create --union daily schedule object\
R1.1.1.7.4.1\
R1.1.1.7.5 create --union weekly schedule object\
R1.1.1.7.5.1\
R1.1.1.7.6 create --union monthly schedule object\
R1.1.1.7.6.1\
R1.2 Create a function and also bound create request method to create spreadsheet with tabs of provided names\
R1.3 Create the same as above but you also provide a mapping of sheet names - sheetIds for later uses\
R1.4 Extend the two requirements above with tab colors\
