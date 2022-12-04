#include <iostream>
#include <string>
#include <fstream>

void part1()
{
    std::ifstream input;
    input.open("../../Day-1-input.txt");

    //error check
    if (input.fail())
    {
        std::cerr << "error opening file";
        exit(1);
    }

    //std::string item;
    int previous = 0;
    input >> previous;
    int current = 0;

    int count = 0;

    while (!input.eof())
    {
        input >> current;

        if (current > previous)
        {
            count++;
        }

        previous = current;

    }

    std::cout << "Part 1:\n";
    std::cout << "number of meshurements larger then previous: " << count;
    input.close();
}


void part2()
{
    std::ifstream input;
    input.open("../../Day-1-input.txt");

    //error check
    if (input.fail())
    {
        std::cerr << "error opening file";
        exit(1);
    }

    //std::string item;
    int first = 0;
    input >> first;

    int second = 0;
    input >> second;

    int third = 0;
    input >> third;

    int previous = first + second + third;
    int current = 0;

    int count = 0;

    while (!input.eof())
    {
        first = second;
        second = third;
        input >> third;
        current = first + second + third;

        if (current > previous)
        {
            count++;
        }

        previous = current;

    }

    std::cout << "\n\n\nPart 2:\n";
    std::cout << "number of windows larger then previous: " << count;
    std::cout << "\n\n\n";
    input.close();
}
int main()
{
    part1();
    part2();

}

