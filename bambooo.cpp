//#include <soi>
#include <bits/stdc++.h>
#include <vector>


signed main() {
    int t, n, h, counter = 0, v = 0; // t = cases, n=lenghv, h=height
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> n;
        vector <int> a;
        for (int ii = 0; ii < n; ii++){
            cin >> h;
            a.push_back(h); 
        }
        vector <int> b;
        for (;;){
            for (int ii = 1; ii < a.size(); ii++){
                if (ii == n-1 && a[ii-1] > a[ii]){
                    counter++;
                    for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                        if(b[mi] == a[ii-1]){
                            b.erase(b.begin() + mi);
                        }else if(b[mi] > a[ii-1]){
                            break;
                        }
                    }
                    b.push_back(a[ii - 1]);
                }else if (ii == n-1 && a[ii-1] < a[ii]){
                    counter++;
                    for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                        if(b[mi] == a[ii-1]){
                            b.erase(b.begin() + mi);
                        }else if(b[mi] > a[ii-1]){
                            break;
                        }
                    }
                    b.push_back(a[ii]);
                }else if (a[ii-1] > a[ii]){
                    for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                        if(b[mi] == a[ii-1]){
                            b.erase(b.begin() + mi);
                        }else if(b[mi] > a[ii-1]){
                            break;
                        }
                    }
                    b.push_back(a[ii-1]);
                }else if (a[ii-1] < a[ii]){
                    for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                        if(b[mi] == a[ii-1]){
                            b.erase(b.begin() + mi);
                        }else if(b[mi] > a[ii-1]){
                            break;
                        }
                    }
                    counter++;
                        //b.size() != 2
                }
            }
            if (b.size() == 2 && b[0] != b[1]){
                counter = counter + 2;
                break;   
            }else if (b.size() == 2 && b[0] == b[1]){
                counter++;
                break;
            }else if (b.size() == 1){
                counter++;
                break;
            }else{
            a = b;
            b.clear();
            }
            
        }
        cout << "Case #" << i << ": " << counter << "\n";
        counter = 0;
    }
}                         
//         int max = *max_element(a.begin(), a.end());
//         for (int ii = 0; ii < n; ii++){
//             if (a[ii] == max){
//                 a[ii] = 0;
//             }
//         }
//         max = *max_element(a.begin(), a.end());
//         for (int ii = 0; max > 0; ii++){
//             if (ii == n-1 && a[ii] == max){
//                 counter++;
//                 a[ii] = 0;
//                 ii = 0;
//                 maxcounter = 0;
//             }else if (ii == n-1 && maxcounter > 0){
//                 counter++;
//                 maxcounter = 0;
//                 ii = 0;
//             }else if (a[ii] == max){
//                 maxcounter++;
//                 a[ii] = 0;
//             }else if (a[ii] == 0 && maxcounter > 0){
//                 counter++;
//                 maxcounter = 0;
//             }else if (ii == n-1){
//                 ii = 0;
//                 maxcounter = 0;
//             }
//             if (max != *max_element(a.begin(), a.end())){
//                 max = *max_element(a.begin(), a.end());
//                 if (maxcounter > 0){
//                     counter++;
//                 }
//                 ii = 0;
//                 maxcounter = 0;
//             }
//         }
//         cout << "Case #" << i << ": " << counter << "\n";
//         counter = 1;
//     }
// }




        // for (int ii = 1; ii < n; ii++){
        //     if (a[ii-1] != a[ii] && a[ii-1] == 1){
        //         counter++;
        //     }else if (ii == n-1 && a[ii] == 1 ){
        //         counter++;
        //     }
        // }
        // cout << "Case #" << i << ": " << counter << "\n";
        // counter = 1;
    

    //     if (a[index] == a[index + 1] && a[index] == a[index + 2]){
    //         cout << "Case #" << i << ": " << 1 << "\n";
    //     }else if (a[index] == a[index + 1] || a[index + 1] == a[index + 2]){
    //         cout << "Case #" << i << ": " << 2 << "\n";
    //     }else if (a[index] == a[index + 2] && a[index] > a[index + 1] ){
    //         cout << "Case #" << i << ": " << 2 << "\n";
    //     }else{
    //        cout << "Case #" << i << ": " << 3 << "\n";
    //     }

    // }
