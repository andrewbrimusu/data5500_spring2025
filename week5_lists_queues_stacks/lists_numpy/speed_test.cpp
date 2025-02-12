	
#include <stdlib.h>
#include <ctime>
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    
    clock_t begin = clock();
    short r[1000000];
    for (short i = 0; i < 1000000; ++i) {
        r[i] = rand() % 1000 + 1;
    }
    clock_t end = clock();
    double time1 = (end-begin) / 1000000.0;
    cout << "time (sec): "<< time1 << endl;
}
