#include <iostream>
#include <string>
#include <memory.h> //for memset()
using namespace std;

int main() {
    string a, b;
    char ch;
    char ans[10001];
    int len;
    cin >> a >> ch >> b;
    if (ch == '*') {
        int aa, bb;
        aa = a.length()-1;
        bb = b.length()-1;
        len = aa+bb+1;
        memset(ans, '0', len * sizeof(char));
        ans[0] = '1';
    }
    else if (ch == '+'){
        int aLen = a.length(), bLen = b.length();
        if (aLen == bLen) {
            len = aLen;
            memset(ans, '0', len * sizeof(char));
            ans[0] = '2';
        }
        else {
            int longLen, shortLen;
            if (a.length() > b.length()) {longLen = a.length(); shortLen = b.length();}
            else if (a.length() < b.length()){shortLen = a.length(); longLen = b.length();}
            len = longLen;
            memset(ans, '0', len * sizeof(char));
            ans[0] = '1';
            ans[longLen-shortLen] = '1';
        }

    }
    for (int i = 0 ; i < len; i++){
        cout << ans[i];
    }
    cout << endl;
    return 0;
}