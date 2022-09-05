import pandas as pd
import datetime

class Class_df():
    def __init__(self, _path):
        self.df = pd.read_csv(_path)
    
    def change(self, _column):
        #공백제거 뒤에.upper()로 붙여도 됌
        self.df[_column] = self.df[_column].str.replace(" ", "").str.upper()
        #대문자변환
        #self.df[_column] = self.df[_column].str.upper()
        return self.df
    
    def time(self, _column, _format = ""):
        if _format == "":
            self.df[_column] = pd.to_datetime(self.df[_column])
        else:
            self.df[_column] = pd.to_datetime(self.df[_column], format= _format)
        return self.df

    def new_var(self, _column):
        self.df["Year"] = pd.to_datetime(self.df[_column]).dt.strftime("%Y")
        self.df["month"] = pd.to_datetime(self.df[_column]).dt.strftime("%m")
        self.df["day"] = pd.to_datetime(self.df[_column]).dt.strftime("%d")
        return self.df

    def review(self):
        return self.df