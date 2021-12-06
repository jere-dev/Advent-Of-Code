#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

struct BingoBoard
{
    void SolveBoard(const std::vector<int>& randomNumbers)
    {
        for (int i = 0; i < randomNumbers.size(); i++)
        {
            int currentNum = randomNumbers[i];
            //find marked number in vector
            auto findResult = std::find(numbers.begin(), numbers.end(), randomNumbers);
            //if findresult is numbers end continue
            if (findResult == numbers.end())
            {
                continue;
            }
    
            //offset findresult
            int currenNumIndex = findResult - randomNumbers.begin();
            //set marked
            marked[currenNumIndex] = true;
    
            //check if row is complete 
            auto currentRow = currenNumIndex / 5;
            auto RowStartIndex = currentRow * 5;
            auto bRowComplete = true;
            for (int j = RowStartIndex; j < RowStartIndex + 5; j++)
            {
                if (!marked[j])
                {
                    bRowComplete = false;
                    break;
                }
            }
    
            //check if column is complete
            auto currentColumn = currenNumIndex % 5;
            auto bColumnComplete = true;
            for (int j = currentColumn; j < marked.size(); j += 5)
            {
                if (!marked[j])
                {
                    bColumnComplete = false;
                    break;
                }
            }
    
            //if row or column completed, score 
            int sumOfUnmarked = 0;
            if (bRowComplete || bColumnComplete)
            {
                WinnningTurn = i;
                for (int j = 0; j < marked.size(); j++)
                {
                    if (!marked[j])
                    {
                        sumOfUnmarked += numbers[j];
                    }
                }
                FinalScore = sumOfUnmarked * currentNum;
            }
        }
    }
    
    std::vector<int> numbers;
    std::vector<bool> marked;
    int FinalScore;
    int WinnningTurn;
};

std::vector<std::string> readfile(const char* filepath)
{
    std::fstream input;
    input.open(filepath, std::ios::in);
    if (!input.is_open())
    {
        std::cerr << "not open";
        exit(1);
    }
    std::vector<std::string> filelines;
    std::string line;
    while (!input.eof())
    {
        input >> line;
        filelines.push_back(line);
    }
    input.close();

    return filelines;
}
int main()
{
    std::vector<std::string> input = readfile("../../Day-4-input.txt");
    
    //read random numbers 
    std::vector<int> randomNumbers;
    std::stringstream NumberStream{ input[0] };
    std::string curentline;
    while (std::getline(NumberStream, curentline, ','))
    {
        randomNumbers.push_back(std::atoi(curentline.c_str()));
    }
    
    //read bingoBoards
    std::vector<BingoBoard> BingoBoards;
    int nextLine = 1;
    while (nextLine + 25 <= input.size()-2)
    {
        BingoBoard CurrentBoard;
        for (int i = nextLine; i < nextLine + 5; ++i)
        {
            for (int j = 0; j < 5; ++j)
            {
                int CurrentNumber;
                
                if (i * 5 - 4 + j <= input.size()-1)
                {
                    CurrentNumber = std::stoi(input[i * 5 - 4 + j]);
                    CurrentBoard.numbers.push_back(CurrentNumber);
                    CurrentBoard.marked.push_back(false);
                }
            }
        }

        BingoBoards.push_back(CurrentBoard);

        nextLine += 5;
    }
    
    for (auto board = BingoBoards.begin(); board != BingoBoards.end(); /* NOTHING */)
    {
        if ((*board).numbers.size() == 0)
            board = BingoBoards.erase(board);

        else
        {
            ++board;
            (*board).SolveBoard(randomNumbers);
        }

    }

    
}
