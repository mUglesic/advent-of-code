#include <iostream>
#include <fstream>

namespace fileUtil {

    dataStructures::Array<std::string> readFile(std::string path) {

        dataStructures::List<std::string> lines;

        std::string s;

        std::ifstream f(path);

        while (std::getline(f, s)) {
            lines.add(s);
        }

        dataStructures::Array<std::string> arr = lines.toArray();

        f.close();
        lines.clean();

        return arr;
    }

}

namespace stringUtil {

    int countChars(std::string s, char c) {

        int counter = 0;
        std::string::iterator it;

        for (it = s.begin(); it != s.end(); it++) {
            if (*it == c) counter++;
        }

        return counter;
    }

    int countStrings(std::string s, std::string delim) {
        
        int delimIndex = 0;
        int counter = 0;

        while (true) {
            delimIndex = s.find(delim, delimIndex);
            if (delimIndex == -1) break;
            counter++;
            delimIndex += delim.size();
        }

        return counter;
    }

    dataStructures::Array<std::string> split(std::string s, char delim) {

        dataStructures::Array<std::string> arr(countChars(s, delim) + 1);

        int prevIndex = -1;
        int delimIndex = -1;

        for (int i = 0; i < arr.length(); i++) {
            delimIndex = s.find(delim, delimIndex + 1);

            arr[i] = s.substr(prevIndex + 1, delimIndex == -1 ? std::string::npos : (delimIndex - prevIndex - 1));

            prevIndex = delimIndex;
        }

        return arr;
    }

    dataStructures::Array<std::string> split(std::string s, std::string delim) {

        dataStructures::Array<std::string> arr(countStrings(s, delim) + 1);

        int prevIndex = -delim.size();
        int delimIndex = -delim.size();

        for (int i = 0; i < arr.length(); i++) {
            delimIndex = s.find(delim, delimIndex + delim.size());

            arr[i] = s.substr(prevIndex + delim.size(), delimIndex == -1 ? std::string::npos : (delimIndex - prevIndex - delim.size()));

            prevIndex = delimIndex;
        }

        return arr;
    }

}