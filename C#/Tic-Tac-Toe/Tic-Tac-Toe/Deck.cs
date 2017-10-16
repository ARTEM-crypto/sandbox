using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    class Deck
    {
        public byte[] Squares { get; }
        public byte WinnerMark { get; private set; } = 0;
        private byte turn;

        public Deck()
        {
            Squares = new byte[10];
            turn = 1; 
        }

        public void ShowDeck()
        {
            int first = 0;
            int second = 1;
            int third = 2;

            for (int i = 0; i < 5; i++)
            {
                if (i % 2 == 0)
                {
                    Console.WriteLine($" {ShowSquareMark(first)} | {ShowSquareMark(second)} | {ShowSquareMark(third)} ");
                    first += 3;
                    second += 3;
                    third += 3;
                }
                else
                    Console.WriteLine("---+---+---");
            }
        }

        public string ShowSquareMark(int position)
        {
            if (Squares[position] == 1)
                return "x";
            else if (Squares[position] == 2)
                return "o";
            else
                return " ";
        }

        public void AddMark(byte mark)
        {
            bool marked = false;
            while (marked != true)
            {
                int position = Convert.ToInt32(Console.ReadLine());
                int indexOfPosition = position - 1;
                if (IsSquareEmpty(indexOfPosition))
                {
                    Squares[indexOfPosition] = mark;
                    turn++;
                    break;
                }
                else
                    Console.WriteLine("This square already taken");
            }
        }

        public bool IsSquareEmpty(int position)
        {
            if (Squares[position] != 1 && Squares[position] != 2)
                return true;
            else
                return false;
        }

       
        public bool CheckState()
        {
            byte checkResult = DeckStateChecker.CheckWinner(Squares);
            if (checkResult == 0 && turn < 10)
                return false;
            else
            {
                WinnerMark = checkResult;
                return true;
            }
        }
    }
}
