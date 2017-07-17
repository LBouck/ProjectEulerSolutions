//projectEuler3.cpp
#include <iostream>
#include <time.h>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

void reduce_duplicates(vector<unsigned long long> &vec){
    for (unsigned long long i=0;i<vec.size();i++){
        for (unsigned long long j=vec.size()-1;j>0;j--){
            if (i==j){ continue; }
            else if (vec.at(i)==vec.at(j)){ 
                vec.erase(vec.begin()+j);
            }
        }
    }
}

vector<unsigned long long> combineVec(vector<unsigned long long> vec1,vector<unsigned long long> vec2){
    vector<unsigned long long> answer;
    for (unsigned long long i=0;i<vec1.size();i++){
        answer.push_back(vec1.at(i));
    }
    for (unsigned long long i=0;i<vec2.size();i++){
        answer.push_back(vec2.at(i));
    }
    reduce_duplicates(answer);
    return answer;
}



vector<unsigned long long> recursive_prime_factors(unsigned long long n){
    vector<unsigned long long> answer;
    for (unsigned long long i=2;i<=(unsigned long long)sqrt(n);i++){
        if (n%i==0){ //recursive step
            answer = combineVec(recursive_prime_factors(i),recursive_prime_factors(n/i));
            return answer;
        }
    }
    answer.push_back(n); //base case: where n is prime
    return answer;
}

int main(){
    clock_t t1, t2;
    t1=clock();
    unsigned long long max = 0;
    unsigned long long n = 600851475143;
    vector<unsigned long long> vec = recursive_prime_factors(n);
    for (unsigned long long i; i<vec.size();i++){
        if (vec.at(i)>max){
            max = vec.at(i);
        }
    }
    t2=clock();
    cout<<"Max prime factor of "<<n<<" is "<<max<<endl;
    double diff = ((double)t2-(double)t1)/CLOCKS_PER_SEC;
    cout<<"Time elapsed: "<<diff<<endl;
    return 0;
}