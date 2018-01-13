//TODO: Use this as a playground to practice with vectors


//TODO:
// Fill out your program's header. The header should contain any necessary
// include statements and also function declarations
#include <iostream>
#include <vector>
using namespace std;

vector<float> sub(vector<float> vector1, vector<float> vector2);
vector<float> dif(vector<float> vector1, vector<float> vector2);
vector<float> mul(vector<float> vector1, vector<float> vector2);
vector<float> emul(vector<float> vector1, vector<float> vector2);

//TODO:
// Write your main program. Remember that all C++ programs need
// a main function. The most important part of your program goes
// inside the main function. 
int main(){
    vector<float> v1(3);
    v1[0] = 5.0;
    v1[1] = 10.0;
    v1[2] = 27.0;
    vector<float> v2(3);
    v2[0] = 3.0;
    v2[1] = 17.0;
    v2[2] = 12.0;
    vector<float> v3(5);
    v3[0] = 27.0;
    v3[1] = 10.0;
    v3[2] = 31.0;
    v3[1] = 5.0;
    v3[2] = 7.0;
    vector<float> v4(5);
    v4[0] = 3.0;
    v4[1] = 1.0;
    v4[2] = 6.0;
    v4[1] = 19.0;
    v4[2] = 8.0;

    cout<<sub(v1, v2)<<endl;
    cout<<dif(v1, v2)<<endl;
    cout<<mul(v3, v4)<<endl;
    cout<<emul(v3, v4)<<endl;        
}

vector<float> sub(vector<float> vector1, vector<float> vector2){
	vector<float> sub(vector1.size());
	for (int i =0; i < vector1.size(); i++){
		sub[i] = vector1[i] - vector2[i];
	}
	return sub
}

