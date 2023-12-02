#include <iostream>
#include <string>
#include <fstream>

void part1()
{
    std::ifstream input;
    input.open("../../Day-2-input.txt");

    //error check
    if (input.fail())
    {
        std::cerr << "error opening file";
        exit(1);
    }

    int forward = 0;
    int down = 0;

    int currentNum = 0;

    std::string s;
    input >> s;

    while (!input.eof())
    {
        if (s == "forward")
        {
            input >> currentNum;
            forward += currentNum;
        }
        else if (s == "down")
        {
            input >> currentNum;
            down += currentNum;
        }
        else if (s == "up")
        {
            input >> currentNum;
            down -= currentNum;
        }
        input >> s;
    }

    std::cout << "Part 1";
    std::cout << "depth: " << down << " horizontal: " << forward << "\nhorizontal x depth: " << forward * down << "\n\n\n";
    input.close();
}

void part2()
{
    std::ifstream input;
    input.open("../../Day-2-input.txt");

    //error check
    if (input.fail())
    {
        std::cerr << "error opening file";
        exit(1);
    }

    int horizontalPos = 0;
    int depth = 0;
    int aim = 0;

    int currentNum = 0;

    std::string s;
    input >> s;

    while (!input.eof())
    {
        if (s == "down")
        {
            input >> currentNum;
            aim += currentNum;
        }
        else if (s == "up")
        {
            input >> currentNum;
            aim -= currentNum;
        }
        else if (s == "forward")
        {
            input >> currentNum;
            horizontalPos += currentNum;
            depth += (aim * currentNum);
        }

        input >> s;
    }

    std::cout << "Part 2";
    std::cout << "depth: " << depth << " horizontal: " << horizontalPos << "\nhorizontal x depth: " << horizontalPos * depth << "\n\n\n";
    input.close();
}
int main()
{
    part1();
    part2();
}


