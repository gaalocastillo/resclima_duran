#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
This program shows an example of how to read
a CSV file and print the values of a specific column
*/

const char* getfield(char* line, int field)
{
    const char* tok;
    for (tok = strtok(line, ",");
            tok && *tok;
            tok = strtok(NULL, ",\n"))
    {
        if (!--field)
            return tok;
    }
    return NULL;
}

int main()
{
    FILE* stream = fopen("input", "r");
    //The field variable contains the column to be printed
    int field = 3;
    char line[1024];
    while (fgets(line, 1024, stream))
    {
        char* tmp = strdup(line);
        printf("The field selected would be %s\n", getfield(tmp, field));
        // NOTE strtok clobbers tmp
        free(tmp);
    }
}
