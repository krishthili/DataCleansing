## DataCleansing
Python based Script using Data Science

# Class Name 
       DataCleansing
       
# Function Name
	01. Pandas.Series analysisMostNullColumn (Pandas.DataFrame, Threshold)
	02. Pandas.DataFrame removeMostNullColumn (Pandas.DataFrame, Pandas.Serie)
	
	# Finding Object Data types with null value and fill it
	03. Pandas.DataFrame analysisObjectData (Pandas.DataFrame, Boolean) 
	04. Pandas.DataFrame fillObjectValues (Pandas.DataFrame, List)
	05. Pandas.DataFrame convertObjectToCategory (Pandas.DataFrame)
	06. Pandas.DataFrame analysisCategoryData (Pandas.DataFrame)
	07. Pandas.DataFrame convertCategoryToNumber (Pandas.DataFrame)
	
	# Finding Number Data types with null value and fill it
	08. Pandas.DataFrame analysisNumberData (Pandas.DataFrame, Boolean) 
	09. Pandas.DataFrame fillNumberData (Pandas.DataFrame) -- Using interpolate()
	
	# Finding correlation between manipulated & disturbance variables
		# Check and Remove Zero Correlation
	10. Pandas.DataFrame analysisZeroCorrelation (Pandas.DataFrame, ProcessVariable)
	11. Pandas.DataFrame removeZeroCorrelation (Pandas.DataFrame, ProcessVariable)
	
		# Check and Removing parameters with high correlation (+ve Correlation, -ve Correlation)
	12. Pandas.DataFrame analysisHighlyCorrelation (Pandas.DataFrame)
	13. Pandas.DataFrame removeHighlyCorrelation (Pandas.DataFrame)
	
	14. Pandas.DataFrame manuallyDropColumns (Pandas.DataFrame, List)
