

# Function to infer the type of a value
def infer_type(value):
    if value is None:
        return "string"
    value = str(value)
    if re.match(r"^-?\d+$", value):
        return "int"
    elif re.match(r"^-?\d*\.\d+$", value):
        return "double"
    else:
        return "string"

# Function to infer the type of an entire column
def infer_column_type(column_values):
    types = {"int": 0, "double": 0, "string": 0}
    for value in column_values:
        inferred_type = infer_type(value)
        types[inferred_type] += 1
    return max(types, key=types.get)

# Get a sample of the DataFrame (with a limit of 25 rows)
sample_data = df.sample(withReplacement=False, fraction=0.1).limit(25).collect()

# Infer the types for each column
type_mappings = {}
for col_name in df.columns:
    column_values = [row[col_name] for row in sample_data]
    inferred_type = infer_column_type(column_values)
    type_mappings[col_name] = inferred_type

# Apply the cast to each column as specified in the inferred type_mappings dictionary
for col_name, col_type in type_mappings.items():
    if col_type == "int":
        df = df.withColumn(col_name, col(col_name).cast("int"))
    elif col_type == "double":
        df = df.withColumn(col_name, col(col_name).cast("double"))

# Print the schema after conversion
print("Schema after conversion:")
df.printSchema()

# Show the transformed DataFrame
df.show()
