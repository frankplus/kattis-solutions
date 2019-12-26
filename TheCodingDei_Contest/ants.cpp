/*
    Solution to Ants problem: https://open.kattis.com/problems/ants
    Author: Sebastien Biollo
    Date: 13/12/2019
*/
#include<bits/stdc++.h>
using namespace std;
int main() { 
    int T;
    cin >> T;
    for(int a = 0; a < T; ++a){
        int C, N;
        cin >> C >> N;
        int shortest = 0;
        int longest = 0;
        for(int b = 0; b < N; ++b){
            int num;
            cin >> num;
            shortest = max(shortest, min(num, C-num));
            longest = max(longest, max(num, C-num));
        }
        cout << shortest << " " << longest << "\n";
    }
}