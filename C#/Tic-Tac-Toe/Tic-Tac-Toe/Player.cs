using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tic_Tac_Toe
{
    class Player
    {
        public string Name { get; }
        public byte Mark { get; }

        public Player(string name, byte mark)
        {
            Name = name;
            Mark = mark;
        }
    }
}
