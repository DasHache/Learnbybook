//#include <soi>
#include <bits/stdc++.h>
#include <vector>
// new idea -> only take into account if a[ii] is bigger and not a[ii-1]

signed main() {
    int t, n, h, counter = 0, v = 0; // t = cases, n=lenghv, h=height
    cin >> t;
    cout << "we have t\n";
    for (int i = 0; i < t; i++){
        cin >> n;
        cout << "we have n\n";
        vector <int> a;
        for (int ii = 0; ii < n; ii++){
            cin >> h;
            cout << "we have h\n";
            a.push_back(h); 
        }
        cout << "before while loop\n";
        vector <int> b;
        int s = a.size();
        cout << " taille de a " << s << "\n";
        while (a.size()>2){
            cout << "in the while loop\n";
            for (int ii = 1; ii < a.size(); ii++){
                if (ii == n-1 && a[ii-1] > a[ii]){
                    cout << " last ii and 1 > 2\n";
                    counter++;
                    if (b.size() != 0){
                        for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                            if(b[mi] == a[ii-1]){
                                b.erase(b.begin() + mi);
                            }else if(b[mi] > a[ii-1]){
                                break;
                            }
                        }
                    }
                    b.push_back(a[ii - 1]);
                }else if (ii == n-1 && a[ii-1] < a[ii]){
                    cout << " last ii and 1 < 2\n";
                    counter++;
                    if (b.size() != 0){
                        for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                            if(b[mi] == a[ii-1]){
                                b.erase(b.begin() + mi);
                            }else if(b[mi] > a[ii-1]){
                                break;
                            }
                        }
                    }
                    b.push_back(a[ii]);
                }else if (a[ii-1] > a[ii]){
                    cout << " 1 > 2\n";
                    if (b.size() != 0){
                        for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                            if(b[mi] == a[ii-1]){
                                b.erase(b.begin() + mi);
                            }else if(b[mi] > a[ii-1]){
                                break;
                            }
                        }
                    }
                    b.push_back(a[ii-1]);
                }else if (a[ii-1] < a[ii]){
                    cout << " 1 > 2\n";
                    if (b.size() != 0){
                        for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                            if(b[mi] == a[ii-1]){
                                b.erase(b.begin() + mi);
                            }else if(b[mi] > a[ii-1]){
                                break;
                            }
                        }
                    }
                    counter++;
                }else if (a[ii-1] == a[ii]){
                    cout << "1 == 2\n";
                    for (int mi = -1; mi < -1 * b.size() - 1;mi--){
                        if(b[mi] == a[ii-1]){
                            b.erase(b.begin() + mi);
                        }else if(b.size() == 0 || b[mi] > a[ii-1]){
                            break;
                        }
                    }
                    b.push_back(a[ii-1]);
                }
                a.erase(a.begin() + (ii-1));
                ii = 1;    
            }
            //a = b; 
            b.clear();    
        }
        cout << " taille de a " << s << "\n";
        for (int w = 0; w < a.size(); w++){
           cout << a[w] << " at place " << w;
        }
        if (a.size() == 2 && a[0] != a[1]){
           counter = counter + 1;   
        }else 
        if (a.size() == 2 && a[0] == a[1]){
            counter++;
        }else if (a.size() == 1){
            counter++;
        }else if (a.size() == 0){
            counter++;
        }
        cout << "\nCase #" << i << ": " << counter << "\n";
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
