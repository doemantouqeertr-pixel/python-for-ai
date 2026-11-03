














# FUNCTION FOR ADDING TOTAL HOURS COLUMN

def add_total_hours(ef):
    ef['total_hours'] = ef['study_hours'] + ef['practical_hours']
    return ef


# FUNCTION FOR LOADING LOG FILE
import pandas as pd

def load_log(path):
    return pd.read_csv(path, skipinitialspace=True)




























