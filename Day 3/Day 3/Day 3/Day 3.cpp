#include <iostream>
#include <string>
#include <vector>
#include <fstream>

int binaryToDecimal(std::string n)
{
    std::string num = n;
    int dec_value = 0;

    int base = 1;

    int len = num.length();
    for (int i = len - 1; i >= 0; i--) {
        if (num[i] == '1')
            dec_value += base;
        base = base * 2;
    }

    return dec_value;
}

void part1()
{
    std::ifstream input;
    input.open("../../Day-3-input.txt");

    //error check
    if (input.fail())
    {
        std::cerr << "error opening file";
        exit(1);
    }

    std::string currentNum;
    std::vector<std::string> lines;

    while (!input.eof())
    {
        input >> currentNum;
        lines.push_back(currentNum);
    }

    std::string gammaRate = "";
    std::string epsilonRate = "";

    int zeros[12]{};
    int ones[12]{};

    for (auto line : lines)
    {
        for (int i = 0; i < line.size(); i++)
        {
            if (line[i] == '1')
            {
                ones[i] += 1;
            }
            else
            {
                zeros[i] += 1;
            }
        }
    }
    for (int i = 0; i < 12; i++)
    {
        if (ones[i] > zeros[i])
        {
            gammaRate.append("1");
            epsilonRate.append("0");
        }
        else
        {
            gammaRate.append("0");
            epsilonRate.append("1");
        }
    }


    std::cout << "\nPart 1\n";
    std::cout << "gamma rate: " << binaryToDecimal(gammaRate) << " epsilon rate: " << binaryToDecimal(epsilonRate) << "\npower consumption of submarine: " << binaryToDecimal(gammaRate) * binaryToDecimal(epsilonRate) << "\n\n\n";
    input.close();
}

// part2 is incomplete 
void part2()
{
    std::ifstream input;
    input.open("../../Day-3-input.txt");

    //error check
    if (input.fail())
    {
        std::cerr << "error opening file";
        exit(1);
    }

    std::string currentNum;
    std::vector<std::string> oxygenGeneratorRating;
    std::vector<std::string> CO2scrubberRating;

    while (!input.eof())
    {
        input >> currentNum;
        oxygenGeneratorRating.push_back(currentNum);
        CO2scrubberRating.push_back(currentNum);
    }
    input.close();



    int zeros[12]{};
    int ones[12]{};

    for (auto line : oxygenGeneratorRating)
    {
        for (int i = 0; i < line.size(); i++)
        {
            if (line[i] == '1')
            {
                ones[i] += 1;
            }
            else
            {
                zeros[i] += 1;
            }
        }
    }

    for (int i = 0; i < 12; i++)
    {
        if (CO2scrubberRating.size() == 1)
            break;

        if (ones[i] > zeros[i])
        {
            for (auto line = oxygenGeneratorRating.begin(); line != oxygenGeneratorRating.end(); /* NOTHING */)
            {
                if ((*line)[i] == '0')
                    line = oxygenGeneratorRating.erase(line);

                else
                    ++line;

            }

            for (auto line = CO2scrubberRating.begin(); line != CO2scrubberRating.end(); /* NOTHING */)
            {
                if ((*line)[i] != '1')
                    line = CO2scrubberRating.erase(line);

                else
                    ++line;

            }
        }
        else if (ones[i] < zeros[i])
        {
            for (auto line = oxygenGeneratorRating.begin(); line != oxygenGeneratorRating.end(); /* NOTHING */)
            {
                if ((*line)[i] == '1')
                    line = oxygenGeneratorRating.erase(line);

                else
                    ++line;
            }

            for (auto line = CO2scrubberRating.begin(); line != CO2scrubberRating.end(); /* NOTHING */)
            {
                if ((*line)[i] == '0')
                    line = CO2scrubberRating.erase(line);

                else
                    ++line;
            }
        }
        else
        {
            for (auto line = oxygenGeneratorRating.begin(); line != oxygenGeneratorRating.end(); /* NOTHING */)
            {
                if ((*line)[i] == '0')
                    line = oxygenGeneratorRating.erase(line);

                else
                    ++line;
            }

            for (auto line = CO2scrubberRating.begin(); line != CO2scrubberRating.end(); /* NOTHING */)
            {
                if ((*line)[i] == '1')
                    line = CO2scrubberRating.erase(line);

                else
                    ++line;
            }

            std::cout << "even";
        }
    }

    std::cout << "\nPart 2\n";
    std::cout << "CO2 scrubber rating: " << binaryToDecimal(CO2scrubberRating[0]) << " epsilon rate: " << binaryToDecimal(oxygenGeneratorRating[0]) << "\nlife support rating of submarine: " << binaryToDecimal(CO2scrubberRating[0]) * binaryToDecimal(oxygenGeneratorRating[0]) << "\n\n\n";
}

int main()
{
    part1();
    part2();
}