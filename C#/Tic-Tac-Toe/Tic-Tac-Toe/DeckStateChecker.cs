using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    class DeckStateChecker
    {
        public static byte CheckWinner(byte[] squares)
        {
            if (CompareSquares(squares, 0, 1, 2))
                return squares[0];
            else if (CompareSquares(squares, 3, 4, 5))
                return squares[3];
            else if (CompareSquares(squares, 6, 7, 8))
                return squares[6];
            else if (CompareSquares(squares, 3, 4, 5))
                return squares[3];
            else if (CompareSquares(squares, 0, 3, 6))
                return squares[0];
            else if (CompareSquares(squares, 1, 4, 7))
                return squares[1];
            else if (CompareSquares(squares, 2, 5, 8))
                return squares[2];
            else if (CompareSquares(squares, 0, 4, 8))
                return squares[0];
            else if (CompareSquares(squares, 2, 4, 6))
                return squares[2];
            else
                return 0;
        }

        private static bool CompareSquares(byte[] squares, byte a, byte b, byte c)
        {
            if (squares[a] == squares[b] && squares[b] == squares[c])
                return true;
            else
                return false;
        }
    }   
}
/* Positions
     0 | 1 | 2 
    ---+---+---
     3 | 4 | 5
    ---+---+---
     6 | 7 | 8
*/
