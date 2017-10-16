using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello players.");
            Console.WriteLine("Player №1 enter your name.");
            string firstPlayerName = Console.ReadLine();
            Console.WriteLine("Player №2 enter your name.");
            string secondPlayerName = Console.ReadLine();

            var player1 = new Player(firstPlayerName, 1);
            var player2 = new Player(secondPlayerName, 2);
            var deck = new Deck();

            Console.WriteLine("The game begins.");
            var game = new Game(player1, player2, deck);

            while (!game.IsFinished())
                game.Turn();

            game.AnnounceResult();
        }
    }
}