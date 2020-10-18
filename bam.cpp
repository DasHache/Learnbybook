#include <bits/stdc++.h>
vector <vector<int> > splitter(vector <int> a, int b){
    vector <vector <int> > list;
    int ind = 0;
    for (int i;i < a.size(); i++){
        if (a[i] == b){
            ind = 1;
            continue;
        }
        if(ind == 0){
            list[0].push_back(a[i]);
        }else{
            list[1].push_back(a[i]);
        }
    }
    return list;

}
int sword_stroke(vector<int> a, int sum_len1){
    if (a.size() == 0) return 0;
    if (a.size() == 1) return 1;
    int m = *max_element(a.begin(), a.end());
    vector <vector <int> > lists = splitter(a, m); 
    for (vector <int> a_list : lists){
        int list_len = sword_stroke(a_list, sum_len1);
        sum_len1 = sum_len1 + list_len;
    }
    return sum_len1;

}
signed main() {
    int tests, n, height; // t = cases, n=lenghv, h=height
    cin >> tests;
    for (int i = 0; i < tests; i++){
        cin >> n;
        vector <int> bamboos(n);
        for(int& h : bamboos) cin >> height;
        int sum_len = 1;
        int answer = sword_stroke(bamboos, sum_len);
        cout << "Case #" << i << ": " << answer << endl;
    }
}                         
