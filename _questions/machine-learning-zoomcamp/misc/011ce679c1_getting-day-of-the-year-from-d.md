---
id: 011ce679c1
question: Getting day of the year from day and month column
sort_order: 4050
---

**Problem description:**

I have one column `day_of_the_month` with values like 1, 2, 20, 25, etc., as integers. I have a second column `month_of_the_year` with values like "jan", "feb", ..., "dec" as strings. I want to convert these two columns into one column `day_of_the_year` and have them as integers. For example, 2 and "jan" should give me 2 (i.e., 2nd day of the year), 1 and "feb" should give me 32 (i.e., 32nd day of the year). What is the simplest pandas method to achieve this?

**Solution description:**

1. Convert the `day_of_the_month` column from `int` to `str`:
   
   ```python
   df['day_of_the_month'] = df['day_of_the_month'].map(str)
   ```

2. Convert the `month_of_the_year` column from "jan", "feb", ..., "dec" into 1, 2, ..., 12 using `map()`.

3. Convert the day and month into a datetime object:

   ```python
   df['date_formatted'] = pd.to_datetime(
       dict(
           year=2055,  
           month=df['month'],
           day=df['day']
       )
   )
   ```

4. Get the day of the year:

   ```python
   df['day_of_year'] = df['date_formatted'].dt.dayofyear
   ```