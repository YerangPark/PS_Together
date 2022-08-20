#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cout << fixed;
    cout.precision(2);

    cin >> t;
    cin.ignore();
    for (int i=0; i<t; i++) {
        int cur = 0;
        float n = 0.0f;
        string str;

        getline(cin, str);

        cur = str.find(' ');
        n = atof(str.substr(0, cur).c_str());
        str = str.substr(cur + 1, str.length());

        for (int j=0; j <= 3; j++) {
            switch (str[0]) {
                case '@' : n *= 3; break;
                case '%' : n += 5; break;
                case '#' : n -= 7; break;
            }
            cur = str.find(' ');
            if (cur == -1) break;
            str = str.substr(cur+1, str.length());
        }
        cout << n << endl;
    }
    return 0;
}