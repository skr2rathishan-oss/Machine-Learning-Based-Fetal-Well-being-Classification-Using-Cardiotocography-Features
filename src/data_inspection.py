from IPython.display import display

# Displays the first n rows of a 1-based range of columns as a table for quick DataFrame inspection
from IPython.display import display

def print_column_values(df, columns, start, end, n=10):
    """
    Display selected columns as a table.

    start and end are 1-based column positions.
    """

    selected_columns = columns[start - 1:end]

    print(f"\nShowing columns {start} to {end}")

    table = df[selected_columns].head(n)

    display(table)