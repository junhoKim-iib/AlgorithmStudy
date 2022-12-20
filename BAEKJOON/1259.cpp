#include<iostream>


using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    string str; 
    while(1){
        cin >> str;
        if(str == "0"){
            return 0;
        }
        int i = 0;
        int j = str.length() -1;
        while(i<j){
            if(str[i] != str[j]){
                
                break;
            }
            i++;
            j--;
        }
        if(i<j){
            cout << "no\n";
        }
        else{
            cout << "yes\n";
        }
    }
    return 0;
}
