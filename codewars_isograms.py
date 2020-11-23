# I was supposed to create a program which tells if a word is an isogram or not
# if a word has no letter repetitions it is an isogram (adp) otherwise it is not (ada)

# bool is_isogram(std::string str) {      creation of a bool type function
#       std:: vector < char > letters(str.begin(), str.end());   creation of a vector of chars with the length of string
#       for (const char &c: letters)   importing the value of a char into a string
#           std::cout << std::tolower(c);
#       for (int i = 0; i < letters.size() - 1;i ++){   comparing all the elements of a vector together
#              for (int ii = i+1; ii < letters.size(); ii++){
#                   if (letters[i] == letters[ii]) return false;  if two char are the same return false
#               }
#        }
#          return true;                             return true if there wes no repetition
# }
#
#           However this code doesn't work, as I understand with numbers because the sample is "0101000010..."

#           this solution I found on internet, however I can barely see the difference
# bool
# is_isogram(std::string str) {
#
# for (int a=0;a < str.size();a++){str[a]=std::tolower(str[a]);}
# if (str == "") {return true;}
# for (int i =0;i < str.size() - 1;i++){
#   for (int j=i+1;j < str.size();j++){
#       if (str[j] == str[i]) {return false;}
#   }
# }
# return true;
# }
