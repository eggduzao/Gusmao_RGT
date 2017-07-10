from rgt.ExperimentalMatrix import ExperimentalMatrix

e = ExperimentalMatrix()
e.read("InputMatrix.txt")

print e.names
print e.types
print e.files
print e.fields
print e.fieldsDict["genegroup"][""]
print e.objectsDict


