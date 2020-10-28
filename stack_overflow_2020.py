# %% [markdown]
# # Stack Overflow Developer Survey 2020 - extra analysis

# %%
import pandas
import numpy

# %% [markdown]
#  Data downloaded from Stack Overflow

# %%
source = pandas.read_csv('survey_results_public.csv')
source.head()

# %% [markdown]
#  ## Liked technologies
#  ### Step by step
#  #### Languages

# %%
language_likes_source = source[['LanguageWorkedWith','LanguageDesireNextYear']]
language_likes_source.head()

# %%
complete_rows_only = language_likes_source.dropna()
complete_rows_only.head()

# %% [markdown]
#  split the lists in both columns
def split_all_lists(dataframe_):
    splited = pandas.DataFrame()
    for column in dataframe_:
        splited[column] = dataframe_[column].str.split(';')
    return splited
# %%
languages_splited = split_all_lists(complete_rows_only)
languages_splited.head()

# %% [markdown]
#  make a row for every item in first column
def explode_first_column(dataframe_):
    return dataframe_.explode(dataframe_.columns[0])

# %%
exploded = explode_first_column(languages_splited)
exploded.head()

# %% [markdown]
#  function that compares technology worked in and technologies desired in a row
def is_liked(row):
    return row[0] in row[1]
# %% [markdown]
# function to apply is_liked on dataframe
def add_likes(dataframe_):
    dataframe_['liked'] = dataframe_.apply(is_liked, axis=1)
    return dataframe_

# %% [markdown]
#  create new column with True if responder wants to continue developing in technology, else False
with_likes = add_likes(exploded)
with_likes.head()

# %%
def aggregate_likes(dataframe_):
    return dataframe_.groupby(dataframe_.columns[0]).agg({'liked':'mean'})

# %%
languages_unsorted = aggregate_likes(exploded)
languages_unsorted.head()

# %%
languages_sorted = languages_unsorted.sort_values('liked', ascending=False)
languages_sorted

# %% [markdown]
#  ### In one step
def likes(root):
    workedwith = ''.join([root, 'WorkedWith'])
    desirenextyear = ''.join([root, 'DesireNextYear'])
    dataframe_part = source[[workedwith, desirenextyear]].dropna()
    splited = split_all_lists(dataframe_part)
    exploded = explode_first_column(splited)
    with_likes_ = add_likes(exploded)
    aggregated = aggregate_likes(with_likes_)
    return aggregated.sort_values('liked', ascending=False)

 # %%
language_likes = likes('Language')
language_likes

# %%
liked_databases = likes('Database')
liked_databases

# %%
platform_likes = likes('Platform')
platform_likes

webframe_likes = likes('Webframe')
webframe_likes

# %%
misctech_likes = likes('MiscTech')
misctech_likes

# %%
collab_tool_likes = likes('NEWCollabTools')
collab_tool_likes

# %% [markdown]
# ## Salaries
#  limit salaries to meaningful values
MINIMAL_WAGE = 13000
MAXIMAL_WAGE = 1999999

# %% [markdown]
#  ... to be continued ...

'LanguageWorkedWith'
'LanguageDesireNextYear'
'DatabaseWorkedWith'
'DatabaseDesireNextYear'
'PlatformWorkedWith'
'PlatformDesireNextYear'
'WebframeWorkedWith'
'WebframeDesireNextYear'
'MiscTechWorkedWith'
'MiscTechDesireNextYear'
'NEWCollabToolsWorkedWith'
'NEWCollabToolsDesireNextYear'
'DevType'
'ConvertedComp'
'YearsCode'