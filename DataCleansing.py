import pandas as pd
import numpy as np

class DataCleansing:

    def analysisMostNullColumn(self,dataFrame,threshold):
        series_index = []
        series_value = []
        nullValue = dataFrame.isnull().sum()
        for key,value in nullValue.iteritems():
            if value != 0:
                percentage = (value/len(dataFrame)*100)
                if percentage > threshold:
                    series_index.append(key)
                    series_value.append(percentage)
                
        return pd.Series(data=series_value, index=series_index)
    
    def removeMostNullColumn(self,dataFrame,series):
        dataFrame = dataFrame.drop(series.index, axis=1)
        return dataFrame
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    
    def analysisObjectData(self, dataFrame, null):
        series_index = []
        series_category_value = []
        series_category_count= []
        series_category_len= []
        series_sum = []
        series_max_name = []
        series_max_val = []
        series_null_percentage = []
        
        dataframe_len = len(dataFrame)
        
        count = 0
        
        nullValues = dataFrame.select_dtypes(include=['object']).isnull().sum()
        
        if null == True:
            for key,value in nullValues.iteritems():
                series_index.append(key)
                series_category_value.append(dataFrame[key].value_counts().index.tolist())
                series_category_count.append(dataFrame[key].value_counts().tolist())
                series_category_len.append(len(dataFrame[key].value_counts().tolist()))
                series_sum.append(dataframe_len - (dataFrame[key].value_counts().sum()))
                series_max_name.append(dataFrame[key].value_counts().index.tolist()[0])
                series_max_val.append(dataFrame[key].value_counts().tolist()[0])
                series_null_percentage.append(100-(((dataFrame[key].value_counts().sum())/dataframe_len)*100))
                count = count + 1
                
        else:
            for key,value in nullValues.iteritems():
                if value != 0:
                    series_index.append(key)
                    series_category_value.append(dataFrame[key].value_counts().index.tolist())   
                    series_category_count.append(dataFrame[key].value_counts().tolist())
                    series_category_len.append(len(dataFrame[key].value_counts().tolist()))
                    series_sum.append(dataframe_len - (dataFrame[key].value_counts().sum()))
                    series_max_name.append(dataFrame[key].value_counts().index.tolist()[0])
                    series_max_val.append(dataFrame[key].value_counts().tolist()[0])
                    series_null_percentage.append(100-(((dataFrame[key].value_counts().sum())/dataframe_len)*100))
                    count = count + 1
                    
        
        return pd.DataFrame({'Category Value':series_category_value, 'Category Count':series_category_count, 'Category length':series_category_len,  'Max Name':series_max_name, 'Max Value':series_max_val, 'Null Count':series_sum, 'Null %':series_null_percentage}, index=series_index)
            
        
    def fillObjectValues(self, dataFrame, exclude):
        nullValues = dataFrame.select_dtypes(include=['object']).isnull().sum()
        for i in nullValues.index:
            if i not in exclude:
                list_of_value = dataFrame[i].value_counts().index.tolist()
                dataFrame[i] =dataFrame[i].fillna(list_of_value[0])
        return dataFrame
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    
    def convertObjectToCategory(self, dataFrame):
        object_columns = dataFrame.select_dtypes(['object']).columns
        dataFrame[object_columns] = dataFrame[object_columns].astype('category')
        return dataFrame
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    
    def analysisCategoryData(self, dataFrame):
        series_index = []
        series_category_value = []
        series_category_count= []
        series_category_len= []
        series_category_value_id = []
                
        category_columns = dataFrame.select_dtypes(['category']).isnull().sum()
        
       
        for key,value in category_columns.iteritems():
            series_index.append(key)
            series_category_value.append(dataFrame[key].value_counts().index.tolist())
            series_category_count.append(dataFrame[key].value_counts().tolist())
            series_category_len.append(len(dataFrame[key].value_counts().tolist()))
            series_category_value_id.append(dict(enumerate(dataFrame[key].cat.categories)))  
            
        return pd.DataFrame({'Category Value':series_category_value, 'Category Count':series_category_count, 'Category length':series_category_len, 'id':series_category_value_id}, index=series_index)
    
    def convertCategoryToNumber(self, DataFrame):
        category_columns = DataFrame.select_dtypes(['category']).columns
        DataFrame[category_columns] = DataFrame[category_columns].apply(lambda x: x.cat.codes)
        return DataFrame
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
        
     
    def analysisNumberData(self, dataFrame, null):
        series_index = []
        series_sum = []
        series_null_percentage = []
        
        dataframe_len = len(dataFrame)
        
        nullValues = dataFrame.select_dtypes(include=['number']).isnull().sum()
        
        if null == True:
            for key,value in nullValues.iteritems():
                series_index.append(key)
                series_sum.append(dataframe_len - (dataFrame[key].value_counts().sum()))
                series_null_percentage.append(100-(((dataFrame[key].value_counts().sum())/dataframe_len)*100))
                
                
        else:
            for key,value in nullValues.iteritems():
                if value != 0:
                    series_index.append(key)
                    series_sum.append(dataframe_len - (dataFrame[key].value_counts().sum()))
                    series_null_percentage.append(100-(((dataFrame[key].value_counts().sum())/dataframe_len)*100))
        return pd.DataFrame({'Null Count':series_sum, 'Null %':series_null_percentage}, index=series_index)
        
    def fillNumberData(self, dataFrame):
        return dataFrame.interpolate()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
        
    def analysisZeroCorrelation(self, dataFrame, target):
        return dataFrame.corr()[target].abs().round(2)
    
    def removeZeroCorrelation(self, dataFrame, target):
        correlations = dataFrame.corr()[target].abs().round(2)
        return dataFrame.drop(correlations[correlations<0.4].index,axis=1)
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    
    #finding correlation between manipulated & disturbance variables
    def analysisHighlyCorrelation(self, dataFrame):
        correlations = dataFrame.corr().round(6)
        return correlations.where(np.triu(np.ones(correlations.shape), k=1).astype(np.bool))
    
    #removing parameters with high correlation (+ve Correlation, -ve Correlation)
    def removeHighlyCorrelation(self, dataFrame):
        correlations = dataFrame.corr().round(2)
        upper = correlations.where(np.triu(np.ones(correlations.shape), k=1).astype(np.bool))
        cols_to_drop = []
        for i in upper.columns:
            if (any(upper[i] == -1) or any(upper[i] == -0.98) or any(upper[i] == -0.99) or any(upper[i] == 0.98) or any(upper[i] == 0.99) or any(upper[i] == 1) ):
                cols_to_drop.append(i)

        return dataFrame.drop(cols_to_drop, axis=1) 
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    
    def manuallyDropColumns(self, dataFrame, columns):
        return dataFrame.drop(columns, axis=1)
    
    