
tableData = [ ['apples','oranges','cherries','banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose'] ]

# caculate the width of longest string for each column
def columnWidth(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[0])):
            if(len(table[i][j]) > colWidths[i]):
                colWidths[i] = len(table[i][j])
    return colWidths


def printTable(tableData, colWidths):
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print('')

printTable(tableData, columnWidth(tableData))