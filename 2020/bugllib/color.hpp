#include <string>

namespace color {

    enum Color {
        BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE
    };

    enum Type {
        REG, BOL, UND, BAC, HI_INT, BOL_HI_INT, HI_INT_BAC, WARN, ERR
    };

    const std::string REGULAR[] = {
        "\e[0;30m", "\e[0;31m", "\e[0;32m", "\e[0;33m", "\e[0;34m", "\e[0;35m", "\e[0;36m", "\e[0;37m"
    };

    const std::string BOLD[] = {
        "\e[1;30m", "\e[1;31m", "\e[1;32m", "\e[1;33m", "\e[1;34m", "\e[1;35m", "\e[1;36m", "\e[1;37m"
    };

    const std::string UNDERLINE[] = {
        "\e[4;30m", "\e[4;31m", "\e[4;32m", "\e[4;33m", "\e[4;34m", "\e[4;35m", "\e[4;36m", "\e[4;37m"
    };

    const std::string BACKGROUND[] = {
        "\e[40m", "\e[41m", "\e[42m", "\e[43m", "\e[44m", "\e[45m", "\e[46m", "\e[47m"
    };

    const std::string HIGH_INTENSITY[] = {
        "\e[0;90m", "\e[0;91m", "\e[0;92m", "\e[0;93m", "\e[0;94m", "\e[0;95m", "\e[0;96m", "\e[0;97m"
    };

    const std::string BOLD_HIGH_INTENSITY[] = {
        "\e[1;90m", "\e[1;91m", "\e[1;92m", "\e[1;93m", "\e[1;94m", "\e[1;95m", "\e[1;96m", "\e[1;97m"
    };

    const std::string HIGH_INTENSITY_BACKGROUND[] = {
        "\e[0;100m", "\e[0;101m", "\e[0;102m", "\e[0;103m", "\e[0;104m", "\e[0;105m", "\e[0;106m", "\e[0;107m"
    };

    const std::string RESET = "\e[0m";

    std::string getColor(Color c, Type t) {
        switch(t) {
            case Type::REG:
                return REGULAR[c];
            case Type::BOL:
                return BOLD[c];
            case Type::UND:
                return UNDERLINE[c];
            case Type::BAC:
                return BACKGROUND[c];
            case Type::HI_INT:
                return HIGH_INTENSITY[c];
            case Type::BOL_HI_INT:
                return BOLD_HIGH_INTENSITY[c];
            case Type::HI_INT_BAC:
                return HIGH_INTENSITY_BACKGROUND[c];
            case Type::WARN:
                return REGULAR[Color::BLACK] + BACKGROUND[Color::YELLOW];
            case Type::ERR:
                return REGULAR[Color::WHITE] + BACKGROUND[Color::RED];
            default:
                return REGULAR[c];
        }
    }

    std::string colorString(std::string s, Color c, Type t = Type::REG) {
        std::string newS = s.substr();
        newS.insert(0, getColor(c, t));
        newS.append(RESET);
        return newS;
    }

    std::string colorString(std::string s, Type t) {
        return colorString(s, Color::WHITE, t);
    }

    std::string colorString(std::string s, Color frontC, Color backC, Type frontT = Type::REG, Type backT = Type::BAC) {
        std::string newS = s.substr();
        newS.insert(0, getColor(frontC, frontT) + getColor(backC, backT));
        newS.append(RESET);
        return newS;
    }

    std::string colorStringNoReset(std::string s, Color c, Type t = Type::REG) {
        std::string newS = s.substr();
        newS.insert(0, getColor(c, t));
        return newS;
    }

}