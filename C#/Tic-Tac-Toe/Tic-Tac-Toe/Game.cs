using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    class Game
    {
        public Player Player1 { get; }
        public Player Player2 { get; }
        public Deck GameDeck { get; }
        public Player Winner { get; private set; }
        private Player lastPlayedPlayer;

        public Game(Player player1, Player player2, Deck deck)
        {
            Player1 = player1;
            Player2 = player2;
            GameDeck = deck;
        }

        public void Turn()
        {
            Player currentPlayer = DeterminePlayer();
            Console.WriteLine($"Now {currentPlayer.Name} turn");
            GameDeck.ShowDeck();
            GameDeck.AddMark(currentPlayer.Mark);
            lastPlayedPlayer = currentPlayer;
            Console.Clear();
        }

        public bool IsFinished()
        {
            bool checkResult = GameDeck.CheckState();
            if (checkResult)
            {
                if (GameDeck.WinnerMark == Player1.Mark)
                    Winner = Player1;
                else if (GameDeck.WinnerMark == Player2.Mark)
                    Winner = Player2;
                else
                    Winner = null;

                return true;
            }
            else
                return false;
        }

        private Player DeterminePlayer()
        {
            if (lastPlayedPlayer == Player2 || lastPlayedPlayer == null)
                return Player1;
            else
                return Player2;
        }

        public void AnnounceResult()
        {
            GameDeck.ShowDeck();
            if (Winner == Player1 || Winner == Player2)
                Console.WriteLine($"Congratulations dear {Winner.Name} you are win!");
            else
                Console.WriteLine("There are no winner, it is DRAW!!!");
        }
    }
}
/* Draw
     x | o | x
    ---+---+---
     x | o | o
    ---+---+---
     o | x | x
 */