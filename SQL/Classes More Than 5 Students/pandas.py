import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    sample = courses.groupby(['class']).agg({
        'student': 'count'
    }).reset_index()

    return sample[sample['student'] >= 5][['class']]
