#include <iostream>
#include <cmath>
#include <time.h>
#include <vector>
using namespace std;
int main(){
    clock_t t1, t2;
    t1=clock();
    unsigned int sum = 0;
    for (unsigned int i=1;i<1000;i++){
        if (i%3==0 || i%5==0){
            sum += i;
        }
    }
    t2=clock();
    cout<<"sum ="<<sum<<endl;
    double diff = ((double)t2-(double)t1)/CLOCKS_PER_SEC;
    cout<<"Time elapsed: "<<diff<<endl;
    return 0;
}
