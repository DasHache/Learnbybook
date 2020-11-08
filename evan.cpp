#include <bits/stdc++.h>

signed main() {
    string s;
    int num;
    cin >> s >> num;
    vector <int> numbers;
    int answer = 0;

    if (s == "EVANIZE"){
        int verify = -1;
        int substraction = 0;
        for (int power = 13; power > -1; power--){
            if (verify == -1  && (num - substraction) / pow(5,power) == 0) continue;
            else{
                verify = 1;
                numbers.push_back((num - substraction)/ pow(5,power));
                substraction = substraction + ((num - substraction)/ pow(5,power)) * pow(5,power);
            }
        }
        int sizenum = numbers.size() - 1;
       for (int i = 0;i < numbers.size(); i++){
            answer = answer + numbers[i] * pow(10, sizenum);
            sizenum--;
        }
            cout << answer * 2;
    }else{
         if (num > 0){
            int count = 0, copi = num;
            while (copi != 0){
                copi = copi / 10;  
                count++;
            }
            copi = num;
            count = count - 1;
            while (count != -1){
                int power = 1;
                for (int i = 0; i < count; i++) power = power * 10;
                numbers.push_back(copi/power); 
                count--;
                copi = copi % power;    
            }
        }else{
            numbers.push_back(0);
        }
        int sizenum = numbers.size() - 1;
        for (int i = 0;i < numbers.size(); i++){
            answer = answer + numbers[i] * pow(5, sizenum);
            sizenum--;
        }
            cout << answer / 2;
    }
}
