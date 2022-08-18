#include <iostream>
#include <string>
using namespace std;

int main() {
    int t, cur, prev = 0;
    float n;
    string str;

    cin >> t;
    cout << "t : " << t << endl;

    for (int i=0; i<t; i++) {
//        cin >> str;
        getline(cin, str);
        cout << "str : " << str << endl;

        cur = str.find(' ');
        cout << "substr res : " << str.substr(prev, cur) << endl;
        n = atof(str.substr(prev, cur).c_str());
        str = str.substr(cur, str.length());

        for (int j=0; j <= 3; j++) {
            cur = str.find(' ');
            str = str.substr(cur, str.length());
            switch (str[cur+1]) {
                case '@' : n *= 3; break;
                case '%' : n += 5; break;
                case '#' : n -= 7; break;
            }
            prev = cur;
        }
        cout << n << endl;
    }
    return 0;
}