#include "test_main.h"
#include "stdio.h"


void test_getSquare()
{

    printf("Test for %d: %s",1, getSquare(1) == 15 ? PASS : FAIL);
    printf("Test for %d: %s",2, getSquare(2) == 18 ? PASS : FAIL);
    printf("Test for %d: %s",3, getSquare(3) == 23 ? PASS : FAIL);
    printf("Test for %d: %s",10, getSquare(10) == 114 ? PASS : FAIL);

}