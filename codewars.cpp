bool is_isogram(std::string str){
    std::vector<char> letters(str.begin(), str.end()); 
    for(int i = 0; i < letters.size() - 1; i++){
        for(int ii = i+1; ii < letters.size(); ii++){
            if(letters[i] == letters[ii]) return false;
            
        }
    }
    return true;
}
// This is the working code, I wrote it by myself correcting the first failed one. I found out what I didn't understand and why.

bool is_isogram(std::string str) {
    std::vector<char> letters(str.begin(), str.end()); 
    for (const char &c: letters)
        std::cout << std::tolower(c);
    for(int i = 0; i < letters.size() - 1; i++){
        for(int ii = i+1; ii < letters.size(); ii++){
            if(letters[i] == letters[ii]) return false;
            
        }
    }
    return true;
}

// This is the not working code. I will explain lines that are false and those that I understood wrongly.
// 2 line of the code. I thought that this line was only creating a vector of char letters with as size the the size str. What it actually does, it is taking  iterators (begin and end) and putting this part of the string in the vector
// (in this case the intire string, but with iterators I could put parts into it)

//4 line of the code. My second mistake was to misread the doc and wrongly assume that the cout was putting each char into the vector (it was actually done in line 2). My third one, was to think that the computer understands the lower and the uppercased letter as two different. So I added a useless for this situation command tolower(). From there goes my fouth mistake on the previous line.

//3 line of the code. I totally forgot about the const. And because I didn't understood the fonctionning of the code since the beginning I havn't noticed it.

// The rest of the code is correct

//I corrected the code by removing the useless for loop. That's all. At least I know how to do vectors of characters now, the interpretation of lowercased and uppercased letters and the next time I wont forget the const (I put it, because it was in the initial code with explainations like the for loop. I thought it essencial for the code)
