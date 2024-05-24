#include "main.h"
#include "./../../test_files/test_main.h"

int getSquare(int input)
{
    return input*input + NUMBER;
}  

int main(int p)
{
    test_getSquare();
}
