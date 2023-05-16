#!/usr/bin/env python
# coding: utf-8

# In[201]:



pip install scipy


# In[5]:


import numpy as np
from distfit import distfit
import seaborn as sns
import fitter
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


file = pd.read_excel('EurovisionDZ.xlsx')
file_2015 = file[(file['year'] == 2015)]

class TaskOne:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2015)]

    def __init__(self, column_name):
        if column_name == 'age' or column_name == 'points' or column_name == 'number' or columnn_name == 'male': 
            self.c_name = column_name
        else:
            print('Mistake')
        
    def return_changed_db(self):
        return self.file_2015[self.c_name]
    
class TaskTwo:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2014)]
    
    def __init__(self, column_name):
        if column_name == 'age' or column_name == 'points' or column_name == 'number' or columnn_name == 'male': 
            self.c_name = column_name
        else:
            print('Mistake')
    def mode(self):
        return statistics.multimode(self.file_2015[self.c_name])
    
    def mediana(self):
        return self.file_2015[self.c_name].median()
    
    def expected_value(self):
        counter = 0
        summa = 0
        for i in self.file_2015[self.c_name]:
            summa += i 
            counter += 1
        pr = round(summa / counter, 3)
        return pr
    
    def sample_dispersion(self):
        return round(self.file_2015[self.c_name].var(), 3)
    
    def sample_standard_deviation(self):
        return round(self.sample_dispersion()**(1 / 2), 3)
    
    def corrected_dispersion(self):
        n = 0 
        for i in self.file_2015[self.c_name]:
            n += 1
        return round(n/(n-1)*self.sample_dispersion(), 3)
    
    def corrected_standard_deviation(self):
        return round(self.corrected_dispersion()**(1 / 2), 3)
    
    def variation_coefficient(self):
        cv = lambda x: np.std(x, ddof=1) / np.mean(x)
        return round(cv(self.file_2015[self.c_name])*100, 3)
    
    def skewness(self):
        num = np.mean(np.power(self.file_2015[self.c_name]-self.file_2015[self.c_name].mean(), 3))
        dem = np.power(self.file_2015[self.c_name].std(), 3)
        res = num / dem 
        return round(res, 3) 
    
    def excess_kurtosis(self):
        num = np.mean(np.power(self.file_2015[self.c_name]-self.file_2015[self.c_name].mean(), 4))
        dem = np.power(self.file_2015[self.c_name].std(), 4)
        res = num / dem - 3
        return round(num / dem, 3)
    
    def build_histogram(self):
        self.file_2015[self.c_name].plot(title = self.c_name.title(), kind = 'hist')
        
    def plot_empirical_cdf(self):
        sns.kdeplot(self.file_2015[self.c_name], cumulative=True)
        
    def how_does_it_look_like(self):
        dist = distfit()
        dist.fit_transform(self.file_2015[self.c_name])
        dist.plot()
        
        
class TaskThree:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2015)]
    
    def description(self):
        passdescription
    
    def corr_age_points(self):
        return round(np.corrcoef(self.file_2015['age'], self.file_2015['points'])[0, 1], 3)
    
    def corr_age_number(self):
        return round(np.corrcoef(self.file_2015['age'], self.file_2015['number'])[0, 1], 3)
    
    def corr_age_male(self):
        return round(np.corrcoef(self.file_2015['age'], self.file_2015['male'])[0, 1], 3)
    
    def corr_points_number(self):
        return round(np.corrcoef(self.file_2015['number'], self.file_2015['points'])[0, 1], 3)
    
    def corr_points_male(self):
        return round(np.corrcoef(self.file_2015['points'], self.file_2015['male'])[0, 1], 3)
    
    def corr_number_male(self):
        return round(np.corrcoef(self.file_2015['number'], self.file_2015['male'])[0, 1], 3)
    
    
    
    
class TaskFour:
    
    def description(self):
        return f'Look at the Word file'
    
    def find_param_a(self):
        return f'a = 12.499'
    
    def find_param_b(self):
        return f'b = 50'
    
    def find_param_c(self):
        return f'c = 23.5'
    
    def print_triangl(self):
        h = plt.hist(np.random.triangular(12.499, 23.5, 50, 27), bins=200, density=True)
        plt.show()
    

    
class TaskFive:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2015)]
    
    def find_for_mean(self):
        x = int(file_2015['age'].mean())
        n = 0
        for i in file_2015['age']:
            n += 1
        n_res = int(n ** (1 / 2))
        alpha = 0.1
        u_krit = 2.05
        s = int((n / (n - 1)) * (file_2015['age'].var()) ** (1 / 2))
        right_side = x + u_krit * s / n_res
        left_side = x - u_krit * s / n_res
        return f"{left_side} < mean < {right_side}"
    
    def find_for_sigma_kwadrat(self):
        n = 0
        for i in file_2015['age']:
            n += 1
        n_res = int(n ** (1 / 2))
        gamma = 0, 9
        alpha = 0, 1
        s = int((n / (n - 1)) * (file_2015['age'].var()) ** (1 / 2))
        hi_kwadrat_left = 38.9
        hi_kwadrat_right = 15.4
        left_side = ((n - 1) * s ** 2) / hi_kwadrat_left
        right_side = ((n - 1) * s ** 2) / hi_kwadrat_right
        return f'{left_side} < sigma_kwadrat < {right_side}'
    
class TaskSix:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2015)]
    task6_db = file_2015['age']
    
    def solution(self):
        res = s_x / s_y
        a0 = self.task6_db.median()
        x_mean = self.task6_db.mean()
        count = 0 
        for i in self.task6_db:
            count += 1
        s = (count / (count - 1) * self.task6_db.var()) ** (1 /2)
        n = count ** (1 / 2)
        T = round((x_mean - a0) / s * n, 3)
        t = 1.71
        if abs(T) < t:
            return f'H0 accepted {-t} < {abs(T)} < {t}'
        else:
            return False

        
    def description(self):
        pass 

class TaskSeven:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015_women = file[(file['year'] == 2015) & (file['male'] == 0)]
    file_2015_men = file[(file['year'] == 2015) & (file['male'] == 1)]
    
    def pre_solution(self):
        x_mean = round(self.file_2015_men['age'].mean(), 3)
        y_mean = round(self.file_2015_women['age'].mean(), 3)
        n = len(self.file_2015_men['age'])
        m = len(self.file_2015_women['age'])
        s_x = round(((n / (n - 1)) * self.file_2015_men['age'].var()), 3)
        s_y = round(((m / (m - 1)) * self.file_2015_women['age'].var()), 3)
        if s_x / s_y < 2.56:
            return f'True1'
        else:
            T = (x_mean - y_mean) / ((s_x * (1 / n) + s_y * (1 / m)) ** (1 / 2))
            q = ((s_x * (1 / 16) + s_y * (1 / 11)) ** 2) / ((1 / (16 -1)) * (s_x **2 / 16 ** 2) + (1 / (11 -1)) * (s_y ** 2 / 11 **2))
            t = 1.61
            if T < t:
                return f'True2'
            else:
                return False
            
        
    
    def solition(self):
        x_mean = round(self.file_2015_men['age'].mean(), 3)
        y_mean = round(self.file_2015_women['age'].mean(), 3)
        n = len(self.file_2015_men['age'])
        m = len(self.file_2015_women['age'])
        s_x = round(((n / (n - 1)) * self.file_2015_men['age'].var()) ** (1 / 2), 3)
        s_y = round(((m / (m - 1)) * self.file_2015_women['age'].var()) ** (1 / 2), 3)
        s = (((n - 1) * s_x ** 2 + (m - 1) * s_y ** 2) / (n + m - 2)) ** (1 / 2)
        T = (x_mean - y_mean) / (s * ((1 / n) + (1 / m)) ** (1 / 2))
        t = 1.71
        if T < t:
            return f'H0 accepted {-t} < {T}'
        else:
            return False

            
    
    
class TaskEight:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2015)]
    task8_db = file_2015['age']
    
    
    def solution(self):
        n = 27
        x = self.task8_db.mean()
        s = round(((n / (n - 1)) * self.task8_db.var()) ** (1 / 2), 3)
        m_list = [5, 6, 5, 5, 6]
        p_list = [0.165, 0.156, 0.196, 0.234, 0.249]
        np_list = [x * n for x in p_list]
        m_np_list = [x - y for x, y in zip(m_list, np_list)]
        m_np_2_list = [x ** 2 for x in m_np_list]
        res_list = [x / y for x , y in zip(m_np_2_list, np_list)]
        summa = 0 
        for i in res_list:
            summa += i 
        hi_kwadrat = 5.991
        if summa < hi_kwadrat:
            return f'H0 is acceptable'
        else:
            return False

        
class TaskNine:
    
    file = pd.read_excel('EurovisionDZ.xlsx')
    file_2015 = file[(file['year'] == 2015)]
    points = file_2015['points']
    semifinal = file_2015['semifinal']
    number = file_2015['number']
    
    def solution(self):
        res_points = [x + y for x, y in zip(self.points, self.semifinal)]
        cor_pearson = round(np.corrcoef(self.number, res_points)[0][1], 3)
        t = 1.71
        if -t < cor_pearson and cor_pearson < t:
            return f'H0 is acceptable'
        else:
            return False

    

    
    

a = TaskFour()
print(a. print_triangl())


# In[ ]:





# In[7]:


a = TaskTwo('age')
print(a.mediana())


# In[ ]:


(a + b + c) / 3 = 29.731 ,
(a^2 + b^2 + c^2 - a*b -a*c - b*c) / 18 = 35.325 , 
(a^5*(b - c) + c^5(a - b) + b^5*(c -a)) / (10*(b - a)*(c - a)*(b - c)) = 29371.115

