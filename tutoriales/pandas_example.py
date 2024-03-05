import random
import pandas

"""
This code generates a list of employees and then uses the
pandas library to summarize some data according to certain
columns of interest.
"""

#We create a list of lists with the information for each employee
employees_info = []
for _ in range(100):
    #We represent an employee as a list of 4 elements [Job,sex,age,salary]
    employees_info.append([random.choice(["Developer","Sales","Systems","Manager"]),
                           random.choice(['male','female']),
                           random.randint(18,66),
                           random.randint(1000,3000)])

#This prints the list of lists with all the information
print (employees_info)

#We create the pandas DataFrame, the basic structure in pandas library
#to manage data. The first parameter is the input data (our list of lists)
#and the second parameter 'columns' is used to specify an identifier for each
#column
data = pandas.DataFrame(employees_info, columns=["Job","Sex","Age","Salary"])

#Summary of the full data
print (data)

"""
Now, we can use pandas functions to get a better understanding of the data
in an easy and quick way.
"""

#For instance, we can group data by sex using the function 'groupby' to
#know the mean salary for male and female employees.
#'groupby' receives the column IDs that we want to use for grouping, and then a diccionary
# of the target columns and the metrics that we want to compute. 
#More info about the groupby column: 
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
group_col = "Sex"
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print ("   Salary grouped by sex      ")
print ("##############################\n")
print (data_salary)

#We also can group data by job
group_col = "Job"
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print ("   Salary grouped by job      ")
print ("##############################\n")
print (data_salary)

#We can group data by multiple columns, e.g., by job and sex
group_col = ["Job","Sex"]
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print (" Salary grouped by (job,sex)  ")
print ("##############################\n")
print (data_salary)

#Grouping data by job and sex, but now sorted by salary.
#To do so, we first do the groupby and then use the function sort_values
#to specify the column(s) we want to use to sort the data
group_col = ["Job","Sex"]
target_col = "Salary"
data_salary = data.groupby(group_col).agg({target_col :["mean","std"]})
print ("##############################")
print (" Salary grouped by (job,sex)  ")
print ("  (sorted by (salary,mean))   ")
print ("##############################\n")
data_salary.sort_values(by=(target_col, "mean"), ascending=False, inplace=True)
print (data_salary)



#COSA 2
#lo guardo aqui porsia

    nombres_unicos = data['name'].unique()
    total_pokemon = len(nombres_unicos)
    daño_total = data['damage'].sum()

    # Para los Pokémon de tipo Fire
    pokemon_fire = data[data['type'] == 'Fire']
    nombres_unicos_fire = pokemon_fire['name'].unique()
    total_daño_fire = pokemon_fire['damage'].sum() 
    total_pokemon_fire = len(nombres_unicos_fire)  
    media_daño_fire = total_daño_fire / total_pokemon_fire

    # Para los Pokémon de tipo Water
    pokemon_water = data[data['type'] == 'Water']
    nombres_unicos_water = pokemon_water['name'].unique()
    total_daño_water = pokemon_water['damage'].sum()
    total_pokemon_water = len(nombres_unicos_water)
    media_daño_water = total_daño_water / total_pokemon_water

    # Para los Pokémon de tipo Grass
    
    pokemon_grass = data[data['type'] == 'Grass']
    pokemon_grass.loc[:, 'healing'] = pokemon_grass['healing'].astype(float)
    total_healing = pokemon_grass['healing'].sum()
    nombres_unicos_grass = pokemon_grass['name'].unique()
    total_daño_grass = pokemon_grass['damage'].sum()
    total_pokemon_grass = len(nombres_unicos_grass)
    media_daño_grass = total_daño_grass / total_pokemon_grass

    media_curacion = total_healing / total_pokemon
    media_curacion_grass = total_healing / total_pokemon_grass

    media_daño_individual = daño_total / total_pokemon
    #daño_por_oponente = data.groupby(['_name', '_type', 'opponent_type'])
    
    # Establecer las medias del daño para cada tipo de Pokémon en la nueva columna correspondiente
    data.loc[data['type'] == 'Fire', 'media_daño_segun_tipo'] = media_daño_fire
    data.loc[data['type'] == 'Water', 'media_daño_segun_tipo'] = media_daño_water
    data.loc[data['type'] == 'Grass', 'media_daño_segun_tipo'] = media_daño_grass
    data['media_daño_individual'] = media_daño_individual
    data['media_curacion']  = media_curacion
    data.loc[data['type'] == 'Grass', 'media_curacion_grass'] = media_curacion_grass


