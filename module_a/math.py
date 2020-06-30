#!/usr/bin/env python
#!/usr/bin/env python
# coding: utf-8


# In[20]:


#get_ipython().run_line_magic('alias', 'nb_convert /Users/aaronciuffo/bin/develtools/nbconvert math.ipynb')




# In[21]:


#get_ipython().run_line_magic('nb_convert', '')




# In[1]:


import logging




# In[2]:


logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s:%(funcName)s %(levelname)s:%(message)s',
#                    datefmt='%Y.%m.%d %H:%M.%S')




# In[7]:


class adder():
    # sample doc string for init
    def __init__(self, vals=None):
        '''Add n numbers and return the value

        Properties:
            values(`list`): list of values'''
        self.vals = vals
        
    
    # use **logger** instead of logging -- this ensures that the messages are sent through any logging
    # handlers that are defined in the application that uses this module
    
    # example property getter/setter decoration
    @property
    def vals(self):
        '''set the values to be added and check type
        
        Args:
            vals(`list` of `int` or `float`): list of values
            
        Rasises:
            TypeError: vals must be of type `list` of type `int` or `tuple`'''
        return self._vals
    
    @vals.setter
    def vals(self, values):
        if not values:
            logging.warning('no values were set. Setting to default of []')
            values = []
        logger.debug(f'values: {values}')
        logger.debug('checking type of `vals`')
        if not isinstance(values, (list, tuple)):
            raise TypeError(f'bad data type; must be of type list or tuple')
        logger.info('checking each value for type')
        for each in values:
            logger.debug(f'checking: {each}')
            if not isinstance(each, (int, float)):
                raise TypeError(f'{each} is not of type int or float')
            logger.debug('ok')
        
        self._vals = values
    
    def answer(self):
        '''Add the values in the list and return the answer
        
        Retruns: 
            sum of vals'''
        logger.info('getting total')
        total = 0
        logger.debug('adding each value')
        for each in self.vals:
            total = total + each
            logger.debug(f'running total: {total}')
        
        return total




# In[8]:


# a = adder()

# a.vals = [1, 4, 6, 77, 2.3]

# a.answer()




# In[ ]:





